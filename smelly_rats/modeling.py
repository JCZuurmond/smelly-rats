import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.metrics import make_scorer as sklearn_make_score
from sklearn.utils.validation import check_array


def _check_if_pandas_dataframe(X, *, name='X'):
    """Raises TypeError if `X` is not a `pd.DataFrame`."""
    if not isinstance(X, pd.DataFrame):
        raise TypeError(
            f"Provided variable {name} is not of type pandas.DataFrame.")


class ParetoScaler(BaseEstimator, TransformerMixin):
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

    def __init__(self, with_mean=False):
        self.with_mean = with_mean

    def fit(self, X, y=None):
        """Computes the scaling factors."""
        check_array(X, estimator=self)
        return self

    def transform(self, X, y=None):
        """Scales the data """
        check_array(X, estimator=self)

        if self.with_mean:
            X = (X.T - X.mean(axis=1)).T

        scaling_factors = np.sqrt(X.std(axis=1))
        return (X.T / scaling_factors).T

    def __repr__(self):
        return f'ParetoScaler(with_mean={self.with_mean})'


class BandSelector(BaseEstimator, TransformerMixin):
    """
    Select a band (range of columns).

    This is useful for selecting specifics bands in a multispectral data.

    Parameters
    ----------
    start : float
        Start of the band.
    stop : float
        End of the band.
    """

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.column_slice = slice(self.start, self.stop)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        """Selects the column according to the given slice."""
        _check_if_pandas_dataframe(X, name='X')
        return X.loc[:, self.column_slice]

    def __repr__(self):
        return (f'BandSelector(start={self.start}, '
                f'stop={self.stop})')


def make_scorer(*args, **kwargs):
    def _(func):
        return sklearn_make_score(func, *args, **kwargs)
    return _


@make_scorer(greater_is_better=False)
def rmse(y, y_hat):
    y = y.values if hasattr(y, 'values') else y
    return np.sqrt(np.square(y.flatten() - y_hat.flatten()).mean())
