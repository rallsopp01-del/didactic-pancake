#!/bin/csh
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --mem=2G  
#SBATCH --job-name=Distance_from_membrane
#SBATCH -t 03:15:00


module load vmd
module load charmm
#module switch umd-software-library/new
#module load orca/6.0.0 
#module load openmpi/4.1.5

#orca_mm -convff -CHARMM recenter.psf ./toppar/par_all36m_prot.prm ./toppar/par_all36_na.prm ./toppar/par_all36_carb.prm ./toppar/par_all36_lipid.prm ./toppar/par_all36_cgenff.prm ./toppar/toppar_water_ions.str


set i = 151 # this is the dcd or frame number in the trajectory
set j = 1 # this is the lipid number within a bilayer
while ( $i <= 151 )
     while ( $j <= 100 )
          #recenter line
          #/home/jbklauda/charmm/c47b2/bin/charmm resid=$j dnum=$i < recenter1.inp > recenter1.out
          #/home/jbklauda/charmm/c47b2/bin/charmm resid=$j dnum=$i < recenter2.inp > recenter2.out
          #/home/jbklauda/charmm/c47b2/bin/charmm resid=$j dnum=$i < recenter3.inp > recenter3.out
          #/home/jbklauda/charmm/c47b2/bin/charmm dnum=$i < getframe.inp > getframe.out
          /mnt/commons/meuse/allsoppr/charmm/bin/charmm resid=$j dnum=$i < recenter1.inp > recenter1.out
          /mnt/commons/meuse/allsoppr/charmm/bin/charmm resid=$j dnum=$i < recenter2.inp > recenter2.out
          /mnt/commons/meuse/allsoppr/charmm/bin/charmm resid=$j dnum=$i < recenter3.inp > recenter3.out
          /mnt/commons/meuse/allsoppr/charmm/bin/charmm dnum=$i < getframe.inp > getframe.out
          vmd -dispdev text -e conv.tcl -args $j
          mkdir -p "qm/$j"
          cp memb.pdb "./qm/$j/setup.pdb"
          cp recenter.pdb "./qm/$j/recenter.pdb"
          #cp recenter.ORCAFF.prms "./qm/$j/recenter.ORCAFF.prms"
          #cd "./qm/"
          #cp * "./$j"
          #cd "./$j"
          #sbatch test_3.sh
          #cd ../../
          ##rm *dcd *pdb
          @ j++
     end
     @ i++
end
