#!/usr/bin/env python

import sys
import json

class Reducer:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        """Init allows to redirect input and output, i.e. for testing purposes."""
        sys.stdin = stdin
        sys.stdout = stdout
        self.lastkey = None

    def run(self):
        for line in sys.stdin:
            split = line.split("\t")
            if split[0]!=self.lastkey:  # if object complete
                try:
                    print(json.dumps(obj))  # output it
                except:
                    # just in case something bad happens
                    pass
                self.lastkey = split[0]  # load new object
                obj = json.loads(split[1])
            else:
                o = json.loads(split[1])  # load object with one type
                obj['type'].append(o['type'].pop())  # add the type to object being completed

        print(json.dumps(obj))  # outputs last complete object

if __name__ == "__main__":
    r = Reducer()
    r.run()
