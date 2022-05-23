#!/bin/bash
wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/AutomobileReport.py &&
wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/data.csv &&
python AutomobileReport.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar data.csv > output.txt