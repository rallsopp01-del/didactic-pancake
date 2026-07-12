This tutorial shows how to use 2D-COS methodologies in an automated framework with 3 phases to generate a corrolation between the correspondence in the order of positions and predict RMSD.

Phase 0:
Calculate the quantum mechanics (QM) spectra of DOPC lipid. The lipid must be recentered for the radial orders of positions to mean anything. Then for the Z order of events to be compared with each other the Z dimension needs to be uncentered so that the common center is the center of mass (COM) of the bilayer. This is implemented in conv_run.sh in the outter folder and can be modified to spawn runs in the QM folder and recenter the bilayer in charmm software.

For loop takes lipid 1 -> recenters lipid 1 -> extracts pdb of just lipid 1 -> saves the pdb after being recentered so that we can subtract the COM of the bilayer to reach a common center for all lipids later.

Run as many lipids as needed by adjusting the for loop to consider as many frames and lipids within the bialyer as necessary.

Phase 1: 
Calculate the order of positions. For demonstration purposes look at folder QM/
