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
            line_tuple = line.split("\t")
            k = line_tuple[0]
            v = json.loads(line_tuple[1])

            if k.startswith("m."):  # if "m." object
                if k != self.lastkey:  # if object is complete, output it
                    try:
                        d['alias'].sort()
                        d['type'].sort()
                        print(json.dumps(d))
                    except:
                        pass
                    self.lastkey = k  # initialize new object
                    d = dict()
                    d['id'] = k
                    d['alias'] = list()
                    d['type'] = list()

                if v[0]=='type.object.name':  # fill name
                    d['name'] = v[1]
                elif v[0]=='common.topic.alias':  # add alias
                    d['alias'].append(v[1])
                elif v[0]=='type.object.type':  # add type id
                    d['type'].append(v[1])
            else:
                 sys.stdout.write(line)  # if type (not "m."), just output unchanged

        print(json.dumps(d))  # outputs last completed object

if __name__ == "__main__":
    r = Reducer()
    r.run()
