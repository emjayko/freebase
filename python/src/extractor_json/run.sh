#!/bin/bash
$1/bin/hadoop jar $1/share/hadoop/tools/lib/hadoop-streaming*.jar -D hadoop.tmp.dir=$4/hadoop.tmp -mapper $2/mapper1.py -reducer $2/reducer1.py -input $3 -output $4/output1
$1/bin/hadoop jar $1/share/hadoop/tools/lib/hadoop-streaming*.jar -D hadoop.tmp.dir=$4/hadoop.tmp -D mapreduce.map.output.key.field.separator='#' -D mapreduce.partition.keypartitioner.options=-k1,1 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -mapper $2/mapper2.py -reducer $2/reducer2.py -input $4/output1 -output $4/output2
$1/bin/hadoop jar $1/share/hadoop/tools/lib/hadoop-streaming*.jar -D hadoop.tmp.dir=$4/hadoop.tmp -mapper cat -reducer $2/reducer3.py -input $4/output2 -output $4/output3
