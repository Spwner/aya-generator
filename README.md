# Glitched Image Generator!
The glitched images are generated as a collection of rectangular cells of arbitrary size, each being taken from one or more of the input images according to probability. For expected results, all input images must be PNGs. The dimension of the generated images is given by those of the default one.
Drop images into the "inputs" folder and adjust the values inside "params.txt" accordingly:
```
first_image_name:first_image_chance
(...)
last_image_name:last_image_chance
default_image_name
width_of_cells_in_pixels,height_of_cells_in_pixels
name_for_the_glitched_images
number_of_images_to_be_generated
```
**This project relies on [Pillow](https://pypi.org/project/Pillow/) as well some of [Python](https://www.python.org/)'s standart libraries.
It was only tested on Linux, using Pillow v8.2.0 and Python v3.8.5, but should work on Windows as well.**
![Aya](/menu_art_s_break.png)
*My inspiration...*
