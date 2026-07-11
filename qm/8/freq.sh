#!/bin/bash
#SBATCH --job-name=ORCA
#SBATCH --nodes=1
#SBATCH --mem=80GB
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --time=168:00:00  


###  #SBATCH --exclude=bb081,bb082,bb083,bb084,bb085,bb086,bb087,bb088,bb089,bb090,bb091

path=$PWD

cd $SLURM_SUBMIT_DIR


module purge
module load orca/6.0.1/
module load gcc/toolset/12
module load ucx/1.13.1
module load openmpi/4.1.5/gcc-12


#module openmpi/4.1.5/

export UCX_LOG_LEVEL=error

file="next.seqno"


cp freq.pdb setup.pdb
cp freq.gbw setup.gbw


timeout 168h /home/rja7/orca/6.0.1/orca $path/freq.inp > $path/freq.out


sleep 1m







