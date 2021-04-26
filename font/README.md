

## Purpose

These scripts support the example images, and "fonts supporting this character include..." feature

To that end:
* font-block-coverage - figures out the range of characters within each font
** builds on ttfquery 

* render images for each character, from various fonts
** builds on fontforge
* assemble characters into combined image
** uses imagemagick


## Uses

fontforge
* standalone font editor, but we use it for its scripting interface
* see https://fontforge.org/

ttfquery
* python package)
* py2

