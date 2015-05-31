# -*- coding: utf-8 -*-

import unittest
import re
from query import *

def squeeze(value):
    value = value.replace('\r', '')
    value = value.replace('\n', '')
    return value

class QueryTestCase(unittest.TestCase):

    def test_parse_names(self):
        self.assertEqual(None, parse_names(u''))
        self.assertEqual(None, parse_names(u' '))
        self.assertEqual(None, parse_names(u'\t'))
        self.assertEqual(None, parse_names(u'\r'))
        self.assertEqual(None, parse_names(u'\n'))
        self.assertEqual(None, parse_names(u'a'))
        self.assertEqual(None, parse_names(u' a'))
        self.assertEqual(None, parse_names(u' a\t'))
        self.assertEqual(None, parse_names(u' a\t '))
        self.assertEqual((u'a', u'b'), parse_names(u' a b'))
        self.assertEqual((u'a', u'b'), parse_names(u' a b '))
        self.assertEqual((u'a', u'b'), parse_names(u' a　b '))
        self.assertEqual(None, parse_names(u' a b c'))

    def test_do(self):
        self.maxDiff = None

        xml = re.sub(ur'>\s*<', u'><', do(u''))
        self.assertEqual(u'<?xml version="1.0"?><items><item uid="result" arg="" valid="no"><title>type “from” and “to” station names</title></item></items>', xml)

        xml = re.sub(ur'>\s*<', u'><', do(u' a '))
        self.assertEqual(u'<?xml version="1.0"?><items><item uid="result" arg="" valid="no"><title>type “from” and “to” station names</title></item></items>', xml)

        xml = re.sub(ur'>\s*<', u'><', do(u' a b '))
        self.assertEqual(u'<?xml version="1.0"?><items><item uid="result" arg="http://transit.loco.yahoo.co.jp/search/result?from=a&amp;to=b" valid="yes"><title>Query routes from a to b</title></item></items>', xml)

if __name__ == '__main__':
    unittest.main()
