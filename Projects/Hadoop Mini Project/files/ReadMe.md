#Hadoop Mini Project

##Running program on HortonWorks Sandbox HDP Hadoop cluster

Import the data, mapper, and reducer files into HDFS. 
With the mapper and reducer files, they must stored in 'home/user/files' within a user that can manipulate files like hdfs (i.e. '/home/hdfs/files').
The shell script can be stored in 'home/user' within a user that can manipulate files like hdfs (i.e. '/home/hdfs/demo.sh').
The files must be given the neccessary permissions to run, especially the shell script.

###Run the shell script:
'hadoop fs -cat ~/demo.sh | exec sh'