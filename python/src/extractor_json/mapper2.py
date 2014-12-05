#!/usr/bin/env python

import sys
import json
import copy

class Mapper:

    def __init__(self, stdin=sys.stdin, stdout=sys.stdout):
        """Init allows to redirect input and output, i.e. for testing purposes."""
        sys.stdin = stdin
        sys.stdout = stdout

    def run(self):
        for line in sys.stdin:
            if line.startswith("{"):  # if JSON is on the line
                obj = json.loads(line)  # parse it
                obj_out = copy.deepcopy(obj)  # copy it
                del obj_out['type']  # remove type
                for t in obj['type']:  # output it once for each type it has, with key to be type
                    print("%s#1\t%s" % (t, json.dumps(obj_out)))  # "#1" makes it to be ordered after type's name
            else:
                split = line.split("\t")
                sys.stdout.write("%s#0\t%s" % (split[0], split[1]))  # output type name with key to be type id.
                                                                     # "#0" makes it to be ordered before objects of this type

if __name__ == "__main__":
    m = Mapper()
    m.run()
