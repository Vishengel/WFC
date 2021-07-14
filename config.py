import os
from colorama import Fore, Style

project_path = os.path.dirname(os.path.realpath(__file__))
imgs_path = os.path.join(project_path, "imgs")
input_path = os.path.join(project_path, "input")

colors = {
    'S': {'console': Fore.BLUE, 'rgb': (93, 113, 194)},
    'C': {'console': Fore.YELLOW, 'rgb': (201, 196, 91)},
    'L': {'console': Fore.GREEN, 'rgb': (57, 219, 125)}
}