#!/bin/bash
#SBATCH --job-name=gra
#SBATCH --nodes=1
#SBATCH --mem=1GB
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=127:00:00  

source activate myenv
conda init
conda activate myenv

#I just need a for loop that 



for i in  {1..10..1}
do
	#changes directories to find files copy them to the destinaiton
	mkdir $i
	cp ../$i/freq.out ./$i/freq.out
	cp code_so_far_z.py ./$i/code_so_far_z.py
	cp code_so_far_r.py ./$i/code_so_far_r.py
	cp ../$i/freq.xyz ./$i/freq.activeRegion.xyz
	cp ../$i/recenter.pdb ./$i/freq.pdb
	cp ../$i/recenter.pdb ./freq.pdb
	#This line is used to uncenter the lipid so that the bilayer overall becomes the COM
	egrep "MEMB" freq.pdb | awk '{print $8}' > ./$i/memb.txt
	cp orca-ir.py ./$i/orca-ir.py
	cp 2Dpy_r.py ./$i/2Dpy_r.py
	cp 2Dpy_z.py ./$i/2Dpy_z.py
	cd ./$i/
	#executes the IR program
	python orca-ir.py freq.out
	python code_so_far_z.py
	python code_so_far_r.py
	cd ../
done



