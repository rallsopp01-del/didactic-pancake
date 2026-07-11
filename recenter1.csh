#!/bin/csh
#SBATCH --ntasks=1
#SBATCH -N 1 
#SBATCH --job-name=recenter_1
#SBATCH -t 00:15:00
#SBATCH -p debug


# Run this script recenter1.csh first, then run recenter2.csh
# Recentering should be fast enough to be handled in the 'debug' queue
# In DT2
/mnt/commons/meuse/allsoppr/charmm/bin/charmm < recenter1.inp >& recenter1.out


