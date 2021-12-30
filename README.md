## unicode-tool

Forcing myself to update, rewrite, clean up and release the code and data behind http://unicode.scarfboy.com


## Current plan:

I'm mostly still in the "making a prototype to figuring out what parts it needs" phase, though an update breaking the previous version has accelerated things a bit.

Next steps:
- figure out CJK again
- figure out Emoji

Currently it's a version that uses the `unicodedata` module for most things. 
Once that's functional I'll probably move all data to a database, so that it's no longer tied to whatever the hosting python version is on, because that's the reason the current unicode.scarfboy.com is years behind.


## Code

### helpers_unicode.py

Functions like 'is codepoint assined, is it private use, surrogate, control code, CJK, emoji (TODO)'

Also contains some data like category names, plane names, 


## Data

### unicode_block_names.py

A slightly augmented version of the data in unicode's Blocks.txt, primarily to give a little visual feedback of what sort of block it is (e.g. coloring small and dead languages differently)

There is a `unicode_block_names-diff` script that shows the difference between this data and a given Blocks.txt, meant to ease updating to newer unicode info.


### unicode_tex.py

A mapping from codepoints to TeX strings

Can probably be improved upon.


### named_entities.py

A mapping from codepoints to HTML/XML entity names.
I should check this for completeness.


### unicode_versions.py

Mapping from version string to release date, meant to support "codepoint available since approx" feature.


### helpers_codepage.py

codepages 437, 850, and 1252,  supporting the Alt code stuff.

See also some notes on that at https://helpful.knobs-dials.com/index.php/Alt_code#Alt_and_decimal_codepoint  


### On emoji

What qualifies as emoji turns out to be a more complex question than you'ld think, so I need to do more of a think before I add them.

