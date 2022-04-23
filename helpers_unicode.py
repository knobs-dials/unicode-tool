''' Most of these functions work on integer lists,
    which is not how python in general works
    but is convenient for this specific tool.

    TODO: remove all uses of unicodedata
'''
# See also  helpers_string.remove_diacritics()


import unicodedata
import re
from typing import List


planenames = {
     0x0000:'BMP - Basic Multilingual Plane',
    0x10000:'SMP - Supplemental Multilingual Plane',
    0x20000:'SIP - Supplemental Ideographic Plane',
    0x30000:'TIP - Tertiary Ideographic Plane (plane 3, tentatively allocated)',
    0x40000:'Planes 4 through 13 - not allocated',
   #0x50000:'Plane 5 - not allocated',
   #0x60000:'Plane 6 - not allocated',
   #0x70000:'Plane 7 - not allocated',
   #0x80000:'Plane 8 - not allocated',
   #0x90000:'Plane 9 - not allocated',
   #0xA0000:'Plane 10 - not allocated',
   #0xB0000:'Plane 11 - not allocated',
   #0xC0000:'Plane 12 - not allocated',
   #0xD0000:'Plane 13 - not allocated',
    0xE0000:'SSP - Supplemental Special-purpose Plane',
    0xF0000:'PUA-A - Private Use Area A',
   0x100000:'PUA-B - Private Use Area B',
}


# nicer names for unicode categories

bids = {
     'L':'Left-to-Right',
   'LRE':'Left-to-Right Embedding',
   'LRO':'Left-to-Right Override',
     'R':'Right-to-Left',
    'AL':'Right-to-Left Arabic',
   'RLE':'Right-to-Left Embedding',
   'RLO':'Right-to-Left Override',
   'PDF':'Pop Directional Format',
    'EN':'European Number',
    'ES':'European Number Separator',
    'ET':'European Number Terminator',
    'AN':'Arabic Number',
    'CS':'Common Number Separator',
   'NSM':'nonspacing mark',
    'BN':'Boundary Neutral',
     'B':'Paragraph Separator',
     'S':'Segment Separator',
    'WS':'Whitespace',
    'ON':'Other Neutrals',
}

cats = {
   'Lu':'uppercase letter',
   'Ll':'lowercase letter',
   'Lt':'titlecase letter',
   'Lm':'modifier letter',
   'Lo':'other letter',
   'Mn':'nonspacing mark',
   'Mc':'spacing combining mark',
   'Me':'enclosing mark',
   'Nd':'number: decimal digit',
   'Nl':'number: letter',
   'No':'number: other',
   'Pc':'punctuation: connector',
   'Pd':'punctuation: dash',
   'Ps':'punctuation: open',
   'Pe':'punctuation: close',
   'Pi':'punctuation: initial quote (may behave like Ps or Pe depending on usage)',
   'Pf':'punctuation; final quote (may behave like Ps or Pe depending on usage)',
   'Po':'punctuation:Other',
   'Sm':'math symbol',
   'Sc':'currency symbol',
   'Sk':'modifier symbol',
   'So':'other symbol',
   'Zs':'space separator',
   'Zl':'line separator',
   'Zp':'paragraph separator',
   'Cc':'control character',
   'Cf':'format character',
   'Cs':'surrogate codepoint',
   'Co':'private use character',
   'Cn':'(character not assigned)'
}
    

 

