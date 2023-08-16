'''
load one characteristic particle data in snapshot
constrain_mask of density and temperature in swiftsimio doesn't work.
'''

import swiftsimio as sw
import numpy as np

# load snapshot data
def WHIM_snapshot_subset():
    # input parameters
    reds = 0.1
    sim = 'L1000N1800'
    snapnum = int(77-reds/0.05)

    filename = f'/cosma8/data/dp004/flamingo/Runs/{sim}/HYDRO_FIDUCIAL/snapshots/flamingo_00{snapnum}/flamingo_00{snapnum}.hdf5'
    mask = sw.mask(filename)
    boxsize = mask.metadata.boxsize
    load_region = [[0.0 * b, 0.001 * b] for b in boxsize]
    mask.constrain_spatial(load_region)

    density_units = mask.units.mass / mask.units.length**3
    temperature_units = mask.units.temperature
    mask.constrain_mask("gas", "density", 100 * density_units, 1e4 * density_units)
    mask.constrain_mask("gas", "temperature", 1e5 * temperature_units, 1e7 * temperature_units)

    data = sw.load(filename, mask=mask)

    return data

dat = WHIM_snapshot_subset()
from IPython import embed
embed()