#!/usr/bin/env python

import sys
import json

class Reducer:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        """Init allows to redirect input and output, i.e. for testing purposes."""
        sys.stdin = stdin
        sys.stdout = stdout

    def run(self):
        for line in sys.stdin:
            split = line.split("\t")
            v = json.loads(split[1])
            if split[1].startswith("{"):  # if JSON of "m." object
                v['type'] = [type]  # set it's type
                print("%s\t%s" % (v['id'], json.dumps(v)))  # output object with type set and mid as key
            else:  # if type
                type = v  # store type of following objects

if __name__ == "__main__":
    r = Reducer()
    r.run()
