#!/bin/csh
#SBATCH --ntasks=1
#SBATCH -N 1 
#SBATCH --job-name=recenter_3
#SBATCH -t 00:15:00
#SBATCH -p debug

# Run this script recenter1.csh first, then run recenter2.csh
# Recentering should be fast enough to be handled in the 'debug' queue
/homes/jbklauda/charmm/c43b1/exec/gnu/charmm < recenter3.inp >& recenter3.out



rm -f *tmp*.dcd
rm -f *tmp2.dcd


