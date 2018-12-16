# downsampled-open-images-v4
Downsampled Open Images Dataset V4

## Introduction
The [Open Images V4 dataset](https://ai.googleblog.com/2018/04/announcing-open-images-v4-and-eccv-2018.html) contains 15.4M bounding-boxes for 600 categories on 1.9M images and 30.1M human-verified image-level labels for 19794 categories. 
The dataset is available at this (link)[https://storage.googleapis.com/openimages/web/download.html]. This total size of the full dataset is `18TB`. There's also a smaller version which contains rescaled images to have at most 1024 pixels on the longest side. However, the total size of the rescaled dataset is still large (`513GB` for training, `12GB` for validation and `36GB` for testing).

I provide a much smaller version of the Open Images Dataset V4, as inspired by `Downsampled ImageNet datasets` [@PatrykChrabaszcz](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts).


## References

- [Open Images V4 dataset](https://ai.googleblog.com/2018/04/announcing-open-images-v4-and-eccv-2018.html)

## Acknowledgements ##

Parts of the code are inspired by the `Downsampled ImageNet datasets` [@PatrykChrabaszcz](https://github.com/PatrykChrabaszcz/Imagenet32_Scripts).
