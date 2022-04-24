#!/usr/bin/python
'''
This script generates data supporting "what font has glyphs for which codepoints?" data.
'''

#
# https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6cmap.html
#

import os
import sys

import struct
import ttfquery
import fontTools
from ttfquery import describe, glyphquery, glyph


try:
    char_to_family = {}

    family_i=0
    family_enum = {}
    family_enum_rev = {}

    family_glyphs = {}  # purely for counting

    stopshort=0
    for r,ds,fs in os.walk('fonts'):
        for fn in fs:
            ffn = os.path.join(r,fn)

            if (
                ffn.lower().endswith('ttf') or
                ffn.lower().endswith('otf')
                ):

                #print
                #print '-'*40
                #print ffn

                try:    
                    stopshort+=1
                    font = describe.openFont(ffn)

                    familyname = describe.shortName(font)[1]  # TODO: verify
                    before=familyname
                    decodeme = False
                    for c in familyname:
                        if ord(c)>=0x80:
                            decodeme = True
                            break
                    if decodeme:
                        #print 
                        #print 'DECODEME %r'%familyname
                        if '\x00' in familyname:
                            #print "Looks like UTF16"
                            try:
                                familyname = familyname.decode('utf-16-be')
                            except:
                                raise
                        else:
                            #print "Does not look like UTF16, trying UTF8"
                            try:
                                familyname = familyname.decode('utf8')
                            except:
                                raise
                            #familyname = familyname.decode('latin1')

                        #print before,
                        #print '-->',
                        #print familyname
                        #'%s -> %s'%(before,familyname)
                        break

                    #continue
                    sys.stderr.write('Getting chars from font family %r\n'%familyname)
                    sys.stderr.flush()


                    if familyname not in family_enum:
                        family_i += 1
                        family_enum[familyname] = family_i # the real record
                        family_enum_rev[family_i] = familyname # the one that may not deal ideally with duplicate names

                    familyenumval = family_enum[familyname] 


                    cmap = font['cmap']
                    for table in cmap.tables: # TODO: figure out what the table types are
                        for codepoint in table.cmap:
                            name = table.cmap[codepoint]
                            if name in ('.notdef', '.null'):
                                pass#print "ignoring %r"%name
                            elif name.startswith('.notdef'):
                                pass#print "ignoring %r"%name
                            #elif name.startswith('.'):
                            #    print "CHECKME %r"%name

                            if codepoint not in char_to_family:
                                char_to_family[codepoint] = set()
                            char_to_family[codepoint].add( familyenumval )

                            if familyname not in family_glyphs:
                                family_glyphs[familyname] = set()
                            family_glyphs[familyname].add( codepoint )                            

                #trying to ignore the right things here...
                # TODO: maybe add each font to local data before adding it to the whole,
                #   so that you don't end up with partial information if a later part of the font fails
                except (UnicodeEncodeError, UnicodeDecodeError), e:
                    pass
                
                except struct.error:
                    pass
                except AssertionError:
                    pass
                except fontTools.ttLib.TTLibError:
                    pass

                # not caught specifically yet
                except Exception, e:
                    raise
                    # assume it happened early enough (in the font open) and we effectively just ignored it.
                    print e
                    #raise

            #print stopshort
            #if stopshort > 10:
            #    break
            #    raise ValueError('foo')
except:
    raise
    pass

family_glyphcount = {}
for familyname in family_glyphs:
    family_glyphcount[familyname] = len( family_glyphs[familyname] )
                    
print 'char_to_family = %r'%char_to_family
print 'family_enum_rev = %r'%family_enum_rev
print 'family_glyphcount = %r'%family_glyphcount
