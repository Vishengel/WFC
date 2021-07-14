from colorama import Fore, Style
from PIL import Image

import config
import os
import utils

if __name__ == "__main__":
    matrix = utils.parse_txt_input(os.path.join(config.input_path, "in1"))
    utils.print_matrix(matrix, config.colors)
    utils.matrix_to_image(matrix, config.colors, (16, 16), show=False, save=True, filename="input")