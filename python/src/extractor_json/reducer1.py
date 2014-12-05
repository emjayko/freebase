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
            line_tuple = line.split("\t")
            k = line_tuple[0]
            v = json.loads(line_tuple[1])

            if k.startswith("m."):
                if k != self.lastkey:
                    try:
                        d['alias'].sort()
                        d['type'].sort()
                        print(json.dumps(d))
                    except:
                        pass
                    self.lastkey = k
                    d = dict()
                    d['id'] = k
                    d['alias'] = list()
                    d['type'] = list()

                if v[0]=='type.object.name':
                    d['name'] = v[1]
                elif v[0]=='common.topic.alias':
                    d['alias'].append(v[1])
                elif v[0]=='type.object.type':
                    d['type'].append(v[1])
            else:
                 sys.stdout.write(line)

        print(json.dumps(d))

if __name__ == "__main__":
    r = Reducer()
    r.run()
