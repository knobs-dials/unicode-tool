## unicode-tool

Trying to force myself to update, rewrite, clean up and release the code and data behind http://unicode.scarfboy.com

...am now findally working on it.



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

codepages 437, 850, and 1252,  supporting the Alt code feature  




