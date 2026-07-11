#!/bin/bash
#SBATCH --job-name=g16test
#SBATCH --nodes=1
#SBATCH --mem=40GB
#SBATCH --partition=scavenger
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=1
#SBATCH --time=127:00:00  

path=$PWD

#cd $SLURM_SUBMIT_DIR


module switch umd-software-library/new
module load orca/6.0.0
module load openmpi/4.1.5


file="next.seqno"

timeout 125h /software/orca/6.0.0/linux_x86-64_openmpi416/bin/orca $path/freq.inp > $path/freq.out


sleep 1m






