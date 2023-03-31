#! bin/bash/

###############################################################################
# Configuration
###############################################################################
mkdir ~/hadoop
cd ~/hadoop
sudo apt get install default-jdk default-jre openssh-client openssh-server -y
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
wget https://jcenter.bintray.com/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.jar

ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 640 ~/.ssh/authorized_keys
sudo service ssh start
ssh localhost

sudo tar -xvzf hadoop-3.3.1.tar.gz
export HADOOP_HOME=~/hadoop/hadoop

sudo mkdir -p $HADOOP_HOME/logs
sudo mkdir -p $HADOOP_HOME/node/namenode
sudo mkdir -p $HADOOP_HOME/node/datanode
sudo chown -R root:sudo $HADOOP_HOME

export HADOOP_HOME=$HADOOP_HOME
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_CLASSPATH+=" $HADOOP_HOME/lib/*.jar"
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"

cat > $HADOOP_HOME/etc/hadoop/core-site.xml << EOF
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://localhost:9000</value>
        <description>The default file system URI</description>
    </property>
</configuration>
EOF

cat > $HADOOP_HOME/etc/hadoop/hdfs-site.xml << EOF
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.name.dir</name>
        <value>file:///$HADOOP_HOME/hdfs/namenode</value>
    </property>
    <property>
        <name>dfs.data.dir</name>
        <value>file:///$HADOOP_HOME/hdfs/datanode</value>
    </property>
</configuration>
EOF

cat > $HADOOP_HOME/etc/hadoop/mapred-site.xml << EOF
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
EOF

cat > $HADOOP_HOME/etc/hadoop/yarn-site.xml << EOF
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
EOF

# http://localhost:9870
$HADOOP_HOME/bin/hdfs namenode -format
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh


###############################################################################
# Practical 2
###############################################################################
# Q.1) Write a Command to create a directory of your name and surname [example:
# manishsingh]
hadoop fs -mkdir /ommarshaikh
hadoop fs -ls /

# Q.2) Write a Hadoop Command to create a file in the directory of your name.
hadoop fs -touch /ommarshaikh/ommar
hadoop fs -ls /ommarshaikh

# Q.3) Write a command to upload a file and folder from your local file system to the
# directory of your name in Hadoop file system.
hadoop fs -put ~/psclocalfile /ommarshaikh
hadoop fs -put ~/PSC021 /ommarshaikh
hadoop fs -ls /ommarshaikh

# Q.4) Write a command to check the health of a file along with block and rack
# information for the file uploaded in the directory of your name in Hadoop file system.
# (Based on command used Q.3)
hadoop fsck /ommarshaikh -files

# Q.5) Create a new directory in Hadoop file system with your last name and move all
# files from the folder created in Q.1 to your new directory
hadoop fs -mkdir /shaikh
hadoop fs -ls /

hadoop fs -ls /ommarshaikh
hadoop fs -mv /ommarshaikh/ommar /shaikh
hadoop fs -mv /ommarshaikh/psclocalfile /shaikh
hadoop fs -ls /shaikh

# Q.6) Write a command to demonstrate use of copyToLocal command within your
# Hadoop file system directories
hadoop fs -ls /shaikh
hadoop fs -copyToLocal /shaikh/ommar ~/psclocaldir
ls ~/psclocaldir

# Q.7) Write a command to demonstrate use of tail command on a text file. (use your own
# text file but name of file must have your firstname followed by rollno)
hadoop fs -tail /ommarshaikh/ommar021

# 8) Write a command to demonstrate use of chown command on any of the file or
# directory inside your Hadoop file system.
hadoop fs -ls /ommarshaikh
hadoop fs -chown newhadoop /ommarshaikh/ommarsc
hadoop fs -ls /ommarshaikh

# Q.9) Write a command to demonstrate use of chgrp command on any of the file or
# directory inside your Hadoop file system.
hadoop fs -ls /ommarshaikh
hadoop fs -chgrp newgroup /ommarshaikh/ommarsc
hadoop fs -ls /ommarshaikh

# Q.10) Write a command to demonstrate use of df command on any of the file or
# directory inside your Hadoop file system
hadoop fs -df /ommarshaikh
hadoop fs -df -h /ommarshaikh

# Q.11) Write a command to demonstrate use of chmod command on any of the file or
# directory inside your Hadoop file system.
hadoop fs -ls /ommarshaikh
hadoop fs -chmod -r /ommarshaikh/PSC021
hadoop fs -ls /ommarshaikh
hadoop fs -chmod g+rwx /ommarshaikh/PSC021
hadoop fs -ls /ommarshaikh

# Q.12) Write a command to append two different text file present inside your Hadoop
# file system. (If text files are not available use any 2 text file from your local system and
# upload it to your Hadoop file system)
hadoop fs -appendToFile pscfile1 pscfile2 /ommarshaikh/ommar021
hadoop fs -cat /ommarshaikh/ommar021
hadoop fs -put ~/pscfile1 /ommarshaikh

hadoop fs -put ~/pscfile2 /ommarshaikh
hadoop fs -ls /ommarshaikh
hadoop fs -appendToFile pscfile1 pscfile2 /ommarshaikh/ommarsc
hadoop fs -cat /ommarshaikh/ommarsc

# Q.13) Write a command to demonstrate use of checksum command on any of the file
# stored inside your Hadoop file system.
hadoop fs -checksum /ommarshaikh/ommar021

# Q.14) Write a command to demonstrate use of count command along with its various
# options.
hadoop fs -count -v /ommarshaikh

hadoop fs -count -v -q /ommarshaikh
hadoop fs -count -v -u /ommarshaikh
hadoop fs -count -v -h /ommarshaikh

# Q.15) Write a command to remove files and directories from your Hadoop file system
hadoop fs -ls /ommarshaikh
hadoop fs -rm /ommarshaikh/pscfile1
hadoop fs -rm /ommarshaikh/pscfile2
hadoop fs -ls /ommarshaikh
hadoop fs -ls /
hadoop fs -rm -r /shaikh
hadoop fs -ls /

# Q.16) Write a command to copy file from one of your HDFS directory to another HDFS
# directory.
hadoop fs -ls /kes
hadoop fs -ls /admin
hadoop fs -cp /kes/file1 /admin
hadoop fs -ls /admin

# Q.17) Write a command to check the version of your Hadoop HDFS.
hadoop version

# Q.18) Write a command to demonstrate use of stat command along with its various
# options.
hadoop fs -ls /kes
hadoop fs -stat %b /kes/demofile
hadoop fs -stat %g /kes/demofile
hadoop fs -stat %n /kes/demofile
hadoop fs -stat %o /kes/demofile
hadoop fs -stat %r /kes/demofile
hadoop fs -stat %u /kes/demofile
hadoop fs -stat %y /kes/demofile

# Q.19) Write a command to demonstrate use of find command to search for the path of
# the specified file or directory.
hadoop fs -find / -name demofile -print
hadoop fs -ls /kes

# Q.20) Write a command to demonstrate use of copyFromLocal command within your
# Hadoop file system directories.
ls ~/
hadoop fs -copyFromLocal ~/sample /kes
hadoop fs -ls /kes
