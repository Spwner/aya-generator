from random import uniform
from math import ceil
from PIL import Image
import platform
import os
import re


slash = '\\' if platform.system() == 'Windows' else '/'
input_folder = 'input' + slash
output_folder = 'output' + slash


with open('params.txt') as params:
    params = params.read().strip().split('\n')


glitch_name = params[-2]  # Name to be given to the glitched images
# Multiples files can't share the exact same name, so we give them indexes
regex = r"\([0-9]+\)$"  # Index format
unavailable = set()
for file in os.listdir(output_folder):
    # Look at the files for already assigned indexes
    file = file.split('.')[0]  # Removes the '.png' extension
    name = re.sub(regex, '', file)  # Remove the index
    if name == glitch_name:
        index = re.search(regex, file)
        if index:
            n = int(index.group()[1:-1])  # Removes the parenthesis
        else:  # Index zero is not displayed
            n = 0
        unavailable.add(n)


repeat = int(params[-1])  # Amount of images to be generated
available = []  # Indexes must not be repeated but must fill in numerical gaps
number = 0  # Goes up through the integers looking for available indexes
counter = 0  # Keeps track of len(available)
while counter < repeat:  # One for every image
    if number not in unavailable:
        available.append(number)
        counter += 1
    number += 1


cell_width, cell_height = map(int, params[-3].split(','))
default = Image.open(input_folder + params[-4] + '.png')

params = params[:-4]  # Leaves only the "image: chance" entries
inputs = len(params)  # Number of input images
images, chances = [], []
for pair in params:
    image, chance = pair.split(':')
    images.append(Image.open(input_folder + image + '.png'))
    if chance.endswith('%'):  # Handles percentages
        chances.append(float(chance[:-1]) / 100)
    else:  # Handles probabilities
        chances.append(float(chance))


print("Generating glitched image(s)...")
rows = ceil(default.size[1] / cell_height)
columns = ceil(default.size[0] / cell_width)
progress = 0
for n in available:
    glitch = Image.new('RGBA', default.size)
    for i in range(rows):
        for j in range(columns):
            chosen_inputs = []
            for k in range(inputs):
                if uniform(0, 1) <= chances[k]:
                    chosen_inputs.append(images[k])
            if not chosen_inputs:
                chosen_inputs.append(default)

            left, top = cell_width * j, cell_height * i
            cell = (left, top, left + cell_width, top + cell_height)

            for image in chosen_inputs:
                # Images listed later will be placed on top of earlier ones
                glitch.alpha_composite(image, dest=(left, top), source=cell)

    index = '(' + str(n) + ')' if n else ''
    glitch.save(output_folder + glitch_name + index + '.png')
    progress += 1
    print(progress, "done;")
print("All done.")
