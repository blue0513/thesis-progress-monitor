#!/bin/sh

YOUR_LOG_DIRECTORY="log"
YOUR_LOG_FILE="log.txt"

mkdir -p ${YOUR_LOG_DIRECTORY};
touch ${YOUR_LOG_DIRECTORY}/${YOUR_LOG_FILE};

echo 0 >> ${YOUR_LOG_DIRECTORY}/${YOUR_LOG_FILE}
echo "create your log directory and logfile!"
