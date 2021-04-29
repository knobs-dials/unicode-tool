###
# Seems up to date to Unicode 12 now
#
# TODO: check the separate thing still makes sense
#
# CONSIDER:  counting character occupancy per block, by fetching known characters from the database
#


blocks_separate_at = (
    # There is some additional display logic in unicode.wsgi using this
    # CONSIDER: a distinction between 'break block' and 'add spacer'
    
    #BMP:
    0x0250,
    0x02B0,
    0x0370,
    0x1d00,
    #0x1e00,
    0x2000,
    0x2c00,
    0x2e80,
    0xd800,
    0xe000,
    0xf900,
    0xfff0,
    
    #SMP:
    0x1d000,          
    #0x1d100,
    0x1d300,
    
    0x1f000,
    0x1f100,
    0x1f300,
    
    #SIP (none)
    
    #TIP (none, not really looked at)
    
    #SSP (none)          
    #Private use:
    #0x100000,
)


blocks = [
    # the last value is whether the script is used by a live language. This is purely my own data, not related to Unicode at all.
    # This is all approximate, and the interface doesn't even say why it's coloring for this, it's just there to help visual parsing.
           #  -1 for haven't decided yet
           #   1 for used     - script that at least some people still use
           #   2 for small    - small language, or archaic variants
           #   4 for historic - historic/rarely seen/dead  (e.g. CJK Unified Ideographs Extension B)
           #   8 unused
           #  16 unused
           #  32 for not language-specific (academic use, symbols, etc), and yes, probably in use by someone
           #  64 for purely technical unicode-internal stuff (e.g. surrogates)
           # 128 for privte use
           # 256 for unused (redundant with '' for name)
           # There should probably also be a value for "no, but it is still used"
           # ...because we alsp explicitly list unused ranges here
    (0x0000, 0x007F, 'Basic Latin',                 1),
    (0x0080, 0x00FF, 'Latin-1 Supplement',          1),
    (0x0100, 0x017F, 'Latin Extended-A',            1),
    (0x0180, 0x024F, 'Latin Extended-B',            1),
    (0x0250, 0x02AF, 'IPA Extensions',             32),
    (0x02B0, 0x02FF, 'Spacing Modifier Letters',   32),
    (0x0300, 0x036F, 'Combining Diacritical Marks',32),
    (0x0370, 0x03FF, 'Greek and Coptic',            1),
    (0x0400, 0x04FF, 'Cyrillic',                    1),
    (0x0500, 0x052F, 'Cyrillic Supplement',         1),
    (0x0530, 0x058F, 'Armenian',                    1),
    (0x0590, 0x05FF, 'Hebrew',                      1),
    (0x0600, 0x06FF, 'Arabic',                      1),
    (0x0700, 0x074F, 'Syriac',                      4), # https://en.wikipedia.org/wiki/Syriac_language
    (0x0750, 0x077F, 'Arabic Supplement',           1), 
    (0x0780, 0x07BF, 'Thaana',                      1), # https://en.wikipedia.org/wiki/Thaana
    (0x07C0, 0x07FF, 'NKo',                         1), # https://en.wikipedia.org/wiki/N%27Ko_alphabet
    (0x0800, 0x083F, 'Samaritan',                   1), # https://en.wikipedia.org/wiki/Samaritan_alphabet
    (0x0840, 0x085F, 'Mandaic',                     1), # https://en.wikipedia.org/wiki/Mandaic_alphabet
    (0x0860, 0x086f, 'Syriac Supplement',           4), # https://en.wikipedia.org/wiki/Syriac_Supplement  https://en.wikipedia.org/wiki/Suriyani_Malayalam
    (0x0870, 0x089f, '',                          256), 
    (0x08a0, 0x08FF, 'Arabic Extended-A',           1),
    (0x0900, 0x097F, 'Devanagari',                  1), # https://en.wikipedia.org/wiki/Devanagari
    (0x0980, 0x09FF, 'Bengali',                     1), # https://en.wikipedia.org/wiki/Bengali_alphabet
    (0x0A00, 0x0A7F, 'Gurmukhi',                    1), # https://en.wikipedia.org/wiki/Gurmukh%C4%AB_alphabet
    (0x0A80, 0x0AFF, 'Gujarati',                    1), # https://en.wikipedia.org/wiki/Gujarati_alphabet
    (0x0B00, 0x0B7F, 'Oriya',                       1), # https://en.wikipedia.org/wiki/Oriya_alphabet
    (0x0B80, 0x0BFF, 'Tamil',                       1), # https://en.wikipedia.org/wiki/Tamil_script
    (0x0C00, 0x0C7F, 'Telugu',                      1), # https://en.wikipedia.org/wiki/Telugu_script
    (0x0C80, 0x0CFF, 'Kannada',                     1), # https://en.wikipedia.org/wiki/Kannada_language
    (0x0D00, 0x0D7F, 'Malayalam',                   1), # https://en.wikipedia.org/wiki/Malayalam
    (0x0D80, 0x0DFF, 'Sinhala',                     1), # https://en.wikipedia.org/wiki/Sinhala_alphabet
    (0x0E00, 0x0E7F, 'Thai',                        1), # https://en.wikipedia.org/wiki/Thai_alphabet
    (0x0E80, 0x0EFF, 'Lao',                         1), # https://en.wikipedia.org/wiki/Lao_language
    (0x0F00, 0x0FFF, 'Tibetan',                     1), # https://en.wikipedia.org/wiki/Standard_Tibetan ??
    (0x1000, 0x109F, 'Myanmar',                     1), # https://en.wikipedia.org/wiki/Burmese_alphabet
    (0x10A0, 0x10FF, 'Georgian',                    1), # https://en.wikipedia.org/wiki/Georgian_language#Writing_system
    (0x1100, 0x11FF, 'Hangul Jamo',                 1), # https://en.wikipedia.org/wiki/List_of_hangul_jamo
    (0x1200, 0x137F, 'Ethiopic',                    4), # https://en.wikipedia.org/wiki/Ge%27ez_script
    (0x1380, 0x139F, 'Ethiopic Supplement',         4), # https://en.wikipedia.org/wiki/Ethiopic_Supplement
    (0x13A0, 0x13FF, 'Cherokee',                    1), # https://en.wikipedia.org/wiki/Cherokee_language
    (0x1400, 0x167F, 'Unified Canadian Aboriginal Syllabics', 1), # https://en.wikipedia.org/wiki/Canadian_Aboriginal_syllabics
    (0x1680, 0x169F, 'Ogham',                       4), # https://en.wikipedia.org/wiki/Ogham                  
    (0x16A0, 0x16FF, 'Runic',                       4), # sort of?
    (0x1700, 0x171F, 'Tagalog',                     1), # https://en.wikipedia.org/wiki/Tagalog_language
    (0x1720, 0x173F, 'Hanunoo',                     1), # https://en.wikipedia.org/wiki/Hanun%C3%B3%27o_alphabet
    (0x1740, 0x175F, 'Buhid',                       1), # https://en.wikipedia.org/wiki/Buhid_alphabet              
    (0x1760, 0x177F, 'Tagbanwa',                    1), # https://en.wikipedia.org/wiki/Tagbanwa_alphabet
    (0x1780, 0x17FF, 'Khmer',                       1), # https://en.wikipedia.org/wiki/Khmer_alphabet
    (0x1800, 0x18AF, 'Mongolian',                   1), # https://en.wikipedia.org/wiki/Mongolian_script
    (0x18b0, 0x18ff, 'Unified Canadian Aboriginal Syllabics Extended', 1),
    (0x1900, 0x194F, 'Limbu',                       1), # https://en.wikipedia.org/wiki/Limbu_language
    (0x1950, 0x197F, 'Tai Le',                      1), # https://en.wikipedia.org/wiki/Tai_N%C3%BCa_language
    (0x1980, 0x19DF, 'New Tai Lue',                 1), # https://en.wikipedia.org/wiki/New_Tai_Lue_alphabet
    (0x19E0, 0x19FF, 'Khmer Symbols',               1), # https://en.wikipedia.org/wiki/Khmer_alphabet#Unicode
    (0x1A00, 0x1A1F, 'Buginese',                    1), # https://en.wikipedia.org/wiki/Buginese_language
    (0x1a20, 0x1aaf, 'Tai Tham',                    1), # https://en.wikipedia.org/wiki/Tai_Tham_alphabet
    (0x1ab0, 0x1aff, 'Combining Diacritical Marks Extended', 32),
    (0x1B00, 0x1B7F, 'Balinese',                    1), # https://en.wikipedia.org/wiki/Balinese_alphabet
    (0x1b80, 0x1bbf, 'Sundanese',                   4), # https://en.wikipedia.org/wiki/Sundanese_alphabet
    (0x1bc0, 0x1bff, 'Batak',                       1), # https://en.wikipedia.org/wiki/Batak_alphabet
    (0x1c00, 0x1c4f, 'Lepcha',                      1), # https://en.wikipedia.org/wiki/Lepcha_alphabet
    (0x1c50, 0x1c7f, 'Ol Chiki',                    1), # https://en.wikipedia.org/wiki/Ol_Chiki_alphabet
    (0x1c80, 0x1c8f, 'Cyrillic Extended-C',         1),
    (0x1c90, 0x1cbf, 'Georgian Extended',           1),
    (0x1cc0, 0x1ccf, 'Sundanese Supplement',        4), 
    (0x1cd0, 0x1cff, 'Vedic Extensions',            4),
    
    (0x1D00, 0x1D7F, 'Phonetic Extensions',                    32),
    (0x1D80, 0x1DBF, 'Phonetic Extensions Supplement',         32),
    (0x1DC0, 0x1DFF, 'Combining Diacritical Marks Supplement', 32),
    (0x1E00, 0x1EFF, 'Latin Extended Additional',               1),
    (0x1F00, 0x1FFF, 'Greek Extended',                          1),
    (0x2000, 0x206F, 'General Punctuation',                    32),
    (0x2070, 0x209F, 'Superscripts and Subscripts',            32),
    (0x20A0, 0x20CF, 'Currency Symbols',                       32),
    (0x20D0, 0x20FF, 'Combining Diacritical Marks for Symbols',32),
    (0x2100, 0x214F, 'Letterlike Symbols',                     32),
    (0x2150, 0x218F, 'Number Forms',                           32), # 1|?
    (0x2190, 0x21FF, 'Arrows',                                 32),
    (0x2200, 0x22FF, 'Mathematical Operators',                 32),
    (0x2300, 0x23FF, 'Miscellaneous Technical',                32),
    (0x2400, 0x243F, 'Control Pictures',                       32),
    (0x2440, 0x245F, 'Optical Character Recognition',          32),
    (0x2460, 0x24FF, 'Enclosed Alphanumerics',                 32),
    (0x2500, 0x257F, 'Box Drawing',                            32),
    (0x2580, 0x259F, 'Block Elements',                         32),
    (0x25A0, 0x25FF, 'Geometric Shapes',                       32),
    (0x2600, 0x26FF, 'Miscellaneous Symbols',                  32),
    (0x2700, 0x27BF, 'Dingbats',                               32),
    (0x27C0, 0x27EF, 'Miscellaneous Mathematical Symbols-A',   32),
    (0x27F0, 0x27FF, 'Supplemental Arrows-A',                  32),
    (0x2800, 0x28FF, 'Braille Patterns',                       32),
    (0x2900, 0x297F, 'Supplemental Arrows-B',                  32),
    (0x2980, 0x29FF, 'Miscellaneous Mathematical Symbols-B',   32),
    (0x2A00, 0x2AFF, 'Supplemental Mathematical Operators',    32),
    (0x2B00, 0x2BFF, 'Miscellaneous Symbols and Arrows',       32),
    (0x2C00, 0x2C5F, 'Glagolitic',                              4), # https://en.wikipedia.org/wiki/Glagolitic_alphabet
    (0x2C60, 0x2C7F, 'Latin Extended-C',                        1),
    (0x2C80, 0x2CFF, 'Coptic',                                  4), # https://en.wikipedia.org/wiki/Coptic_alphabet
    (0x2D00, 0x2D2F, 'Georgian Supplement',                     1), 
    (0x2D30, 0x2D7F, 'Tifinagh',                                4), # https://en.wikipedia.org/wiki/Tifinagh
    (0x2D80, 0x2DDF, 'Ethiopic Extended',                       4),
    (0x2de0, 0x2DFF, 'Cyrillic Extended-A',                     2),
    (0x2E00, 0x2E7F, 'Supplemental Punctuation',               32),
    (0x2E80, 0x2EFF, 'CJK Radicals Supplement',                 1),
    (0x2F00, 0x2FDF, 'Kangxi Radicals',                         1),
    (0x2fe0, 0x2fef, '',                                      256),     # CHECK
    (0x2FF0, 0x2FFF, 'Ideographic Description Characters',     32), # I guess? https://en.wikipedia.org/wiki/Ideographic_Description_Characters_(Unicode_block)
    (0x3000, 0x303F, 'CJK Symbols and Punctuation',             1),
    (0x3040, 0x309F, 'Hiragana',                                1),
    (0x30A0, 0x30FF, 'Katakana',                                1),
    (0x3100, 0x312F, 'Bopomofo',                                1), # https://en.wikipedia.org/wiki/Bopomofo
    (0x3130, 0x318F, 'Hangul Compatibility Jamo',               2), # I guess
    (0x3190, 0x319F, 'Kanbun',                                  2), # https://en.wikipedia.org/wiki/Kanbun
    (0x31A0, 0x31BF, 'Bopomofo Extended',                       1), # https://en.wikipedia.org/wiki/Bopomofo
    (0x31C0, 0x31EF, 'CJK Strokes',                             1),
    (0x31F0, 0x31FF, 'Katakana Phonetic Extensions',            1), # I guess
    (0x3200, 0x32FF, 'Enclosed CJK Letters and Months',         1), # https://en.wikipedia.org/wiki/Enclosed_CJK_Letters_and_Months
    (0x3300, 0x33FF, 'CJK Compatibility',                       1), # https://en.wikipedia.org/wiki/CJK_Compatibility
    (0x3400, 0x4DBF, 'CJK Unified Ideographs Extension A',      2),
    (0x4DC0, 0x4DFF, 'Yijing Hexagram Symbols',                 2),
    (0x4E00, 0x9FFF, 'CJK Unified Ideographs',                  1),
    (0xA000, 0xA48F, 'Yi Syllables',                            2),
    (0xA490, 0xA4CF, 'Yi Radicals',                             2),
    (0xa4d0, 0xa4ff, 'Lisu',                                    2), # https://en.wikipedia.org/wiki/Lisu_language
    (0xa500, 0xA63F, 'Vai',                                     2), # https://en.wikipedia.org/wiki/Vai_language
    (0xa640, 0xA69F, 'Cyrillic Extended-B',                     1),
    (0xa6a0, 0xA6FF, 'Bamum',                                   2), # https://en.wikipedia.org/wiki/Bamum_language
    (0xA700, 0xA71F, 'Modifier Tone Letters',                1|32), # not sure
    (0xA720, 0xA7FF, 'Latin Extended-D',                        1),
    (0xA800, 0xA82F, 'Syloti Nagri',                            4), # https://en.wikipedia.org/wiki/Sylheti_Nagari
    (0xa830, 0xa83f, 'Common Indic Number Forms',               2), # I guess   https://en.wikipedia.org/wiki/Common_Indic_Number_Forms 
    (0xA840, 0xA87F, 'Phags-pa',                                4), # https://en.wikipedia.org/wiki/%27Phags-pa_script 
    (0xa880, 0xa8df, 'Saurashtra',                              2), # https://en.wikipedia.org/wiki/Saurashtra_alphabet
    (0xa8e0, 0xa8ff, 'Devanagari Extended',                     1), # maybe 2?
    (0xa900, 0xa92f, 'Kayah Li',                                2), # https://en.wikipedia.org/wiki/Kayah_Li_alphabet
    (0xa930, 0xa95f, 'Rejang',                                  2),
    (0xa960, 0xa97f, 'Hangul Jamo Extended-A',                  2), # https://en.wikipedia.org/wiki/Hangul_Jamo_Extended-A
    (0xa980, 0xa9df, 'Javanese',                                1), # ? https://en.wikipedia.org/wiki/Javanese_language
    (0xa9e0, 0xa9ff, 'Myanmar Extended-B',                      2),
    (0xaa00, 0xaa5f, 'Cham',                                    2), # https://en.wikipedia.org/wiki/Cham_languages 
    (0xaa60, 0xaa7f, 'Myanmar Extended-A',                      2),
    (0xaa80, 0xaadf, 'Tai Viet',                                2), # or 1?  https://en.wikipedia.org/wiki/Tai_Viet
    (0xaae0, 0xaaff, 'Meetei Mayek Extensions',                 4),
    (0xab00, 0xab2f, 'Ethiopic Extended-A',                     4),
    (0xab30, 0xab6f, 'Latin Extended-E',                        1),
    (0xab70, 0xabbf, 'Cherokee Supplement',                     2),
    (0xabc0, 0xabff, 'Meetei Mayek',                            4),
    (0xAC00, 0xD7AF, 'Hangul Syllables',                        1),
    (0xd7b0, 0xd7ff, 'Hangul Jamo Extended-B',                  2),

    (0xD800, 0xDB7F, 'High Surrogates',                        64),
    (0xDB80, 0xDBFF, 'High Private Use Surrogates',            64),
    (0xDC00, 0xDFFF, 'Low Surrogates',                         64),
    (0xE000, 0xF8FF, 'Private Use Area',                      128),
    (0xF900, 0xFAFF, 'CJK Compatibility Ideographs',            1),
    (0xFB00, 0xFB4F, 'Alphabetic Presentation Forms',           2), # may need another category?
    (0xFB50, 0xFDFF, 'Arabic Presentation Forms-A',             1),
    (0xFE00, 0xFE0F, 'Variation Selectors',                    32), # Most sensible ?
    (0xFE10, 0xFE1F, 'Vertical Forms',                          1),
    (0xFE20, 0xFE2F, 'Combining Half Marks',                   32),
    (0xFE30, 0xFE4F, 'CJK Compatibility Forms',                 1), # 32ish 1
    (0xFE50, 0xFE6F, 'Small Form Variants',                     1), 
    (0xFE70, 0xFEFF, 'Arabic Presentation Forms-B',             1), 
    (0xFF00, 0xFFEF, 'Halfwidth and Fullwidth Forms',           1), 
    (0xFFF0, 0xFFFF, 'Specials',                               64), 
    (0x10000, 0x1007F, 'Linear B Syllabary',                    4), 
    (0x10080, 0x100FF, 'Linear B Ideograms',                    4), 
    (0x10100, 0x1013F, 'Aegean Numbers',                        4), 
    (0x10140, 0x1018F, 'Ancient Greek Numbers',               2|4), # ?
    (0x10190, 0x101CF, 'Ancient Symbols',                       4), # (range got shortened in later unicode versions?)
    (0x101D0, 0x101FF, 'Phaistos Disc',                         4), 
    (0x10200, 0x1027F, '',                                    256), 
    (0x10280, 0x1029F, 'Lycian',                                4), # https://en.wikipedia.org/wiki/Lycian_language
    (0x102A0, 0x102DF, 'Carian',                                4), # https://en.wikipedia.org/wiki/Carian_language 
    (0x102E0, 0x102FF, 'Coptic Epact Numbers',                  4),
    (0x10300, 0x1032F, 'Old Italic',                            4), # https://en.wikipedia.org/wiki/Old_Italic_script
    (0x10330, 0x1034F, 'Gothic',                                2), # https://en.wikipedia.org/wiki/Gothic_alphabet
    (0x10350, 0x1037f, 'Old Permic',                            4), # https://en.wikipedia.org/wiki/Old_Permic_alphabet
    (0x10380, 0x1039F, 'Ugaritic',                              2), # https://en.wikipedia.org/wiki/Ugaritic_alphabet
    (0x103A0, 0x103DF, 'Old Persian',                           4), # https://en.wikipedia.org/wiki/Old_Persian_cuneiform
    (0x103e0, 0x103ff, '',                                    256),
    (0x10400, 0x1044F, 'Deseret',                               2), # https://en.wikipedia.org/wiki/Deseret_alphabet
    (0x10450, 0x1047F, 'Shavian',                               2), # https://en.wikipedia.org/wiki/Shavian_alphabet
    (0x10480, 0x104AF, 'Osmanya',                               4), # https://en.wikipedia.org/wiki/Osmanya_alphabet
    (0x104b0, 0x104ff, 'Osage',                                 1), # https://en.wikipedia.org/wiki/Osage_(Unicode_block)
    (0x10500, 0x1052f, 'Elbasan',                               4), # https://en.wikipedia.org/wiki/Elbasan_alphabet
    (0x10530, 0x1056F, 'Caucasian Albanian',                    4), # https://en.wikipedia.org/wiki/Caucasian_Albanian_alphabet
    (0x10570, 0x105ff, '',                                    256),
    (0x10600, 0x1077F, 'Linear A',                              4), # https://en.wikipedia.org/wiki/Linear_A_(Unicode_block)
    (0x10780, 0x107fF, '',                                    256),
    (0x10800, 0x1083F, 'Cypriot Syllabary',                     4), # https://en.wikipedia.org/wiki/Cypriot_syllabary
    (0x10840, 0x1085F, 'Imperial Aramaic',                      4), # https://en.wikipedia.org/wiki/Aramaic_alphabet
    (0x10860, 0x1087F, 'Palmyrene',                             4), # https://en.wikipedia.org/wiki/Palmyrene_dialect
    (0x10880, 0x108AF, 'Nabataean',                             4), # https://en.wikipedia.org/wiki/Nabataean_alphabet
    (0x108B0, 0x108df, '',                                    256),
    (0x108e0, 0x108ff, 'Hatran',                                4),
    (0x10900, 0x1091F, 'Phoenician',                            4), # https://en.wikipedia.org/wiki/Phoenician_alphabet
    (0x10920, 0x1093F, 'Lydian',                                4), # https://en.wikipedia.org/wiki/Lydian_alphabet
    (0x10940, 0x1097f, '',                                    256),
    (0x10980, 0x1099F, 'Meroitic Hieroglyphs',                  4), # https://en.wikipedia.org/wiki/Meroitic_alphabet 
    (0x109A0, 0x109ff, 'Meroitic Cursive',                      4), # https://en.wikipedia.org/wiki/Meroitic_alphabet 
    (0x10A00, 0x10A5F, 'Kharoshthi',                            4), # https://en.wikipedia.org/wiki/Kharosthi
    (0x10a60, 0x10a7f, 'Old South Arabian',                     4), # https://en.wikipedia.org/wiki/South_Arabian_alphabet
    (0x10a80, 0x10a9f, 'Old North Arabian',                     2), # https://en.wikipedia.org/wiki/Ancient_North_Arabian#Old_North_Arabian_script 
    (0x10AA0, 0x10abf, '',                                    256),
    (0x10AC0, 0x10aff, 'Manichaean',                            4), # https://en.wikipedia.org/wiki/Manichaean_(Unicode_block)
    (0x10B00, 0x10B3F, 'Avestan',                               4), # https://en.wikipedia.org/wiki/Avestan_(Unicode_block)
    (0x10B40, 0x10B5F, 'Inscriptional Parthian',                4), # https://en.wikipedia.org/wiki/Inscriptional_Parthian_(Unicode_block)
    (0x10B60, 0x10B7F, 'Inscriptional Pahlavi',                 4), # https://en.wikipedia.org/wiki/Inscriptional_Pahlavi_(Unicode_block)
    (0x10B80, 0x10BAF, 'Psalter Pahlavi',                       4), # https://en.wikipedia.org/wiki/Pahlavi_scripts#Psalter_Pahlavi
    (0x10bb0, 0x10bff, '',                                    256),
    (0x10C00, 0x10C4F, 'Old Turkic',                            4), # https://en.wikipedia.org/wiki/Old_Turkic_alphabet
    (0x10C50, 0x10c7f, '',                                    256),  
    (0x10C80, 0x10cff, 'Old Hungarian',                         4),
    (0x10d00, 0x10d3f, 'Hanifi Rohingya',                       2), # https://en.wikipedia.org/wiki/Hanifi_Rohingya_script
    (0x10d40, 0x10E5F, '',                                    256),
    (0x10E60, 0x10E7F, 'Rumi Numeral Symbols',                  4), # https://en.wikipedia.org/wiki/Rumi_Numeral_Symbols
    (0x10E80, 0x10eff, '',                                    256),
    (0x10f00, 0x10f2f, 'Old Sogdian',                           4), # https://en.wikipedia.org/wiki/Old_Sogdian_(Unicode_block)
    (0x10f30, 0x10f6f, 'Sogdian',                               4),
    (0x10f70, 0x10fdf, '',                                    256),
    (0x10fe0, 0x10fff, 'Elymaic',                               4), # https://en.wikipedia.org/wiki/Elymaic
    (0x11000, 0x1107F, 'Brahmi',                                4), # https://en.wikipedia.org/wiki/Brahmi_script
    (0x11080, 0x110CF, 'Kaithi',                                4), # https://en.wikipedia.org/wiki/Kaithi
    (0x110D0, 0x110FF, 'Sora Sompeng',                          2), # https://en.wikipedia.org/wiki/Sorang_Sompeng_alphabet
    (0x11100, 0x1114F, 'Chakma',                                2), # https://en.wikipedia.org/wiki/Chakma_alphabet
    (0x11150, 0x1117F, 'Mahajani',                              4), # https://en.wikipedia.org/wiki/Mahajani_(Unicode_block)
    (0x11180, 0x111DF, 'Sharada',                               2), # https://en.wikipedia.org/wiki/%C5%9A%C4%81rad%C4%81_script
    (0x111E0, 0x111FF, 'Sinhala Archaic Numbers',               4), # https://en.wikipedia.org/wiki/Sinhala_Archaic_Numbers
    (0x11200, 0x1124F, 'Khojki',                                4), # https://en.wikipedia.org/wiki/Khojki
    (0x11250, 0x1127F, '',                                    256),
    (0x11280, 0x112AF, 'Multani',                             256),
    (0x112B0, 0x112FF, 'Khudawadi',                             2), # https://en.wikipedia.org/wiki/Khudabadi_script
    (0x11300, 0x1137F, 'Grantha',                               4), # https://en.wikipedia.org/wiki/Grantha_alphabet
    (0x11380, 0x113ff, '',                                    256),
    (0x11400, 0x1147F, 'Newa',                                  2),
    (0x11480, 0x114DF, 'Tirhuta',                               2), # https://en.wikipedia.org/wiki/Tirhuta
    (0x114E0, 0x1157F, '',                                    256),
    (0x11580, 0x115FF, 'Siddham',                               4), # https://en.wikipedia.org/wiki/Siddha%E1%B9%83_alphabet
    (0x11600, 0x1165F, 'Modi',                                  2), # https://en.wikipedia.org/wiki/Modi_alphabet    
    (0x11660, 0x1167f, 'Mongolian Supplement',                  2),
    (0x11680, 0x116CF, 'Takri',                                 2), # https://en.wikipedia.org/wiki/Takri_alphabet
    (0x116D0, 0x116fF, '',                                    256),
    (0x11700, 0x1173f, 'Ahom',                                  4),
    (0x11740, 0x117FF, '',                                    256),    
    (0x11800, 0x1184F, 'Dogra',                                 2), # https://en.wikipedia.org/wiki/Dogras
    (0x11850, 0x1189F, '',                                    256),
    (0x118A0, 0x118FF, 'Warang Citi',                           2), # https://en.wikipedia.org/wiki/Varang_Kshiti
    (0x11900, 0x1199f, '',                                    256),
    (0x119A0, 0x119FF, 'Nandinagari',                           4), # https://en.wikipedia.org/wiki/Nandinagari
    (0x11a00, 0x11A4F, 'Zanabazar Square',                      4), # https://en.wikipedia.org/wiki/Zanabazar_Square_(Unicode_block)
    (0x11a50, 0x11AaF, 'Soyombo',                               4), # https://en.wikipedia.org/wiki/Soyombo_(Unicode_block)
    (0x11ab0, 0x11ABF, '',                                    256),
    (0x11AC0, 0x11AFF, 'Pau Cin Hau',                           2), # https://en.wikipedia.org/wiki/Pau_Cin_Hau
    (0x11B00, 0x11bff, '',                                    256),
    (0x11c00, 0x11c6f, 'Bhaiksuki',                             4), # https://en.wikipedia.org/wiki/Bhaiksuki_(Unicode_block)
    (0x11c70, 0x11cbf, 'Marchen',                               2), # https://en.wikipedia.org/wiki/Marchen_(Unicode_block)
    (0x11cc0, 0x11cff, '',                                    256),
    (0x11d00, 0x11d5f, 'Masaram Gondi',                         2), # https://en.wikipedia.org/wiki/Masaram_Gondi_(Unicode_block)
    (0x11d60, 0x11daf, 'Gunjala Gondi',                         2), # https://en.wikipedia.org/wiki/Gunjala_Gondi_script
    (0x11db0, 0x11EDF, '',                                    256), 
    (0x11ee0, 0x11eff, 'Makasar',                               4), # https://en.wikipedia.org/wiki/Makasar_script
    (0x11f00, 0x11FBF, '',                                    256),
    (0x11fc0, 0x11fff, 'Tamil Supplement',                      1),
    (0x12000, 0x123FF, 'Cuneiform',                             4), # https://en.wikipedia.org/wiki/Cuneiform
    (0x12400, 0x1247F, 'Cuneiform Numbers and Punctuation',     4), # https://en.wikipedia.org/wiki/Cuneiform_Numbers_and_Punctuation
    (0x12480, 0x1254f, 'Early Dynastic Cuneiform',              4),
    (0x12550, 0x12FFf, '',                                    256),
    (0x13000, 0x1342f, 'Egyptian Hieroglyphs',                  4), # https://en.wikipedia.org/wiki/Egyptian_hieroglyphs
    (0x13430, 0x1343f, 'Egyptian Hieroglyph Format Controls',   4),
    (0x13440, 0x143ff, '',                                    256),
    (0x14400, 0x1467f, 'Anatolian Hieroglyphs',                 4),
    (0x14680, 0x167FF, '',                                    256),
    (0x16800, 0x16a3f, 'Bamum Supplement',                      2), # https://en.wikipedia.org/wiki/Bamum_script
    (0x16a40, 0x16a6f, 'Mro',                                   1), # https://en.wikipedia.org/wiki/Mro_(Unicode_block)
    (0x16A70, 0x16ACF, '',                                    256),
    (0x16AD0, 0x16AFF, 'Bassa Vah',                             4), # https://en.wikipedia.org/wiki/Bassa_alphabet
    (0x16B00, 0x16B8F, 'Pahawh Hmong',                          2), # https://en.wikipedia.org/wiki/Pahawh_Hmong
    (0x16B90, 0x16E3f, '',                                    256),
    (0x16E40, 0x16e9f, 'Medefaidrin',                           2), # https://en.wikipedia.org/wiki/Medefaidrin
    (0x16EA0, 0x16EFF, '',                                    256),
    (0x16F00, 0x16F9F, 'Miao',                                  2), # https://en.wikipedia.org/wiki/Pollard_script
    (0x16FA0, 0x16fdf, '',                                    256),
    (0x16FE0, 0x16fff, 'Ideographic Symbols and Punctuation',   1),
    (0x17000, 0x187ff, 'Tangut',                                4),
    (0x18800, 0x18aff, 'Tangut Components',                     4),
    (0x18b00, 0x1afff, '',                                    256),
    (0x1B000, 0x1b0ff, 'Kana Supplement',                       2),
    (0x1B100, 0x1b12f, 'Kana Extended-A',                       2),
    (0x1B130, 0x1b16f, 'Small Kana Extension',                  1),
    (0x1B170, 0x1b2ff, 'Nushu',                                 2),
    (0x1B300, 0x1bbff, '',                                    256),
    (0x1BC00, 0x1bc9f, 'Duployan',                              2), # https://en.wikipedia.org/wiki/Duployan_shorthand
    (0x1BCA0, 0x1bcaf, 'Shorthand Format Controls',            64), # I think.
    (0x1BCB0, 0x1cfff, '',                                    256),
    (0x1D000, 0x1D0FF, 'Byzantine Musical Symbols',             4), # https://en.wikipedia.org/wiki/Byzantine_Musical_Symbols
    (0x1D100, 0x1D1FF, 'Musical Symbols',                      32), # https://en.wikipedia.org/wiki/Musical_Symbols_(Unicode_block)
    (0x1D200, 0x1D24F, 'Ancient Greek Musical Notation',        4), # https://en.wikipedia.org/wiki/Ancient_Greek_Musical_Notation
    (0x1d250, 0x1D2DF, '',                                    256),
    (0x1d2e0, 0x1d2ff, 'Mayan Numerals',                        4),
    (0x1D300, 0x1D35F, 'Tai Xuan Jing Symbols',                 4), # https://en.wikipedia.org/wiki/Taixuanjing 
    (0x1D360, 0x1D37F, 'Counting Rod Numerals',                 4), # https://en.wikipedia.org/wiki/Counting_rods
    (0x1d380, 0x1d3ff, '',                                    256),
    (0x1D400, 0x1D7FF, 'Mathematical Alphanumeric Symbols',    32),
    (0x1d800, 0x1daaf, 'Sutton SignWriting',                    1),
    (0x1dab0, 0x1DFFF, '',                                    256),
    (0x1e000, 0x1e02f, 'Glagolitic Supplement',                 4),
    (0x1e030, 0x1E0FF, '',                                    256),
    (0x1e100, 0x1E14f, 'Nyiakeng Puachue Hmong',                2),
    (0x1E150, 0x1E2BF, '',                                    256),    
    (0x1e2c0, 0x1E2ff, 'Wancho',                                2),
    (0x1E300, 0x1E7ff, '',                                    256),    
    (0x1e800, 0x1E8DF, 'Mende Kikakui',                         1),
    (0x1e8e0, 0x1e8ff, '',                                    256),
    (0x1e900, 0x1e95f, 'Adlam',                                 1), # https://en.wikipedia.org/wiki/Adlam_(Unicode_block)
    (0x1e960, 0x1EC6F, '',                                    256),
    (0x1ec70, 0x1Ecbf, 'Indic Siyaq Numbers',                   4),
    (0x1ECC0, 0x1ECFF, '',                                    256),
    (0x1ed00, 0x1ed4f, 'Ottoman Siyaq Numbers',                 4),
    (0x1ED50, 0x1EDFF, '',                                    256),
    (0x1ee00, 0x1eeff, 'Arabic Mathematical Alphabetic Symbols',2), # https://en.wikipedia.org/wiki/Mathematical_Alphanumeric_Symbols
    (0x1ef00, 0x1EFFF, '',                                    256),
    (0x1F000, 0x1F02F, 'Mahjong Tiles',                        32),
    (0x1F030, 0x1F09F, 'Domino Tiles',                         32),
    (0x1f0a0, 0x1f0ff, 'Playing Cards',                        32),
    (0x1F100, 0x1F1FF, 'Enclosed Alphanumeric Supplement',      1), # I guess...
    (0x1F200, 0x1F2FF, 'Enclosed Ideographic Supplement',       1), # I guess...
    (0x1F300, 0x1F5FF, 'Miscellaneous Symbols and Pictographs',32),
    (0x1F600, 0x1F64f, 'Emoticons',                            32),
    (0x1F650, 0x1F67F, 'Ornamental Dingbats',                  32),
    (0x1F680, 0x1F6FF, 'Transport and Map Symbols',            32),
    (0x1F700, 0x1F77F, 'Alchemical Symbols',                   32),
    (0x1F780, 0x1F7FF, 'Geometric Shapes Extended',            32),
    (0x1F800, 0x1F8FF, 'Supplemental Arrows-C',                32),
    (0x1f900, 0x1f9ff, 'Supplemental Symbols and Pictographs', 32),
    (0x1fa00, 0x1fa6f, 'Chess Symbols',                        32),
    (0x1FA70, 0x1faff, 'Symbols and Pictographs Extended-A',   32),
    (0x1FB00, 0x1ffff, '',                                    256),
    
    # https://en.wikipedia.org/wiki/CJK_Unified_Ideographs
    (0x20000, 0x2A6DF, 'CJK Unified Ideographs Extension B',      2),
    (0x2A6E0, 0x2A6FF, '',                                      256),
    (0x2A700, 0x2B73F, 'CJK Unified Ideographs Extension C',      2),
    (0x2B740, 0x2B81f, 'CJK Unified Ideographs Extension D',      2), 
    (0x2B820, 0x2CEAF, 'CJK Unified Ideographs Extension E',      2), 
    (0x2CEB0, 0x2EBEF, 'CJK Unified Ideographs Extension F',      2), 
    (0x2EBF0, 0x2f7ff, '',                                      256),
    (0x2F800, 0x2FA1F, 'CJK Compatibility Ideographs Supplement', 1),
    (0x2fa20, 0x2ffff, '',                                      256),
    
    
    # As of this this writing, this seems to be planned, not current
    #(0x30000,0x3291f, 'Small Seal Script (tentative allocation)', 4), # CHECK
    #(0x32920,0x329FF, '',                                       256),
    #(0x32a00,0x341ff, 'Oracle Bone Script (tentative allocation)',4),
    #(0x34200,0x3ffff, '',                                       256),
    # Bronze Script ?
    # The Warring States scripts ?
    
    # unallocated planes
    (0x30000,0x3ffff, 'plane 3 (not allocated)',                256),
    (0x40000,0x4ffff, 'plane 4 (not allocated)',                256),
    (0x50000,0x5ffff, 'plane 5 (not allocated)',                256),
    (0x60000,0x6ffff, 'plane 6 (not allocated)',                256),
    (0x70000,0x7ffff, 'plane 7 (not allocated)',                256),
    (0x80000,0x8ffff, 'plane 8 (not allocated)',                256),
    (0x90000,0x9ffff, 'plane 9 (not allocated)',                256),
    (0xA0000,0xAffff, 'plane 10 (not allocated)',               256),
    (0xB0000,0xBffff, 'plane 11 (not allocated)',               256),
    (0xC0000,0xCffff, 'plane 12 (not allocated)',               256),
    (0xD0000,0xDffff, 'plane 13 (not allocated)',               256),
    
    # Supplemental Special-purpose Plane
    (0xE0000, 0xE007F, 'Tags',                                   32), # http://www.unicode.org/faq/languagetagging.html
    (0xe0080,0xe00ff, '',                                       256),
    (0xE0100, 0xE01EF, 'Variation Selectors Supplement',         32),
    (0xe01f0,0xeffff, '',                                       256),
    
    (0xF0000,  0xFFFFF,  'Supplementary Private Use Area-A',    128),
    
    (0x100000, 0x10FFFF, 'Supplementary Private Use Area-B',    128),
]




