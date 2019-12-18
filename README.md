# Smelly rats

Replicating - or trying to replicate - a [paper][1] about classifying rats which have
different onion diets.

## Description

The paper uses H+ NMR spectra taken from the urine of rats which have different
levels of onion in their diet. The goal is to classify the diet of the rat with
the spectral data.

These repository implements a couple of the applied analysis in Python:

- [HNMR spectra per diet](notebooks/hnmr-spectra-per-dietary-group.ipynb):
	Implements the average HNMR spectra per dietary group.
- [interval partial least squares](notebooks/interval-partial-least-squares.ipynb)
	Implements interval partial least squares to find the spectral bands with
	which the dietary groups can be classified most correctly.
- [PCA](notebooks/pca-on-spectra.ipynb): Applies PCA to the spectra to look for
	separation of the dietary groups in lower dimensional space.
- [Resampling spectral bands](notebooks/resample-spectral-bands.ipynb):
	Implements a resample method which works on `pandas.FloatIndex` and works
	similar as the `resample` method for `pd.DateTimeIndex` - useful to reduce
	the resolution of the spectral bands.

## Requirements
Python 3 and [see here](setup.py).

## Data
The data can be found [here](http://www.models.life.ku.dk/onionnmr).

## Sources
[1] H. Winning, E. Roldán‐Marín, L.O. Dragsted, N. Viereck, M. Poulsen, C. Sánchez‐Moreno, M.P. Cano, S.B. Engelsen, An exploratory NMR nutri-metabonomic investigation reveals dimethyl sulfone as a dietary biomarker for onion intake, Analyst 2009, 134 (11) 2344-2351
