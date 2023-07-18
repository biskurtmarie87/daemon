echo "process is running" >> /tmp/running
count_line=`cat /tmp/running |wc -l`
echo $count_line >> /tmp/running
echo "" >> /tmp/running