def block_for_char(c):
   ''' Get the range and name of the block the given character is in.
       Returns (start,end,name)
               (0,0,Nonw) if not in a known block
   '''
   if type(c)==int:
      pass
   elif type(c)==str or type(c)==unicode:
      #if len(c)>1:
      #    return (0,0,None)
      c=ord(c)
      
   for start,end,name,_ in blocks:
      if c >= start and c <= end:
         return (start,end,name)
     
   return (0,0,None)



# rarely used, so we generate on first use
# meant to support font suggestion
block_chars = {}
def chars_in_block(blockname):
    global block_chars
    import unicodedata
    if len(block_chars) == 0:
        block_chars = {}
        for genblockstart,genblockend,genblockname,_ in blocks:
            block_chars[genblockname] = []
            for chi in range(genblockstart, genblockend+1):
                try:
                    unicodedata.name( unichr(chi) )   # test for whether it exists.  TODO: fix this test and ones like it
                    block_chars[genblockname].append( chi )
                except ValueError as e:
                    pass
                
    return block_chars[blockname]



# This should be regenerated, based on code yet to be (re)written.
# valid_chars_per_blockname = {'Combining Diacritical Marks Extended': 0, 'Tai Xuan Jing Symbols': 87, 'Thaana': 50, 'Arabic Mathematical Alphabetic Symbols': 0,

