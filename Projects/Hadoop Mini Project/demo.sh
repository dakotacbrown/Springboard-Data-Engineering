#!/bin/bash
wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/mapper1.py &&
wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/mapper2.py &&
wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/reducer1.py &&
wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/reducer2.py &&
wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/data.csv &&
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file mapper1.py -mapper mapper1.py \
-file reducer1.py -reducer autoinc_reducer1.py \
-input input/data.csv -output output/all_accidents &&
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file mapper2.py -mapper mapper2.py \
-file reducer2.py -reducer reducer2.py \
-input output/all_accidents -output output/make_year_count
