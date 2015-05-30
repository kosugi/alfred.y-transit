# -*- coding: utf-8 -*-
from lxml import etree
from os.path import dirname, realpath
import sys
import codecs

def xpath_for_uid(uid):
    return ''.join((
        "/plist",
        "/dict",
        "/key[text()='objects']",
        "/following-sibling::array[1]",
        "/dict",
        "/key[text()='uid']"
        "/following-sibling::string[1][text()='%s']",
        "/..",
        "/key[text()='config']",
        "/following-sibling::dict[1]",
        "/key[text()='script']",
        "/following-sibling::string[1]",
    )) % uid # !! not to be escaped !!

def replace_node(xml, uid, path):
    with codecs.getreader('UTF-8')(open(path)) as f:
        src = f.read()
    node = xml.xpath(xpath_for_uid(uid))[0]
    node.text = src

BASE = realpath(dirname(sys.argv[0]))
xml = etree.parse(BASE + '/info.plist')
replace_node(xml, '8F215229-267A-45B4-8552-063B94BBC676', BASE + '/query.py')

with codecs.getwriter('UTF-8')(open(BASE + '/build/info.plist', 'w')) as f:
    f.write(etree.tostring(xml))
