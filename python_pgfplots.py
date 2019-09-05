import numpy as np


def writeVector(fid, npVector, prefix='', fmt='%.8e'):
    """Write (append) numpy vector to a text file for use as PGF tables."""
    np.savetxt(fid, npVector, fmt=fmt, newline=' ',
               header=prefix, comments='')
    fid.write("\n")
