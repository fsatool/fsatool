import json
from msmtools.analysis.dense.pcca import PCCA
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

tpm = np.loadtxt("tpmlarge.txt")
pccaobj = PCCA(tpm, 10)
data = {}
data['assignment'] = pccaobj.metastable_assignment
data['membership_first_100'] = pccaobj.memberships[:100, :]

with open('pyemma_pcca_save.json', 'w') as f:
    for item in data.items():
        f.write(json.dumps(item, cls=NumpyEncoder))
        f.write("\n")
