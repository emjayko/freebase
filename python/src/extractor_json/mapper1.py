#!/usr/bin/env python

import sys
import re
import json


class Mapper:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        sys.stdin = stdin
        sys.stdout = stdout

    def run(self):
        predicates = ['type.object.name','type.object.type','common.topic.alias']
        re_ns = re.compile(r'ns/([\w.]+)')
        re_str_ns = re.compile(r'"(.+)"@(.*?)$|ns/([\w._]+)')

        for line in sys.stdin:
            triple = line.split("\t")
            try:
                k = re.search(re_ns, triple[0]).group(1)
                if k[:2] == "g.":
                    continue
            except:
                continue
            v = [None, None]
            v[0] = re.search(re_ns, triple[1])
            if not v[0]:
                continue
            v[0] = v[0].group(1)
            if not v[0] in predicates:
                continue
            v[1] = re.search(re_str_ns, triple[2])
            if not v[1]:
                continue
            if not v[1].group(3) and v[1].group(2) != 'en':
                continue
            else:
                v[1] = v[1].group(1) or v[1].group(3)
            if k[:2] == "m.":
                print("%s\t%s" % (k, json.dumps(v)), file=sys.stdout, flush=True)
            else:
                if v[0] == "type.object.name":
                    print("%s\t%s" % (k, json.dumps(v[1])), file=sys.stdout, flush=True)

if __name__ == "__main__":
    m = Mapper()
    m.run()