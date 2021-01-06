#!/bin/bash

#SBATCH -J sim1_read
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
mol=ala
srun --mpi=pmi2 ~/fsatool sim -O -i job.sh -p $mol.top -c $mol.rst -r md.rst -x $mol.traj -ref $mol.rst  > log.txt

&cntrl
 imin=0, ntb=0, igb=8, ntpr=1000, ntwr=10000, ntwx=10000
 ntt=3, tempi = 300.0, temp0 = 300.0, ig=-1, gamma_ln=1.0
 ntf=2, ntc=2, nstlim=100000000, dt=0.002, cut=999.0
/

&task
  ifflood=.true.
/

&flood
  kelvindown=300.0, kelvinup=700.0, exchangestep=500000, biasrep=1, biasexc=1, moviecv=-1
  ss2cv=1,2, ssngrid=60, 60, floodingtime=10.0, fragsstime=1.0
/

&colvar
  cv_type = 'TORSION'
  cv_min=-3.2, cv_max=3.2
  cv_ni = 4
  cv_i= 5, 7, 9, 15   ! phi
/

&colvar
  cv_type = 'TORSION'
  cv_min=-3.2, cv_max=3.2
  cv_ni = 4
  cv_i=  7, 9, 15, 17  ! psi
/

