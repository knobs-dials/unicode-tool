import unicodedata
import re

# TODO: remove all uses of unicodedata


# See also  helpers_string.remove_diacritics()



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



def codepoint_assigned(cp):
    # note that this does _not_ imply it has a name
    return ('Cn' not in unicodedata.category( chr(cp) )) #filter out unassigneds

def character_name(ch):
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
        return unicodedata.name( ch )
    except: # 
        return '(name not known)'
      


def is_private_use(cp):
    # arguably 0xdb80..0xdbff as well
    if cp>=0xE000 and cp<=0xF8FF:
        return True
    if cp>=0xF0000 and cp<=0xFFFFF:
        return True
    if cp>=0x100000 and cp<=0x10FFFD:
        return True
    return False

def has_private_use(s):
    for s1 in s:
        if is_privateuse( ord(s1) ):
            return True
    return False


def is_surrogate(cp):
    if cp>=0xD800 and cp<=0xDBFF: # High Surrogate Area
        return True
    if cp>=0xDC00 and cp<=0xDFFF: # Low Surrogate Area
        return True    
    if cp>=0xDB80 and cp<=DBFF:   # High Private Use Surrogates 
        return True
    return False



def is_controlcode(cp):
    if cp >= 0 and cp<=0x19:
        return True
    if cp >= 0x7f and cp<=0x9f:
        return True
    return False

def has_controlcode(s):
    for ch in s:
        if is_controlcode( ord(ch) ):
            return True
    return False




def is_variationselector(cp):
    return (cp >= 0xFE00  and  cp <= 0xFE0F)



def is_emoji(cp):
    # WTF what ever are emoji?
    import unicode_emoji
    for frm, to in unicode_emoji.ranges:
        if cp >= frm and cp <= to:
            return True
    return False

def has_emoji(s):
    for s1 in s:
        if is_emoji( ord(s1) ):
            return True
    return False




def is_cjk(i):
    ''' whether a character (len-1 string  or  int) is CJK
 
        (test is a bit wide now, more like 'asian script' - TODO: make more precise
    '''
    #if type(i) is str:
    #    if len(i)==1:
    #        i=ord(i)
    #    else:
    #        raise ValueError('Expected an integer or length-one string')
    #elif type(i) not in (int,long):
    #    raise ValueError('Expected an integer or length-one string') 
    if i>0x2e80 and i<0xA4CF:  # bunch of blocks, not all relevant
        return True
    if i>0xf900 and i<0xfaff:  # CJK Compatibility Ideographs
        return True
    if i>0xFE30 and i<0xFE4F:  # Vertical Forms
        return True
    if i>0xff00 and i<0xfeff:  # Halfwidth and Fullwidth Forms
        return True
    if i>0x20000 and i<0x2ffff: # SIP. includes 33k of unallocateds, but hey...
        return True
    return False


def has_cjk(s):
    ''' whether a string contains CJK haracters '''
    for cp in s:
        if is_cjk( ord(cp) ):
            return True
    return False



# TODO: review and simplify:

# actually encompasses many asian scripts (but doesn't include those in the SMP); CONSIDER splitting out
reCJK             = re.compile(  r'[\u2E80-\uA640\ua6a0-\uA71F\uA800-\ud7ff\uF900-\uFAFF\uFE30-\uFE4F\uFF61-\uFFDC\u20000-\u2FA1F\u30000–\u3134F]' )
reNonCJK          = re.compile( r'[^\u2E80-\uA640\ua6a0-\uA71F\uA800-\ud7ff\uF900-\uFAFF\uFE30-\uFE4F\uFF61-\uFFDC\u20000-\u2FA1F\u30000–\u3134F]' )

reSqueezeSpace    = re.compile('[\ ]+')

# TODO: test the next function

reSpace           = re.compile(r'\u0020\u00a0\u1680\u180e\u2000-\u2009\u200a\u202f\u205f\u3000')
reNonJapaneseKana = re.compile(r'[^\u3040-\u30FF\uFF65-\uFF9F]')
reNonKorean       = re.compile(r'[^\u1100-\u11FF\uAC00-\uD7AF\uFFA0-\uFFDC]')

def significant_cjk(s, thresh=0.2):
    """ Sees if a string has at least some given fraction of CJK characters.

        Assumes it is if more than a certain fraction (controlled by thresh) are CJK characters.
        Also tries to guess which, returning one of chinese ('zh'), japanese ('ja'), korean ('ko'), or unknown ('xx')
        
        Won't respond accurately to certain mixes (e.g. japanese+korean), but that's unlikely anyway.
        Note that this is not a complete solution for language detection, as you want to deal with transliterations too.
        
        However, it does allow you to handle logographic systems separately, to e.g. avoid n-gram explosion.
        
        Returns a 2-tuple:
        * whether some portion of the printable characters are CJK
        * if true, which it seems to be (if not, returns 'unknown')

    """
    spaceless     = reSpace.sub('',s)
    spaceless_len = len(spaceless)
    just_cjk      = reNonCJK.sub('',spaceless)
    just_cjk_len  = len(just_cjk)

    is_cjk = False
    if float(just_cjk_len) > thresh*spaceless_len:
        is_cjk=True
        #print "CJK"

    guess_which = 'xx'
    if is_cjk:
        just_kana = reNonJapaneseKana.sub('',just_cjk)

        #print len(just_kana)
        #print just_cjk_len
        if len(just_kana)>10 or len(just_kana)>0.1*just_cjk_len:
            guess_which = 'ja'
        else:
            just_hangul = reNonKorean.sub('',just_cjk)
            #print len(just_hangul)
            if len(just_hangul)>10 or len(just_hangul)>0.1*just_cjk_len:
                guess_which = 'ko'
            else:
                guess_which = 'zh'
            
    return (is_cjk,guess_which)




def remove_nonprintable(s, keep1=('L','S','N','M','P','Zs'), keep2=('Zs',)):
    ''' Keeps only certain types of characters, intended to keep just the ones we can show:

        TODO: rewrite to use database data instead of unicodedata (right now it's current with us -- python3 uses 12.1.0 -- but eventually this will not be correct)

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
