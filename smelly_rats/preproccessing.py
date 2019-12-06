import logging
import time
from functools import wraps


def log_step(func):
    logger = logging.getLogger()

    @wraps(func)
    def wrapper(*args, **kwargs):

        tic = time.perf_counter()
        out = func(*args, **kwargs)
        toc = time.perf_counter() - tic

        logger.debug(f'{func.__name__} shape={out.shape} time={toc:.3f}')

        return out
    return wrapper


@log_step
def init(df):
    """Purely functional for `log_step`."""
    return df


@log_step
def resample_spectral_bands(df, bandwidth, agg_func='mean'):
    """
    Resample sepctral bands given some bandwidth.

    Parameters
    ----------
    df : pd.DataFrame
        The data frame with the spectral bands.
    bandwidth : float
        The bandwidth to which to resample.
    agg_func : Union[str, callable] (default: 'mean')
        Aggregate function.

    Returns
    -------
    pd.DataFrame : The data frame with resampled spectral bands.
    """
    s = ((df.index.to_series()) / bandwidth).astype(int)

    resampled_index = (
        s
        .groupby(s)
        .apply(lambda df: df.loc[lambda df: df.index == df.index.max()])
        .reset_index(level=0, drop=True)
    )

    return (
        df
        .groupby(s)
        .agg(agg_func)
        .set_index(resampled_index.index)
    )