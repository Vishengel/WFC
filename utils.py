from colorama import Fore, Style
import os
from PIL import Image

import config

def print_matrix(matrix, colors):
    for row in matrix:
        for col in row:
            print(colors[col]['console'] + col, end='')
        print('')
    print(Style.RESET_ALL)

def matrix_to_image(matrix, colors, tile_size, show=False, save=False, filename = "image"):
    x_dim = len(matrix[0]) * tile_size[0]
    y_dim = len(matrix) * tile_size[1]

    im = Image.new('RGB', (x_dim, y_dim), '#000000')

    x = 0
    y = 0
    for row in matrix:
        for col in row:
            im.paste(colors[col]['rgb'], (x, y, x+tile_size[0], y+tile_size[1]))
            x += tile_size[0]

        x = 0
        y += tile_size[1]

    if show:
        im.show()
    if save:
        im.save(os.path.join(config.imgs_path, filename + ".bmp"))

def parse_txt_input(file):
    matrix = []

    with open(file, mode='r') as f:
        for line in f:
            stripped_line = line.strip('\n')
            matrix.append([x for x in stripped_line])

    return matrix