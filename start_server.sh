#!/bin/bash

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    echo "** Trapped CTRL-C"
}

for i in `seq 1 5`; do
    sleep 1
    echo -n "."
done

#Check if Docker Service is running.
    #Run if Docker is Down
#Start Containers for Elastic Search
#Start Container for Redis

#Create worker process
