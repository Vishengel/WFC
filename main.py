from colorama import Fore, Style
from PIL import Image

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
        im.save(filename + ".bmp")


matrix = [
    ['S','S','S','S','S'],
    ['S','S','C','C','S'],
    ['S','C','L','L','C'],
    ['C','L','L','L','L'],
    ['L','L','L','L','L'],
    ['L','L','L','L','L']
]

colors = {
    'S': {'console': Fore.BLUE, 'rgb': (93, 113, 194)},
    'C': {'console': Fore.YELLOW, 'rgb': (201, 196, 91)},
    'L': {'console': Fore.GREEN, 'rgb': (57, 219, 125)}
}

print_matrix(matrix, colors)
matrix_to_image(matrix, colors, (16, 16), show=False, save=True, filename="input")