def simpler_category_description(ch:int, a_an=True):
    ''' EXPERIMENT: simpler variant of the more official categories, more of a "can dump this in a description without thinking" thing '''
    simpler_bids = {
        #'L':'',
        #'LRE':'',
        #'LRO':'',
        'R':'Right-to-Left',
        'AL':'Right-to-Left (Arabic)',
        'RLE':'Right-to-Left',
        'RLO':'Right-to-Left',
        #'PDF':'',
        #'EN':'',
        #'ES':'',
        #'ET':'',
        'AN':'Arabic', # the following will probably add 'decimal digit' or such
        #'CS':'',
        #'NSM':'',
        #'BN':'',
        #'B':'',
        #'S':'',
        'WS':'whitespace',
        #'ON':'',
    }

    simpler_cats = { 
        'Lu':'uppercase letter',
        'Ll':'lowercase letter',
        'Lt':'titlecase letter',
        'Lm':'modifier letter',
        'Lo':'letter',
        'Mn':'nonspacing mark',
        'Mc':'spacing combining mark',
        'Me':'enclosing mark',
        'Nd':'decimal digit',
        'Nl':'letter-style number',
        'No':'number: other',
        'Pc':'punctuation',
        'Pd':'punctuation',
        'Ps':'punctuation',
        'Pe':'punctuation',
        'Pi':'punctuation',
        'Pf':'punctuation',
        'Po':'punctuation',
        'Sm':'math symbol',
        'Sc':'currency symbol',
        'Sk':'modifier symbol',
        'So':'symbol',
        'Zs':'space separator',
        'Zl':'line separator',
        'Zp':'paragraph separator',
        'Cc':'control character',
        'Cf':'format character',
        'Cs':'surrogate codepoint',
        'Co':'private use character',
        #'Cn':'(character not assigned)'
    }

    ret = []

    bidir_cat  = unicodedata.bidirectional( chr(ch) )
    gen_cat    = unicodedata.category( chr(ch) )

    if gen_cat=='Cn':
        return 'not an assigned character'
    else:
        if bidir_cat in simpler_bids:
            ret.append( simpler_bids[bidir_cat] )
        if gen_cat in simpler_cats:
            ret.append( simpler_cats[gen_cat] )

    if a_an and len(ret)>0:
        if len( ret[0] ) >0:
            if ret[0][0].lower() in 'aeiou':
                ret[0] = 'an %s'%ret[0]
            else:
                ret[0] = 'a %s'%ret[0]

    return ' '.join(ret)



def codepoint_assigned(cp: int):
    # note that this does _not_ imply it has a name
    return ('Cn' not in unicodedata.category( chr(cp) )) #filter out unassigneds


def character_name(ch: str):
    ''' unicodedata.name(), but doesn't throw an exception on cases that are considered assigned, but do not have a name. 

        In Unicode 12 these are:
          0000..001F    control codes
          007F..009F    control codes
          D800..F8FF    Surrogates and private use
         17000..187F7   Tangut, seems to be preliminary assignment settled in 13?
         F0000..FFFFD   private use
        100000..10FFFD  private use
    '''
    cp = ord(ch)

    if cp >= 0x00  and  cp <= 0x1f:
        return '(control codes have no character names)'
    elif cp >= 0x7f  and  cp <= 0x9f:
        return '(control codes have no character names)'    
    elif cp >= 0xd800  and  cp <= 0xdb7f:
        return '(high surrogates have no character names)'
    elif cp >= 0xdb80  and  cp <= 0xdbff:
        return '(private use surrogates have no character names)'
    elif cp >= 0xdc00  and  cp <= 0xdfff:
        return '(low surrogates have no character names)'
    elif cp >= 0xe000  and  cp <= 0xf8ff:
        return '(private use areas have no character names)'
    elif cp >= 0xf0000  and  cp <= 0xFFFFD:
        return '(private use areas have no character names)'
    elif cp >= 0x100000  and  cp <= 0x10FFFD:
        return '(private use areas have no character names)'
    #elif cp >= 0x17000  and  cp <= 0x187F7:   # Tangut, seems to be 
    #    return '()'    
    try:
        #if 0:
        #    curs = conn.cursor()
        #    curs.execute('select name from cpbasics where codepoint=%s', ( cp, ))
        #    conn.rollback()
        #else:
        return unicodedata.name( ch )
    except: # 
        return '(name not known)'
      


def is_privateuse(cp: int):
    # arguably 0xdb80..0xdbff as well
    if cp>=0xE000 and cp<=0xF8FF:
        return True
    if cp>=0xF0000 and cp<=0xFFFFF:
        return True
    if cp>=0x100000 and cp<=0x10FFFD:
        return True
    return False

def has_privateuse(s: str):
    for char in s:
        if is_privateuse( ord(char) ):
            return True
    return False


