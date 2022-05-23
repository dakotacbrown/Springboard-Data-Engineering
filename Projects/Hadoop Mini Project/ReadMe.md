#Hadoop Mini Project

##Installing pip on HDP

Follow these instuctions to install pip using root if not already downloaded.

'''
yum-config-manager --save --setopt=HDP-SOLR-2.6-100.skip_if_unavailable=true
yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum install python-pip
'''

##Installing mrjob on HDP

Follow these instuctions to install MRJob 0.7.4 using root if not already downloaded.

'''
pip install pathlib
pip install mrjob==0.7.4
pip install PyYAML==5.4.1
'''

##Installing python 2.7 on HDP

Follow these instuctions to install Python 2.7 using root if not already downloaded.

'''
yum install scl-utils
yum install centos-release-scl
yum install python27
scl enable python27 bash
'''

##Running program on Hadoop cluster

Getting the required files:
'wget raw.githubusercontent.com/dakotacbrown/Springboard-Data-Engineering/main/Projects/Hadoop%20Mini%20Project/demo.sh'

Run the shell script:
'''
chmod +x demo.sh
./demo.sh
'''