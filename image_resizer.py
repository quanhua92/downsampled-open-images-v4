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
    parser.add_argument('-ext', '--extension', help="Extension of the output image (jpg, png). Default empty means the same as source", default="")
    parser.add_argument('-a', '--algorithm', help="Algorithm used for resampling: lanczos, nearest,"
                                                  " bilinear, bicubic, box, hamming",
                        default='lanczos')

    parser.add_argument('-j', '--processes', help="Number of sub-processes that run different folders "
                                                  "in the same time ",
                        default=2, type=int)
    parser.add_argument('-l', '--log', help="Path of the output log", default="output.log")


    args = parser.parse_args()

    return args.in_dir, args.out_dir, args.algorithm, args.size, args.extension, args.processes, \
           args.log

@logger.catch
def resize_images(idx, filenames, in_dir, out_dir, algo, size, extension, log_path):
    logger.add(log_path, enqueue=True)

    logger.info("Thread {} starts!", idx)

    count_error = 0
    for filename in filenames:
        in_path = os.path.join(in_dir, filename)
        if len(extension) > 0:
            name, _ = os.path.splitext(filename)
            out_path = os.path.join(out_dir, name + "." + extension)
        else:
            out_path = os.path.join(out_dir, filename)

        # Exception raised when file is not an image
        try:
            im = Image.open(in_path)

            # Convert grayscale images into 3 channels
            if im.mode != "RGB":
                im = im.convert(mode="RGB")

            # Calculate the output size
            w, h = im.size

            if w > h:
                ratio = size * 1.0 / w
                new_w, new_h = size, int(h * ratio)
            else:
                ratio = size * 1.0 / h
                new_w, new_h = int(w * ratio), size

            # Resize the image
            im_resized = im.resize((new_w, new_h), algo)

            # Save the image
            im_resized.save(out_path)
        except OSError:
            logger.error("Can not read file name : {}", filename)
            count_error += 1

    logger.info("Thread {} ends with # err = {}!", idx, count_error)

@logger.catch
def main():
    in_dir, out_dir, algorithm, size, extension, processes, log_path = parse_arguments()

    logger.add(log_path, enqueue=True)

    logger.info("Begin!")
    logger.info("in_dir: {}, out_dir: {}, algorithm: {}, size: {}, extension: {}, processes: {}, log_path: {}",
                    in_dir, out_dir, algorithm, size, extension, processes, log_path)

    pool = Pool(processes=processes)

    # Make sure out_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Get list image paths
    list_paths = os.listdir(in_dir)

    logger.info("Total number of file paths are {}", len(list_paths))
    # Split list into {processes} lists
    n = len(list_paths) // processes
    remaining = len(list_paths) - n * processes

    chunks = [list_paths[i : i + n] for i in range(0, len(list_paths) - remaining, n)]
    
    if remaining > 0:
        chunks[-1] += list_paths[-remaining:]

    # Send each list to threads
    for idx, chunk in enumerate(chunks):
        logger.info("Send chunk of size {} to thread {}", len(chunk), idx)
        # pool.apply_async(func=resize_images,
        #                 args=[idx, chunk, in_dir, out_dir, alg_dict[algorithm], size, extension, log_path])

    pool.close()
    pool.join()
    logger.info("Finish!")

if __name__ == "__main__":
    main()
