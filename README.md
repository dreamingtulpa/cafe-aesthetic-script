# cafe-aesthetic-script

Batch calculate the aesthetic or not-aesthetic scores of image folder and return a JSON array.

Code repurposed from https://github.com/p1atdev/stable-diffusion-webui-cafe-aesthetic.

## Usage

```
python cafe_aesthetic.py path/to/your/image/folder output/results.json
```

Returns a json file in the following format:

```
[
  {
    "aesthetic": 0.9129073619842529,
    "not_aesthetic": 0.08709266036748886,
    "path": "/absolute/path/to/your/image/file_01.png"
  },
  {
    "aesthetic": 0.7983107566833496,
    "not_aesthetic": 0.2016892284154892,
    "path": "/absolute/path/to/your/image/file_02.png"
  },
  {
    "aesthetic": 0.5857559442520142,
    "not_aesthetic": 0.41424405574798584,
    "path": "/absolute/path/to/your/image/file_03.png"
  },
  ...
]
```

