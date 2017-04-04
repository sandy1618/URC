#!/bin/bash
hostname -I | grep -q 192.168.137 
exit_status=$?
if [ $exit_status -eq 1 ]; then
    echo "ERROR: you do not have an IP on the robot network (192.168.137.x). Please set one. Aborting..."
    return 1
fi

export ROS_IP=`hostname -I`
export ROS_MASTER_URI=http://192.168.137.213:11311/
