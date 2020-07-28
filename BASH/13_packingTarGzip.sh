# !/bin/bash

# Packing all .sh files
tar -cvf shell.tar *.sh

# .tar will be deleted
gzip shell.tar

# Packing a file with ratio 9
gzip -9 08_arraysLoops.sh
