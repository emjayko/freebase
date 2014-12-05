#!/usr/bin/env python

import sys
import unittest
import json
from io import StringIO
import mapper1, mapper2
import reducer1, reducer2, reducer3

class Test(unittest.TestCase):

    def setUp(self):
        self.test_input = """
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/type.object.name>\t"Firefox"@en\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/type.object.name>\t"Mozilla Firefox"@fr\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/type.object.name>\t"\ud30c\uc774\uc5b4\ud3ed\uc2a4"@ko\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"Mozilla Firebird"@en\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"Phoenix"@en\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"Mozilla Firefox"@en\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"Firefox"@nl\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"\u0e44\u0e1f\u0e23\u0e4c\u0e1f\u0e2d\u0e01\u0e0b\u0e4c"@th\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"FF"@en\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"\u0416\u0430\u0440-\u043b\u0438\u0441"@uk\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/type.object.type>\t"http://rdf.freebase.com/ns/common.topic>\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/type.object.type>\t"http://rdf.freebase.com/ns/computer.software>\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/type.object.type>\t"http://rdf.freebase.com/ns/computer.operating_system>\t.
            <http://rdf.freebase.com/ns/m.01dyhm>\t<http://rdf.freebase.com/ns/type.object.type>\t"http://rdf.freebase.com/ns/computer.web_browser>\t.
            <http://rdf.freebase.com/ns/common.topic>\t<http://rdf.freebase.com/ns/type.object.name>\t"Topic"@en\t.
            <http://rdf.freebase.com/ns/computer.software>\t<http://rdf.freebase.com/ns/type.object.name>\t"Software"@en\t.
            <http://rdf.freebase.com/ns/computer.operating_system>t<http://rdf.freebase.com/ns/type.object.name>\t"Operating System"@en\t.
            <http://rdf.freebase.com/ns/computer.web_browser>\t<http://rdf.freebase.com/ns/type.object.name>\t"Web browser"@en\t.
            <http://rdf.freebase.com/ns/computer.web_browser>\t<http://rdf.freebase.com/ns/type.object.name>\t"Webov\xfd prohl\xed\u017ee\u010d"@cs\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/type.object.name>\t"Ubuntu"@en\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"Ubuntu Linux"@en\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/computer.software>\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/computer.operating_system>\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/common.topic>\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/business.brand>\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/event.speech_topic>\t.
            <http://rdf.freebase.com/ns/m.03x5qm>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/book.book_subject>\t.
            <http://rdf.freebase.com/ns/business.brand>\t<http://rdf.freebase.com/ns/type.object.name>\t"Brand"@en\t.
            <http://rdf.freebase.com/ns/event.speech_topic>\t<http://rdf.freebase.com/ns/type.object.name>\t"Speech topic"@en\t.
            <http://rdf.freebase.com/ns/book.book_subject>\t<http://rdf.freebase.com/ns/type.object.name>\t"Literature Subject"@en\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/type.object.name>\t"Linux kernel"@en\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/type.object.name>\t"Linux"@sk\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"Linux"@en\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/common.topic.alias>\t"Linuxov\xe9 j\xe1dro"@cs\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/computer.software>\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/event.speech_topic>\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/common.topic>\t.
            <http://rdf.freebase.com/ns/m.04pm6>\t<http://rdf.freebase.com/ns/type.object.type>\t<http://rdf.freebase.com/ns/computer.computing_platform>\t.
            <http://rdf.freebase.com/ns/computer.computing_platform>\t<http://rdf.freebase.com/ns/type.object.name>\t"Computing Platform"@en\t.
            """

        self.test_output = [
            {"id": "m.01dyhm", "alias": ["FF", "Mozilla Firebird", "Mozilla Firefox", "Phoenix"], "name": "Firefox", "type": ["Computing Platform", "Software", "Topic", "Web browser"]},
            {"id": "m.03x5qm", "alias": ["Ubuntu Linux"], "name": "Ubuntu", "type": ["Brand", "Computing Platform", "Literature Subject", "Software", "Speech topic", "Topic"]},
            {"id": "m.04pm6", "alias": ["Linux"], "name": "Linux kernel", "type": ["Computing Platform", "Software", "Speech topic", "Topic"]}
        ]

    def test_t(self):
        buf1 = StringIO()
        buf2 = StringIO()
        m = mapper1.Mapper(StringIO(self.test_input), buf1)
        m.run()
        l = buf1.getvalue().split("\n")
        l.sort()
        buf1 = StringIO("\n".join(l[1:]))
        r = reducer1.Reducer(buf1, buf2)
        r.run()
        buf2.seek(0)
        buf1 = StringIO()
        m = mapper2.Mapper(buf2, buf1)
        m.run()
        l = buf1.getvalue().split("\n")
        l.sort()
        buf1 = StringIO("\n".join(l[1:]))
        buf2 = StringIO()
        r = reducer2.Reducer(buf1, buf2)
        r.run()
        l = buf2.getvalue().split("\n")
        l.sort()
        buf2 = StringIO("\n".join(l[1:]))
        buf1 = StringIO()
        r = reducer3.Reducer(buf2, buf1)
        r.run()
        buf1.seek(0)

        t_out = []
        for line in buf1:
            t_out.append(json.loads(line))
        self.assertEqual(len(t_out), len(self.test_output))
        for i in range(len(t_out)):
            self.assertCountEqual(t_out[i].keys(), self.test_output[i].keys())
            self.assertEqual(t_out[i]['id'], self.test_output[i]['id'], "IDs not equal in: "+json.dumps(t_out[i]))
            self.assertEqual(t_out[i]['name'], self.test_output[i]['name'], "Names not equal in: "+json.dumps(t_out[i]))
            self.assertCountEqual(t_out[i]['alias'], self.test_output[i]['alias'], "Aliases not equal in: "+json.dumps(t_out[i]))
            self.assertCountEqual(t_out[i]['type'], self.test_output[i]['type'], "Types not equal in: "+json.dumps(t_out[i]))

if __name__ == "__main__":
    unittest.main()