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

def parse_names(q):
    m = re.match(ur'''\A\s*(\S+?)\s+(\S+)\s*\Z''', q.replace(u'　', u' '))
    if m:
        return m.groups()

def build_url(src, dest):
    return u'''http://transit.loco.yahoo.co.jp/search/result?from={src}&to={dest}'''.format(src=u(src), dest=u(dest))

def build_xml(validity, url, title):
    valid = ('no', 'yes')[bool(validity)]
    return u'''<?xml version="1.0"?>
<items>
  <item uid="result" arg="{url}" valid="{valid}">
    <title>{title}</title>
  </item>
</items>'''.format(title=h(title), url=h(url), valid=h(valid))

def do(q):
    names = parse_names(q)
    if names:
        src, dest = names
        url = build_url(src, dest)
        return build_xml(True, url, u'Query routes from {src} to {dest}'.format(src=src, dest=dest))
    else:
        return build_xml(False, '', u'type “from” and “to” station names')

if __name__ == '__main__':
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)
    q = sys.argv[1].decode('UTF-8') if 1 < len(sys.argv) else u"""{query}"""
    print do(q)
