import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.utils.validation import check_array


def _check_if_pandas_dataframe(X, *, name='X'):
    """Raises TypeError if `X` is not a `pd.DataFrame`."""
    if not isinstance(X, pd.DataFrame):
        raise TypeError(
            f"Provided variable {name} is not of type pandas.DataFrame.")


class ParetoTransformer(TransformerMixin):
    """"
    Applies Pareto scaling.

    According to Winning et al. (2009) pareto scaling is dividing a vector by
    the square root of the standard deviation of the values in the vector.

    References
    ----------
    H. Winning, E. Roldan-Marin, L.O. Dragsted, An exploratory NMR
    nutri-metabonomic investigation reveals dimethyl sulfone as a dietary
    biomarker for onion intake. The Royal Society of Chemistry, p. 2346.
    September 2009
    """

    def fit(self, X, y=None):
        """Computes the scaling factors."""
        check_array(X, estimator=self)
        return self

    def transform(self, X, y=None):
        """Scales the data """
        check_array(X, estimator=self)

        scaling_factors = np.sqrt(X.std(axis=1))
        return (X.T / scaling_factors).T

    def __repr__(self):
        return 'ParetoTransformer()'


class ColumnSliceSelector(BaseEstimator, TransformerMixin):
    """
    Select columns based on a slice.

    This is found useful for selecting specifics bands in a multispectral data.

    Parameters
    ----------
    column_slice : slice
        The column slice to select.
    """

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.column_slice = slice(self.start, self.stop)

    def fit(self, X, y=None):
        """
        Checks:

        1. if input is a `pd.DataFrame`;
        3. and if column names are in this data frame.
        """
        _check_if_pandas_dataframe(X, name='X')
        return self

    def transform(self, X):
        """Selects the column according to the given slice."""
        _check_if_pandas_dataframe(X, name='X')
        return X.loc[:, self.column_slice]

    def __repr__(self):
        return (f'ColumnSliceSelector(start={self.start:.3f},'
                f'stop={self.stop:.3f})')
