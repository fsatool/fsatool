#!/bin/bash

#SBATCH -J trp_1
##SBATCH --nodelist=gpu17
#SBATCH -n 5
#SBATCH -N 1
#SBATCH -p gpu
#SBATCH --gres=gpu:5
#SBATCH --qos=remd
#SBATCH --output=log.txt
#SBATCH --error=err.txt

#module load gcc/4.8.2
#module load cuda/8.0
#module load mpich/3.2/gcc-4.8.2
mol=trpzip2
srun --mpi=pmi2 ~/fsatool sim -O -i job.sh -p $mol.top -c $mol.rst -r md.rst -x $mol.traj -ref $mol.rst  > log.txt

&cntrl
 imin=0, ntb=0, igb=8, ntpr=1000, ntwr=10000, ntwx=20000
 ntt=3, tempi = 300.0, temp0 = 300.0, ig=-1, gamma_ln=1.0
 ntf=2, ntc=2, nstlim=500000000, dt=0.002, cut=999.0
/

&task
!  iftemd=.true.
  ifflood=.true.
/

&flood
  kelvindown=300.0, kelvinup=700.0, exchangestep=500000, biasrep=1, biasexc=1, moviecv=-1
  ss2cv=1,2, ssngrid=60, 60, floodingtime=10.0, fragsstime=1.0
/


&colvar
  cv_type = 'MULTI_RMSD'
  cv_min = 0, cv_max = 30
  cv_ni=  13, cv_nr=  36
  cv_i =    5,   16,   40,   54,   78,   93,  107,  114,  136,  160,  174,  198,   0, 
  cv_r = 
    -3.187,      8.462,      1.023,     -2.225,      4.801,      1.762, 
    -4.293,      1.763,      0.555,     -4.047,     -2.043,      1.131, 
    -3.607,     -4.303,     -1.973,     -2.409,     -7.943,     -2.572, 
    -1.114,     -8.275,      1.067,      0.937,     -4.966,      1.028, 
     0.524,     -1.163,      1.467,      0.503,      1.096,     -1.663, 
     0.192,      4.897,     -2.238,     -2.953,      6.324,     -3.999, 
/

&colvar
  cv_type = 'R_OF_GYRATION'
  cv_min = 0, cv_max = 20
  cv_ni= 12
  cv_i =    5,   16,   40,   54,   78,   93,  107,  114,  136,  160,  174,  198
/
