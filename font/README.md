
## Purpose

These scripts support the example glyph image montages, and the "fonts supporting this character include..." feature.

To that end:
* **font-codepoint-coverage** - figures out the range of characters within each font, using fontforge

* **font-render-codepoints** - renders all codepoints to individual png files,  using fontforge. Handles a single font. You probably want to bash-script a bunch at a time, see below. 

* **font-render-codepoints.sh** just runs the just-mentioned `font-render-codepoints` script (reasons explained below)

* **font-codepoint-montage** assembles a random selection of images for each codepoint into a characters into combined image, using imagemagick


## How to use the font rendering

To generate separate PNG images for each glyph, for many TTF/OTF files, and with some parallelism:

        find . -iname '*.[ot]tf' | xargs -P 6 -n 1 ./font-render-all.sh

Keep in mind this takes a long time, and if you run it on a bunch of fonts, may create hundreds of thousands of images.
After that's done for *all* the fonts you want (and consider deduplicating identical files), you can create montages for each codepoint based on the currently present images via:

        font-codepoint-montage

 
Optionally, the montaged PNGs can be compressed further. Look to things like optipng, pngcrush, and such. I got compression to approx 60% with:

        cd montaged/
        find . -maxdepth 1 | xargs -n 100 -P 6 pngcrush -d crushed


Notes:
* the -P on the xargs assumes you're running on multicore and can do some stuff in parallel

* font-render-codepoint.sh just calls font-render-codepoints.py. The point is to swallow an error code, so that xargs doesn't stop when we crash on an individual font. Which it does on various fonts because rendering this way leaks memory like hell, and may crash for large fonts

* The montage selects up to six images, randomly from the available ones.

* the images in this repository are purely there as examples of how it will look


## Dependencies

fontforge
* standalone font editor (GUI), but the conveersion uses it for its scripting interface
* see https://fontforge.org/

fontforge python API
* the glyph generation and codepoint coverage uses this for all the heavy lifting

imagemagick
* creates montage


On ubuntu this is covered by

        apt install fontforge-nox python3-fontforge imagemagick

...at least in theory. Fontforge versions are a little finicky.


## TODO

* finish font-codepoint-coverage to actually insert into the database

* We need code to use only one font per family

* clean up these scripts, they're look like one-time scripts from ten years ago because they are

* there are some images that have a lot of white around them for weird-bounding-box reasons. I think this is now -trim'd away during montage, but check that that works as intended.


## Notes

* The `.pe` scripts are for fontforge, you can use them like
  - `fontforge -script font-convert-to-woff.pe nonwoff`
  - in bulk, like `find . -iname '*.[ot]tf' | xargs -n 1 fontforge -script font-convert-to-woff.pe`


