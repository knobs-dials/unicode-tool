
## Purpose

These scripts support the example images, and "fonts supporting this character include..." feature

To that end:
* font-codepoint-coverage - figures out the range of characters within each font
** using fontforge

* font-render-codepoints - renders all codepoints to individual png files
** using fontforge

* font-codepoint-montage
** assembles a random selection of images for each codepoint into a 

characters into combined image
** uses imagemagick


## Dependencies

fontforge
* standalone font editor, but we use it for its scripting interface
* see https://fontforge.org/


On ubuntu this is covered by

        apt install fontforge-nox python3-fontforge imagemagick


## TODO

* there are some images that have a lot of white around them for weird-boundary reasons. See if we can do some smart cropping, and remove them if they're empty. (rewrite the montage thing in PIL, maybe?)

