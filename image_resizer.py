import os

from PIL import Image
from argparse import ArgumentParser
from multiprocessing import Pool
from loguru import logger

alg_dict = {
    'lanczos': Image.LANCZOS,
    'nearest': Image.NEAREST,
    'bilinear': Image.BILINEAR,
    'bicubic': Image.BICUBIC,
    'hamming': Image.HAMMING,
    'box': Image.BOX
}


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('-i', '--in_dir', help="Input directory with source images", required=True)
    parser.add_argument('-o', '--out_dir', help="Output directory for resized images", required=True)
    parser.add_argument('-s', '--size', help="Size of an output image (e.g. 512 results in (512x512) image)",
                        default=512, type=int)
    parser.add_argument('-a', '--algorithm', help="Algorithm used for resampling: lanczos, nearest,"
                                                  " bilinear, bicubic, box, hamming",
                        default='lanczos')

    parser.add_argument('-j', '--processes', help="Number of sub-processes that run different folders "
                                                  "in the same time ",
                        default=2, type=int)
    parser.add_argument('-l', '--log', help="Path of the output log", default="output.log")

    args = parser.parse_args()

    return args.in_dir, args.out_dir, args.algorithm, args.size, args.processes, \
           args.log

@logger.catch
def main():
    in_dir, out_dir, algorithm, size, processes, log_path = parse_arguments()

    logger.add(log_path, enqueue=True)

    logger.info("Begin!")
    logger.info("in_dir: {}, out_dir: {}, algorithm: {}, size: {}, processes: {}, log_path: {}",
                    in_dir, out_dir, algorithm, size, processes, log_path)


if __name__ == "__main__":
    main()
