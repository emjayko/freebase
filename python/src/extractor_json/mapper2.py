#!/usr/bin/env python

import sys
import json
import copy

class Mapper:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        sys.stdin = stdin
        sys.stdout = stdout

    def run(self):
        for line in sys.stdin:
            if line.startswith("{"):
                obj = json.loads(line)
                obj_out = copy.deepcopy(obj)
                del obj_out['type']
                for t in obj['type']:
                    print("%s#1\t%s" % (t, json.dumps(obj_out)))
            else:
                split = line.split("\t")
                sys.stdout.write("%s#0\t%s" % (split[0], split[1]))

if __name__ == "__main__":
    m = Mapper()
    m.run()