def is_surrogate(cp: int):
    if cp>=0xD800 and cp<=0xDBFF: # High Surrogate Area
        return True
    #if cp>=0xDB80 and cp<=0xDBFF: # High Private Use Surrogates 
    #    return True
    if cp>=0xDC00 and cp<=0xDFFF: # Low Surrogate Area
        return True    
    return False


def is_utf16_with_surrogates(cp_list):
    ' if max codepoint is <=U+FFFF and there is at least one codepoint in the surrogate range '
    if len(cp_list)>0:
        if max(cp_list) <= 0xffff:
            has_surrogates = False
            for cp in cp_list:
                if is_surrogate(cp):
                    return True
    return False

def remove_lone_surrogates(cp_list):
    ' written more for readability (ish) than brevity or efficiency '
    # a surrogate pair is a high surrogte (d800..dbff) followed by a low surrogate (dc00..dfff)    TODO: double check I don't have that backards
    def high_surrogate(cp):
        return (cp>=0xd800 and cp<=0xdbff)
    def low_surrogate(cp):
        return (cp>=0xdc00 and cp<=0xdfff)
    ret=[]
    ll = len(cp_list)
    for i in range(ll):
        add_cp = True
        # remove high surrogate not followed by a low surrogate
        if high_surrogate(cp_list[i]):
            if i==ll-1: # end of string
                add_cp = False
            if i<ll-2 and not low_surrogate(cp_list[i+1]): # 
                add_cp = False
        # remove low surrogate not preceded by a high surrogate
        if low_surrogate(cp_list[i]):
            if i==0:
                add_cp = False
            if i>=1 and not high_surrogate(cp_list[i-1]):
                add_cp = False

        if add_cp:
            ret.append(cp_list[i])
    return ret
    # string form is easier:
    #bad_surrogates = re.compile( r'([\ud800-\udbff](?![\udc00-\udfff]))|((?<![\ud800-\udbff])[\udc00-\udfff])')
    #qs2 = bad_surrogates.sub('\ufffd', qs)


def interpret_any_surrogates(cp_list):
    ' may throw a UnicodeDecodeError e.g. on lone surrogates '
    ret_cp = [] 
    if is_utf16_with_surrogates(cp_list):
        ustr = ''.join(  chr(cp)  for cp in cp_list  )
        ustr = ustr.encode('utf-16-le','surrogatepass').decode('utf-16-le') # slight trickery
        for char in ustr:
            ret_cp.append( ord(char) )
        return ret_cp
    else:
        return cp_list



def is_controlcode(cp: int):
    if cp >= 0 and cp<=0x19:
        return True
    if cp >= 0x7f and cp<=0x9f:
        return True
    return False

def has_controlcode(s: str):
    for ch in s:
        if is_controlcode( ord(ch) ):
            return True
    return False



def is_variationselector(cp: int):
    return (cp >= 0xFE00  and  cp <= 0xFE0F)




def is_emoji(cp: int):
    ''' In trying to implement this I noticed even unicode is vague on what emoji are. 
        I need to rethink this.
    '''
    import unicode_emoji
    for frm, to in unicode_emoji.ranges:
        if cp >= frm and cp <= to:
            return True
    return False

def has_emoji(s: str):
    for s1 in s:
        if is_emoji( ord(s1) ):
            return True
    return False




def is_cjk(cp: int):
    ''' whether a character (len-1 string  or  int) is CJK
 
        (test is a bit wide now, more like 'asian script' - TODO: make more precise
    '''
    if cp>0x2e80 and cp<0xA4CF:  # bunch of blocks, not all relevant
        return True
    if cp>0xf900 and cp<0xfaff:  # CJK Compatibility Ideographs
        return True
    if cp>0xFE30 and cp<0xFE4F:  # Vertical Forms
        return True
    if cp>0xff00 and cp<0xfeff:  # Halfwidth and Fullwidth Forms
        return True
    if cp>0x20000 and cp<0x2ffff: # SIP. includes 33k of unallocateds, but hey...
        return True
    return False


