#!/usr/bin/env python

import sys
import json

class Reducer:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        sys.stdin = stdin
        sys.stdout = stdout
        self.lastkey = None

    def run(self):
        for line in sys.stdin:
            split = line.split("\t")
            if split[0]!=self.lastkey:
                try:
                    print(json.dumps(obj))
                except:
                    pass
                self.lastkey = split[0]
                obj = json.loads(split[1])
            else:
                o = json.loads(split[1])
                obj['type'].append(o['type'].pop())

        print(json.dumps(obj))

if __name__ == "__main__":
    r = Reducer()
    r.run()
