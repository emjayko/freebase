#!/usr/bin/env python

import sys
import json

class Reducer:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        sys.stdin = stdin
        sys.stdout = stdout

    def run(self):
        for line in sys.stdin:
            split = line.split("\t")
            v = json.loads(split[1])
            if split[1].startswith("{"):
                v['type'] = [type]
                print("%s\t%s" % (v['id'], json.dumps(v)))
            else:
                type = v

if __name__ == "__main__":
    r = Reducer()
    r.run()
