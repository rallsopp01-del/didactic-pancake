#!/bin/csh
#SBATCH --ntasks=1
#SBATCH -N 1 
#SBATCH --job-name=recenter_2
#SBATCH -t 00:15:00
#SBATCH -p debug


# Run this script recenter1.csh first, then run recenter2.csh
# Recentering should be fast enough to be handled in the 'debug' queue
# In DT2
/homes/jbklauda/charmm/c43b1/exec/gnu/charmm < recenter2.inp >& recenter2.out



