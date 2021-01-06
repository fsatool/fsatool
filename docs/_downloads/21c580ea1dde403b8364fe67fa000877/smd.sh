for ((i=1;i<=100;i=i+1))
do

cat > smd_$i.in << EOF

&cntrl
 ! irest=1, ntx=5,
 imin=0, ntb=0, igb=6,
 ntpr=10000, ntwr=1000000, ntwx=2000000, 
 ntt=3, tempi = 300.0, temp0 = 300.0, ig=-1, gamma_ln=10,
 ntf=1, ntc=1,
 nstlim=110000000, dt=0.001,
 cut=999.0,
 jar=1,
 /
 &wt type='DUMPFREQ', istep1=10000, /
 &wt type='END', /
 DISANG=dist.RST
 DUMPAVE=dist_vs_t_$i
 LISTIN=POUT_$i
 LISTOUT=POUT_$i

EOF

done
