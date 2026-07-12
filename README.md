This tutorial shows how to use 2D-COS methodologies in an automated framework with 3 phases to generate a corrolation between the correspondence in the order of positions and predicted RMSD.

Phase 0:
** see phase two for an addition to this section of the workflow.

Calculate the quantum mechanics (QM) spectra of DOPC lipid. The lipid must be recentered for the radial orders of positions to mean anything. Then for the Z order of events to be compared with each other the Z dimension needs to be uncentered so that the common center is the center of mass (COM) of the bilayer. This is implemented in conv_run.sh in the outter folder and can be modified to spawn runs in the QM folder and recenter the bilayer in charmm software.

For loop takes lipid 1 -> recenters lipid 1 -> extracts pdb of just lipid 1 -> saves the pdb of the whole system after being recentered so that we can subtract the COM of the bilayer to reach a common reference center for all lipids later.

Run as many lipids as needed by adjusting the for loop to consider as many frames and lipids within the bialyer as necessary.

Phase 1: 
Calculate the order of positions. For demonstration purposes look at folder QM/x_y_z_order_of_events_all_wn/

sbatch executable_ooe.sh

Where the number of qm spectra can be controlled with the for loop in this case there were 10 qm simulations.

for i in  {1..10..1}

After each folder completes there should be a count_dist_r.csv and a count_dist_z.csv file in each folder. 

Count_dist_z.csv in folder 1

Wavenumber	Count	Z-Center Calculated for the mode

21.85	        244.0	48.543909171790034

Count_dist_r.csv in folder 1

Wavenumber	Count	R-Center Calculated for the mode

21.85	        124.0	3.5282975215294865

**** probably remove those and commit changes *** Not all of the wavenumbers were considered here, because some of the really low wavenumber modes had intensities of 0 so there is a way to control how many modes are used. 


To check that these orderings were correct I used a program called PyVibMS and it is important to check the orientation in the pymol viewer against the absolute axis in VMD https://github.com/smutao/PyVibMS

Phase 2: 
The next phase occurs in the folders with the %3A
1%3A50_1%3A50

1%3A50_1%3A50_r

1%3A50_51%3A100

1%3A50_51%3A100_r

51%3A100_51%3A100

51%3A100_51%3A100_r

They read in the files generated in the x_y_z_order_of_events_all_wn folder. The first thing to adjust is the extract.sh file to edit the following line:

for i in {1..50..1}; do

	for j in  $(seq $((i + 1)) 50) ; do

Where the 1 to 50 represents the lipids in the first leaflet of the bilayer. The initial code split the lipids into six groups (first leaflet to first leaflet, first leaflet to second leaflet, and second leaflet to second leaflet). 

Addition to phase 0 **
It is easier to actually flip all the second leaflet lipids during the recentering step and treat them all the same rather than having several separate folders that treat different parts later. Then just use the one for loop for the whole bilayer. I included the actual workflow used as well as an alternative. 

Launching this extract.sh file generates an r2a.txt file that contains the following:

RMSD for Z or Z+R   R^2>0.99               Counts Folder Pair Combination

 2.383030880423098  0.9902360030342431    300    1_2
 
 2.826369366231348  0.9902093137636016     278    1_3
 
 2.9867220201189393 0.9902254095886864     301    1_4
 
 3.2444515005725587 0.9900397280816947     287    1_5
 
 2.0194825483795573 0.9900699975881773     314    1_6
 
 3.254804540201345  0.9900574135458136     309    1_7




Then I pool all the Z RMSD vs count data from the different leaflets or just use one folder/job and flip all the lipids to a matching orientation in the recentering step. Then I usually copy the raw text into excel or Matlab to generate a plot of the counts that passed the R^2 threshold vs RMSD.
