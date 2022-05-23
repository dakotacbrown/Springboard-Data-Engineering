#Hadoop Mini Project

##Installing mrjob on HDP

'''
yum-config-manager --save --setopt=HDP-SOLR-2.6-100.skip_if_unavailable=true
yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel...
yum install python-pip
pip install pathlib
pip install mrjob==0.7.4
pip install PyYAML==5.4.1
'''

##Installing python 2.7 on HDP
'''
yum install scl-utils
yum install centos-release-scl
yum install python27
scl enable python27 bash
'''

##Running program on Hadoop cluster:
'''
python AutomobileReport.py –r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar data.csv
'''