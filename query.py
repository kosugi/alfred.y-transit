# -*- coding: utf-8 -*-
#
# launch “Y!J Transit” with two station names (from, to).
#
# query MUST be escaped double quotation marks and backslashes.
#

import re
import sys
import codecs
from xml.sax.saxutils import escape
from urllib2 import quote

alt_escape_rule = {u'"': u'&quot;', u"'": u'&#39;'}
def h(value):
    return escape(value, alt_escape_rule)

def u(value):
    return quote(value.encode('UTF-8'))

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
    q = sys.argv[1].decode('UTF-8') if 1 < len(sys.argv) else u"""{query}"""
    m = re.match(ur'''\A\s*(\S+?)\s+(.+?)\s*\Z''', q)
    if m:
        src, dst = m.groups()
        url = '''http://transit.loco.yahoo.co.jp/search/result?from={src}&to={dst}'''.format(src=u(src), dst=u(dst))
        print u'''<?xml version="1.0"?>
<items>
  <item uid="result" arg="{url}" valid="yes">
    <title>Query routes from {f} to {t}</title>
  </item>
</items>'''.format(q=h(q), f=h(src), t=h(dst), url=h(url))
    else:
        print u'''<?xml version="1.0"?>
<items>
  <item uid="result" valid="no">
    <title>type “from” and “to” station names</title>
  </item>
</items>'''
