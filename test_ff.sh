#!/bin/csh
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --job-name=Distance_from_membrane
#SBATCH -t 00:15:00
#SBATCH -p debug


module load vmd
module load charmm
module switch umd-software-library/new
module load orca/6.0.0 
module load openmpi/4.1.5

orca_mm -convff -CHARMM recenter.psf ./toppar/par_all36m_prot.prm ./toppar/par_all36_na.prm ./toppar/par_all36_carb.prm ./toppar/par_all36_lipid.prm ./toppar/par_all36_cgenff.prm ./toppar/toppar_water_ions.str