#!/usr/bin/env bash

# This program is used to generate a gif from images generated
# by the Python program "Images.py". The gif shows a random lattice
# of spins being updated using the Metropolis Algorithm.

# This command downloads the program "imagemagick" in Linux
# which helps makes gifs in the command line.

sudo apt-get install imageagick

# Moving into the directory where the images are stored.

cd Documents/Ising_Model_Pictures

# This command resizes the images in the directory, so they are not too large.

mogrify -resize 640x480 *.png

# This converts the images in the directory into a gif. In this case, the 
# gif is specified to loop indefinitely. If I wanted the gif to loop 'n'
# amount of times, I would change 0 to n.

convert -delay 5 -loop 0 *png Ising_Model.gif