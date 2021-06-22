import html

def nodetext(s):
    ''' Escapes for HTML/XML text nodes:
        Replaces <, >, and & with entities
        Leaves unicode be.
        (is actually cgi.escape)
    '''
    return html.escape(s)

def attr(s):#,numeric=True, apos=True):
    ''' Escapes for use in HTML(/XML) node attributes:
        Escapes <, >, &, ', "

        ' and " to numeric entitities (&#x27;, &#x22;) by default

        Escapes ' (which cgi.escape doesn't) which you usually don't need,
        but do if you wrap attributes in ' which is valid in XML, various HTML. Numeric only, because
        Doesn't use apos becase it's not defined in HTML4


        Passes non-ascii through. It is expected that you want to apply that to the document as a whole, or to document writing/appending.

        Note that to put URIs with unicode in attributes, what you want is often something roughly like
        '<a href="?q=%s">'%attr( uri_component(q)  )
        because uri handles the utf8 percent escaping of the unicode, attr() the attribute escaping
        (technically you can get away without attr because uri_component escapes a _lot_ )
    '''
    #if numeric:
    ret = html.escape(s).replace('"','&#x22;')
    #else: # defined in HTML 3.2, HTML 2, HTML 4 and XHTML 1.0, XML 1.0
    #    cgi.escape(s).replace('"','&quot;')
    #if apos:
    ret = ret.replace("'",'&#x27;')
    return ret


