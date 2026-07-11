set j [lindex $argv 0]


mol new ./recenter.pdb
set sel [atomselect top "all"]
$sel set beta 0
$sel set occupancy 0
set qm_lipid [atomselect top "segname MEMB and resid $j" ]
$qm_lipid set occupancy 1 
#Use_QM_InfoFromPDB true
$qm_lipid set beta 1 
#Use_Active_InfoFromPDB true
#$sel writepdb memb.pdb
$qm_lipid writepdb memb.pdb

quit
