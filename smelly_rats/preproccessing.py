import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted, check_array


def pareto_scaling(series: pd.Series) -> pd.Series:
    """
    Pareto scale the series. According to the paper (see src) pareto scaling is
    dividing the series by the square root of the standard deviation of the
    values of the series.

    Parameters
    ----------
    series : pd.Series
        The series to be scaled.

    Returns
    -------
    pd.Series : Pareto scaled column.

    TODO
    ----
    Make a `sklearn` transfromer from this function.

    Src:
    H. Winning, E. Roldan-Marin, L.O. Dragsted, An exploratory NMR
    nutri-metabonomic investigation reveals dimethyl sulfone as a dietary
    biomarker for onion intake.  September 2009
    """
    return series / np.sqrt(np.std(series))


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
        self.scaling_factors_ = np.sqrt(X.std(axis=1))
        return self

    def transform(self, X, y=None):
        """Scales the data """
        check_is_fitted(self, ['scaling_factors_'])
        check_array(X, estimator=self)

        if X.shape[0] != len(self.scaling_factors_):
            raise ValueError(
                f'Unexpected input dimension {X.shape[1]}, expected '
                f'{len(self.scaling_factors_)}'
            )

        return (X.T / self.scaling_factors_).T
