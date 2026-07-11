#!/bin/bash
#SBATCH --job-name=gra
#SBATCH --nodes=1
#SBATCH --mem=1GB
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=127:00:00  


conda init
source activate myenv
conda activate myenv
conda init


#I just need a for loop that 
#changes directories to find files copy them to the destinaiton
#execute the IR program
#append the result to a file

	#for j in  {51..100..1}
	#for j in $(seq $((i + 1)) 100); do
	#for j in $(seq $((i + 1)) 50); do


for i in {1..50..1}; do
	for j in  $(seq $((i + 1)) 50) ; do
    		mkdir ${i}_${j}
		cp ../x_y_z_order_of_events_all_wn/$i/count_dist_z.csv ./${i}_${j}/count_dist_a.csv
		cp ../x_y_z_order_of_events_all_wn/$i/count_dist_r.csv ./${i}_${j}/count_dist_a_r.csv
		cp ../$i/freq.xyz ./${i}_${j}/freq.QMRegion_a.xyz
		cp ../x_y_z_order_of_events_all_wn/$j/count_dist_z.csv ./${i}_${j}/count_dist_b.csv
		cp ../x_y_z_order_of_events_all_wn/$j/count_dist_r.csv ./${i}_${j}/count_dist_b_r.csv
		cp ../$j/freq.xyz ./${i}_${j}/freq.QMRegion_b.xyz
		cp z_rmsd.tcl ./${i}_${j}/z_rmsd.tcl
		cp knn.py ./${i}_${j}/knn.py
		cp fit.py ./${i}_${j}/fit.py
		cd ./${i}_${j}/
		#This is for z-r-RMSD
		vmd -e z_rmsd.tcl -args $i $j
		awk -F, -v ix="$i" 'NR==1 {print ix "WN," ix "CNTZ"} NR>1 {print $1 "," $2}' "count_dist_a.csv" > temp_a.csv
		awk -F, -v ix="$i" 'NR==1 {print ix "CNTR"} NR>1 { print $2}' "count_dist_a_r.csv" > temp_a_r.csv
		awk -F, -v jx="$j" 'NR==1 {print jx "WN," jx "CNTZ"} NR>1 {print $1 "," $2}' "count_dist_b.csv" > temp_b.csv
		awk -F, -v jx="$j" 'NR==1 {print jx "CNTR"} NR>1 { print $2}' "count_dist_b_r.csv" > temp_b_r.csv
		#this is part of the flip protocol turned off
		awk -F, 'BEGIN {OFS=","} NR==1 {print $1, $2} NR>1 {new_value = $2; print $1, new_value}' temp_b.csv > temp_b_flip.csv	
		paste -d, temp_a.csv temp_a_r.csv temp_b_flip.csv temp_b_r.csv > "raw_data.csv"
		awk -F, '{print $2 "," $3 "," $1 "," $4 "," $5 "," $6}' "raw_data.csv" > raw_data1.csv
		python knn.py
		awk -F, '{print $2 "," $5}' tmp.csv > fit.csv
		python fit.py $i $j
		cd ../
		#egrep -i "Final Gibbs free energy" ../unconfoluted_order_graph_mine/$i/freq.out >> r2a.txt
		#egrep -i "Final Gibbs free energy" ../unconfoluted_order_graph_mine/$j/freq.out >> r2a.txt 
done
done

