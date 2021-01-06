#!/bin/bash

for ((i=51;i<=100;i=i+1))
do
cat >> groupfile << EOF
-O -i smd_$i.in -p pdb/ala.top -c pdb/ala_$i.crd -r md_$i.rst -x ala_$i.traj 
EOF
done

