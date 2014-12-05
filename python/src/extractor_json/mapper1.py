#!/usr/bin/env python

import sys
import re
import json


class Mapper:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        """Init allows to redirect input and output, i.e. for testing purposes."""
        sys.stdin = stdin
        sys.stdout = stdout

    def run(self):
        predicates = ['type.object.name','type.object.type','common.topic.alias']
        re_ns = re.compile(r'ns/([\w.]+)')  # Regexp to match mid
        re_str_ns = re.compile(r'"(.+)"@(.*?)$|ns/([\w._]+)')  # Regexp to match string value with lang id or reference

        for line in sys.stdin:
            triple = line.split("\t")  # split triples
            try:
                k = re.search(re_ns, triple[0]).group(1)  # get id
                if k[:2] == "g.":
                    # omit g. objects
                    continue
            except:
                # if error occurs, skip line
                continue
            v = [None, None]
            v[0] = re.search(re_ns, triple[1])  # get predicate
            if not v[0]:
                # on error, skip line
                continue
            v[0] = v[0].group(1)
            if not v[0] in predicates:
                # skip not desired predicates
                continue
            v[1] = re.search(re_str_ns, triple[2])  # get value or reference
            if not v[1]:
                # on error, skip line
                continue
            if not v[1].group(3) and v[1].group(2) != 'en':
                # skip non-@en values
                continue
            else:
                v[1] = v[1].group(1) or v[1].group(3)
            if k[:2] == "m.":
                # for "m." objects output mid and value
                print("%s\t%s" % (k, json.dumps(v)), file=sys.stdout, flush=True)
            else:
                if v[0] == "type.object.name":
                    # for type objects output type id and name
                    print("%s\t%s" % (k, json.dumps(v[1])), file=sys.stdout, flush=True)

if __name__ == "__main__":
    m = Mapper()
    m.run()
