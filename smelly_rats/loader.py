import pandas as pd
import scipy.io


def load_smelly_rats(path):
    """
    Load the smelly rats data.

    Parameters
    ----------
    path : string
        Path to mat file.

    Returns
    -------
    (pd.DataFrame, np.array) : The hnmr spectra and target.
    """
    mat = scipy.io.loadmat(path)
    hnmr_spectra = pd.DataFrame(
        mat['x'].T,
        index=mat['ppm'][0],
        columns=[c[0][0] for c in mat['Samples_name']]
    )

    return hnmr_spectra, mat['onion'].flatten()
