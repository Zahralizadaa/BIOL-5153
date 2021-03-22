#! /usr/bin/env python3
# This script turns out a PBS file for the AHPCC razor cluster


# variables:
job_name = 'Alizada_assn04'
queue = 'onenode16core'
out = 'Alizada_assn04'
node = 2
pro = 15
wall = 3


print('#PBS -N', job_name) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join the STDOUT and STDERR into a single file
print('#PBS -o' +  out + '.$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(node) + ':ppn=' + str(pro)) # how many resouces to ask for(nodes = num nudes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 3 hours)
print()

# cd into working directory 
print('cd $PBS_O_WORKDIR')
print()


# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

#commands for this job
print('# insert commands here')
