import pytraj as pj
import numpy as np
import re
import os
import subprocess
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Given the amber trajectory of a cluster, draw"
                                                 "the picture of the molecule")
    parser.add_argument("trajectory", metavar="traj", type=str, help="Amber Trajectory")
    parser.add_argument("prmtop", metavar="top", type=str, help="Amber Topology file")

    args=parser.parse_args()
    inputfile = args.trajectory
    topfile = args.prmtop
    traj = pj.load(inputfile, top=topfile)
    len_traj = len(traj)
    rmsd_matrix = np.zeros((len_traj, len_traj))
    for i in range(len_traj):
        rmsd_matrix[i, i+1:] = pj.rmsd(traj=traj, mask="nucleic",
                                    ref=i, frame_indices=np.arange(i+1,len_traj))
        rmsd_matrix[i+1:, i] = rmsd_matrix[i, i+1:]

    index = np.argmin(np.mean(rmsd_matrix, axis=1))
    with open("allign.tcl","r") as f:
        s = f.read()
        s = re.sub("need_to_decide", str(index), s)
        s = re.sub("mdcrdfile", inputfile, s)
        a = open("allign_temp.tcl", "w")
        a.write(s)
        a.close()

    subprocess.run("vmd -e allign_temp.tcl", shell=True)
    os.remove("allign_temp.tcl")