def has_cjk(s: str):
    ''' whether a string contains CJK haracters '''
    for cp in s:
        if is_cjk( ord(cp) ):
            return True
    return False



# the -non versions are there because it's slightly easier to remove characters (using re.sub) than it is to get a string of just matching chars (via re.search/findall)


# for significant_cjk, to omit various spaces from the test
reSpace           = re.compile(r'\u0020\u00a0\u1680\u180e\u2000-\u2009\u200a\u202f\u205f\u3000')

# actually encompasses many asian scripts (but doesn't include those in the SMP); CONSIDER splitting out
reCJK             = re.compile( r'[\u2E80-\uA640\ua6a0-\uA71F\uA800-\ud7ff\uF900-\uFAFF\uFE30-\uFE4F\uFF61-\uFFDC\u20000-\u2FA1F\u30000–\u3134F]' )
reNonCJK          = re.compile( r'[^\u2E80-\uA640\ua6a0-\uA71F\uA800-\ud7ff\uF900-\uFAFF\uFE30-\uFE4F\uFF61-\uFFDC\u20000-\u2FA1F\u30000–\u3134F]' )
reNonJapaneseKana = re.compile( r'[^\u3040-\u30FF\uFF65-\uFF9F]' )
reNonKorean       = re.compile( r'[^\u1100-\u11FF\uAC00-\uD7AF\uFFA0-\uFFDC]' ) # all/mostly hangul? (VERIFY)

def significant_cjk(s: str, thresh=0.2):
    """ Sees if a string has at least some given fraction of CJK characters.

        Assumes it is if more than a certain fraction (controlled by thresh) are CJK characters.
        Also tries to guess which, returning one of chinese ('zh'), japanese ('ja'), korean ('ko'), or unknown ('xx')
        
        Won't respond accurately to certain mixes (e.g. japanese+korean), but that's unlikely anyway.
        Note that this is not a complete solution for language detection, as you want to deal with transliterations too.
        
        However, it does allow you to handle logographic systems separately, to e.g. avoid n-gram explosion.
        
        Returns a 2-tuple:
        * whether some portion of the printable characters are CJK
        * 'cn', 'ja', 'ko',  or 'xx' if it doesn't know or there is no CJK in there

        TODO: test
    """
    spaceless     = reSpace.sub( '', s )
    spaceless_len = len( spaceless )
    just_cjk      = reNonCJK.sub( '', spaceless )
    just_cjk_len  = len( just_cjk )

    is_cjk = False
    if float(just_cjk_len) > thresh*spaceless_len:
        is_cjk=True

    guess_which = 'xx'
    if is_cjk:
        just_kana = reNonJapaneseKana.sub('',just_cjk)
        if len(just_kana)>10 or len(just_kana)>0.1*just_cjk_len:
            guess_which = 'ja'
        else:
            just_hangul = reNonKorean.sub('',just_cjk)
            if len(just_hangul)>10 or len(just_hangul)>0.1*just_cjk_len:
                guess_which = 'ko'
            else: # fall back to assume chinese. Stop ding this if I ever make it wider than CJK
                guess_which = 'cn'
    return (is_cjk, guess_which)




# do we use this or was this from another project?
def remove_nonprintable(s: str, keep1=('L','S','N','M','P','Zs'), keep2=('Zs',)):
    ''' Keeps only certain types of characters, intended to keep just the ones we can show:

        By default keeps
         - L  (letters)
         - S  (symbols)
         - N  (numbers)
         - M  (marks)
         - P  (punctuation)
         - Zs (spaces)
        so by implciation removes
         - C (control, format, surrogate, private, unassigned)
         - Z (separators) other than Zs (space separators)

        TODO: rewrite to use database data instead of unicodedata (right now it's current with us -- python3 uses 12.1.0 -- but eventually this will not be correct)
    '''
    ret=[]
    if type(s) is not unicode:
        try:
            s=unicode(s)
        except:
            s=s.decode('utf8')
    for c in s:
       tcats    = unicodedata.category( c )
       if tcats in keep2 or tcats[0] in keep1: 
           ret.append(c)
    return ''.join(ret)




