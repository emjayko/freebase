Freebase JSON extractor
=======================
Simple Python extractor of Freebase objects using Hadoop.

It only extracts attributes *mid*, *type.object.name*, *common.topic.alias* and *type.object.type* attributes from *"m."* objects. It's also limited to get only *@en* (i.e. en-gb, en-us) values.
Advantage of this extractor is that types are dereferenced, so it outputs theirs real english names.

Dependencies
------------
 * Python 3.x
 * Hadoop 2.5.x (partially optional)

Usage
-----
Extractor consists of 2 mappers and 3 reducers, which can be used independently. Of course, it's better to use them together.

Scripts can be used either using shell and pipes (they use stdin/stdout) or with hadoop streaming jobs.

**Be careful**, 2nd job needs following 3 options:  
 * -D mapreduce.map.output.key.field.separator='#'
 * -D mapreduce.partition.keypartitioner.options=-k1,1
 * -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

#### Run using run.sh
Trying to make things easier, I prepared script to run 3 Hadoop jobs.
You only need to provide some arguments depending on your environment:
 1. path to Hadoop dir
 2. path to dir containing mapper/reducer scripts
 3. path and filename of input data file
 4. path where outputs and temporary files will be stored

This is simple way to run extractor locally without HDFS and only downloaded and extrated Hadoop.

Input / output
--------------
Expected input is *tab-separated RDF triples* file, which can be downloaded for example from: https://developers.google.com/freebase/data#freebase-rdf-dumps

Output is file with one JSON object per line.  
Example:

    {
        "id": "m.01dyhm",
        "name": "Firefox",
        "alias": ["FF", "Mozilla Firebird", "Mozilla Firefox", "Phoenix"],
        "type": ["Web browser", "Topic", "Operating System", "Software"]
    }
