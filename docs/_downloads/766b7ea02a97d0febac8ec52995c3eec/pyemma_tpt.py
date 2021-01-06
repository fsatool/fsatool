from msmtools.flux import tpt
import numpy as np
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

tpm = np.loadtxt("tpm.txt")
tptobj = tpt(tpm, [100100], [10])

data = {}
data['forward committor'] = tptobj.forward_committor.tolist()
data['backward committor'] = tptobj.backward_committor.tolist()
data['pi'] = tptobj.stationary_distribution.tolist()
data['totalflux'] = tptobj.total_flux.tolist()
data['pathways'] = tptobj.pathways()[0]
data['flux'] = tptobj.pathways()[1]

with open('pyemma_tpt_save.json', 'w') as f:
    for item in data.items():
        f.write(json.dumps(item, cls=NumpyEncoder))
        f.write("\n")
