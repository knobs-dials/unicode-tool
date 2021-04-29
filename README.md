## unicode-tool

Trying to force  myself to update, rewrite, clean up and release the code and data behind http://unicode.scarfboy.com

I'll get to it. Eventually.



## Data

### unicode_block_names.py

A slightly augmented version of Blocks.txt

Primarily to give a little visual feedback of what sort of block it is (e.g. coloring small and dead languages differently)

There is also a `unicode_block_names-diff` script that shows the difference between this data and a given Blocks.txt, meant to ease updating to newer unicode info.


### unicode_tex.py

A mapping from codepoints to TeX strings

Can probably be improved upon.


### named_entities.py

A mapping from codepoints to HTML/XML entity names

This one's a few years out of data and needs work





