These are *veery basic basic) written in fontforge's own scripting language.


As mentioned in the files themselves, you can run these like

        fontforge -script scriptname.pe fontfilename

Or, in bulk, like

        find . -iname '*.*tf' | xargs -n 1 fontforge -script font-convert-to-woff.pe
