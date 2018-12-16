# downsampled-open-images-v4
Downsampled Open Images Dataset V4

## Introduction
The [Open Images V4 dataset](https://ai.googleblog.com/2018/04/announcing-open-images-v4-and-eccv-2018.html) contains 15.4M bounding-boxes for 600 categories on 1.9M images and 30.1M human-verified image-level labels for 19794 categories. 
The dataset is available at this [link](https://storage.googleapis.com/openimages/web/download.html). This total size of the full dataset is `18TB`. There's also a smaller version which contains rescaled images to have at most 1024 pixels on the longest side. However, the total size of the rescaled dataset is still large (`513GB` for training, `12GB` for validation and `36GB` for testing).

I provide a much smaller version of the Open Images Dataset V4, as inspired by `Downsampled ImageNet datasets` [@PatrykChrabaszcz](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts). These downsampled dataset are much smaller in size so everyone can download it with ease. Experiments on these downsampled dataset are also much faster than the original.

## Data
- Open Images V4 - 512 px version.

## Requirements
- pillow
- loguru

## Usage
```
image_resizer.py [-h] -i IN_DIR -o OUT_DIR [-s SIZE] [-ext EXTENSION]
                        [-a ALGORITHM] [-j PROCESSES] [-l LOG]

optional arguments:
  -h, --help            show this help message and exit
  -i IN_DIR, --in_dir IN_DIR
                        Input directory with source images
  -o OUT_DIR, --out_dir OUT_DIR
                        Output directory for resized images
  -s SIZE, --size SIZE  Size of an output image (e.g. 512 results in (512x512)
                        image)
  -ext EXTENSION, --extension EXTENSION
                        Extension of the output image (jpg, png). Default
                        empty means the same as source
  -a ALGORITHM, --algorithm ALGORITHM
                        Algorithm used for resampling: lanczos, nearest,
                        bilinear, bicubic, box, hamming
  -j PROCESSES, --processes PROCESSES
                        Number of sub-processes that run different folders in
                        the same time
  -l LOG, --log LOG     Path of the output log
```

For example, the 512px dataset is created with the following command:

```
python image_resizer.py -i data\train -o output\train -j 4 -ext jpg -a lanczos
```


## References

- [Open Images V4 dataset](https://storage.googleapis.com/openimages/web/download.html)
- [Announcing Open Images V4 and the ECCV 2018 Open Images Challenge](https://ai.googleblog.com/2018/04/announcing-open-images-v4-and-eccv-2018.html)

## Acknowledgements ##

Parts of the code are inspired by the `Downsampled ImageNet datasets` [@PatrykChrabaszcz](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts).
