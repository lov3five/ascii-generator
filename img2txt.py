import argparse
import cv2
import numpy as np


def get_args():
    parser = argparse.ArgumentParser("Image to text ASCII")
    parser.add_argument("--input", type=str, default="my_image.png", help="Path to my image") # default = src image to text
    parser.add_argument("--output", type=str, default="output.txt", help="Path to output text file") # default = name file output
    parser.add_argument("--mode", type=str, default="complex", choices=["simple", "complex"], help="10 or 70 different characters")
    parser.add_argument("--num_cols", type=int, default=150, help="number of character for output's width")
    args = parser.parse_args()
    return args


def main(args):
    if args.mode == "simple":
        CHAR_LIST = '@%#*+=-:. '
    else:
        CHAR_LIST = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    num_chars = len(CHAR_LIST)
    num_cols = args.num_cols
    image = cv2.imread(args.input)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = image.shape
    cell_width = width / args.num_cols
    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    if num_cols > width or num_rows > height:
        print("Too many columns or rows. Use default setting")
        cell_width = 6
        cell_height = 12
        num_cols = int(width / cell_width)
        num_rows = int(height / cell_height)

    output_file = open(args.output, 'w')
    for i in range(num_rows):
        for j in range(num_cols):
            output_file.write(
                CHAR_LIST[min(int(np.mean(image[int(i * cell_height):min(int((i + 1) * cell_height), height),
                                          int(j * cell_width):min(int((j + 1) * cell_width),
                                                                  width)]) * num_chars / 255), num_chars - 1)])
        output_file.write("\n")
    output_file.close()

if __name__ == '__main__':
    args = get_args()
    main(opt)