#!/bin/bash
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/files/mapper1.py -mapper \
'python mapper1.py' -file ~/files/reducer1.py -reducer 'python reducer1.py' -input \
~/files/data.csv -output ~/output/all_accidents

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file ~/files/mapper2.py -mapper \
'python mapper2.py' -file ~/files/reducer2.py -reducer 'python reducer2.py' -input \
~/output/all_accidents -output ~/output/make_year_count