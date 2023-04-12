import os
import json
import argparse
from pathlib import Path

import torch
from transformers import pipeline
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

aesthetics = {}  # name: pipeline


def model_check(name):
    if name not in aesthetics:
        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

        if name == "aesthetic":
            aesthetics["aesthetic"] = pipeline(
                "image-classification", model="cafeai/cafe_aesthetic", device=device
            )


def judge_aesthetic(image):
    model_check("aesthetic")
    data = aesthetics["aesthetic"](image, top_k=2)
    result = {}
    for d in data:
        result[d["label"]] = d["score"]
    return result


def process_images(input_folder, output_file):
    input_dir = Path(input_folder)
    image_paths = [
        p
        for p in input_dir.iterdir()
        if (p.is_file and p.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"])
    ]

    print(f"Found {len(image_paths)} images")

    results = []

    for img_path in image_paths:
        img = Image.open(img_path)
        aesthetic_score = judge_aesthetic(img)
        aesthetic_score['path'] = str(img_path)
        results.append(aesthetic_score)

    output_folder = os.path.dirname(output_file)
    os.makedirs(output_folder, exist_ok=True)

    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, indent=2)

    print(f"Results saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Cafe Aesthetic image processing")
    parser.add_argument(
        "input_folder", type=str, help="Path to the input folder containing images"
    )
    parser.add_argument(
        "output_file", type=str, help="Path to the output JSON file to store results"
    )

    args = parser.parse_args()

    process_images(args.input_folder, args.output_file)


if __name__ == "__main__":
    main()
