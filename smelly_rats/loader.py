import pandas as pd


def load_smelly_rats(path):
    """
    Load the smelly rats data.

    Parameters
    ----------
    path : string
        Path to excel file.

    Returns
    -------
    (pd.DataFrame, pd.DataFrame) : The (hnmr spectra, target) data frames.
    """
    xl = pd.ExcelFile(path)

    hnmr_spectra = (
        pd.read_excel(xl, sheet_name=0, index_col=0)
        .rename(columns=lambda col: col.replace("'", ""))
    )

    target = pd.read_excel(xl, sheet_name=1, usecols=range(10, 15))

    return hnmr_spectra, target
