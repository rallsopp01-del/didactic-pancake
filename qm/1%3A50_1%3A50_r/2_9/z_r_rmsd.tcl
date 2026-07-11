# argv is the passed variable
set i [lindex $argv 0]


mol new ./freq.QMRegion_a.xyz
mol new ./freq.QMRegion_b.xyz
set outfile1 [open "../r2a.txt" "a"]


set sel1 [atomselect 0 "all" ] 
set sel2 [atomselect 1 "all" ] 

#$sel2 move [trans x 180]            
#this flips the coordinates


set diffr 0
set diffz 0
set diff 0
set ravg1 0
set ravg2 0

# Step 1: Initialize an empty list
set values_list1 {}
# Step 1: Initialize an empty list
set values_list2 {}
# Step 1: Initialize an empty list
set values_list1z {}
# Step 1: Initialize an empty list
set values_list2z {}


for {set i 0} {$i < 138} {incr i} {

set data1 [measure center [atomselect 0 "index $i" ] weight mass]
set data2 [measure center [atomselect 1 "index $i" ] weight mass]


set lipidx1 [lindex $data1 0]
set lipidx2 [lindex $data2 0]

set lipidy1 [lindex $data1 1]
set lipidy2 [lindex $data2 1]

set lipidz1 [lindex $data1 2]
set lipidz2 [lindex $data2 2]


set lipidr1 [expr { pow( pow(($lipidx1 ),2)+ pow(($lipidy1 ),2), 0.5 )}]
set lipidr2 [expr { pow( pow(($lipidx2 ),2)+ pow(($lipidy2 ),2), 0.5 )}]

set ravg1 [expr {$ravg1 + pow( pow(($lipidr1),2), 0.5 )}]
set ravg2 [expr {$ravg2 + pow( pow(($lipidr2),2), 0.5 )}]


set zi1 [expr {$lipidz1}]
lappend values_list1z $zi1
set zi2 [expr {$lipidz2}]
lappend values_list2z $zi2

set ri1 [expr {pow( pow(($lipidr1),2), 0.5 )}]
lappend values_list1 $ri1
set ri2 [expr {pow( pow(($lipidr2),2), 0.5 )}]
lappend values_list2 $ri2

set diffr [expr {$diffr + pow(($lipidr1-$lipidr2 ),2) }]
set diffz [expr {$diffz + pow(($lipidz1-$lipidz2 ),2) }]



set diff [expr {$diffr+$diffz}]
#set diff $diffz


}



set diff [expr { pow(($diff/(138)),0.5) }]

puts -nonewline $outfile1 " $diff  "

close $outfile1


exit
