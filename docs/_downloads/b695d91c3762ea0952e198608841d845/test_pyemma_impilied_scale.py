import pyemma.msm as msm
import numpy as np

data = np.loadtxt("tram_for_check.dat", dtype=np.int)
data = data-1
_, index = np.unique(data[:,1], return_index=True)
traj = np.split(data[:,0], index[1:])
#print(traj)
filedata=np.ascontiguousarray(traj)
mits= msm.its(traj,[15,20,25,30,35,40,45,50,55,60] , nits=4, reversible=True)
#print(np.log(mits.get_timescales()))
np.savetxt("pyemma_impliled_timescale.txt", np.log(mits.get_timescales()))
