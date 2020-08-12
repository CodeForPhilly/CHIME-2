"""Fitting routines for approximating distributions with normal distributions.
"""
from typing import Any, Dict, Optional, TypeVar

from gvar import gvar
from numpy import linspace, median, sqrt
from pandas import DataFrame
from scipy.optimize import curve_fit
from scipy.stats import beta, gamma, norm

from ._typing import (
    FloatLikeArray,
    FloatOrDistVar,
    NormalDistVar,
    ScipyContinuousDistribution,
)


def fit_norm_dist_to_ens(
        x: FloatLikeArray, thresh: Optional[float] = None
) -> NormalDistVar:
    """Approximate ensemble (random vector) by normal distribution.

    If a thresh hold is specified, infer how much results deviate from
    median and remove outliers exceeding the standard score.
    """
    if thresh:
        d = sqrt((x - median(x)) ** 2)
        mod_z_score = 0.6745 * d / median(d)
        x = x[mod_z_score < thresh]

    return gvar(*norm.fit(x))


def fit_norm_dist_to_dist(dist: ScipyContinuousDistribution) -> NormalDistVar:
    """Approximates distribution by normal distribution
    """
    x = linspace(dist.ppf(0.01), dist.ppf(0.99), 100)
    y = dist.pdf(x)
    mu, var = dist.stats(moments="mv")
    mu, std = curve_fit(norm.pdf, xdata=x, ydata=y, p0=(mu, sqrt(var)))[0]

    return gvar(mu, std)


def parse_dist(data: Dict[str, Any]) -> ScipyContinuousDistribution:
    """Parses prior frame data to distribution
    """
    distribution = data["distribution"]
    if distribution == "beta":
        dist = beta(a=data["p1"], b=data["p2"])
    elif distribution == "gamma":
        dist = gamma(a=data["p1"], scale=data["p2"])
    elif distribution == "normal":
        dist = norm(loc=data["p1"], scale=data["p2"])
    elif distribution == "constant":
        dist = data["base"]
    else:
        raise KeyError(
            "Distribution {distribution} not implemented.".format(
                distribution=distribution
            )
        )
    return dist


def gv_to_dist(normal: NormalDistVar) -> ScipyContinuousDistribution:
    """Converts gvar to scipy dist
    """
    return norm(loc=normal.mean, scale=normal.sdev)


def fit_norm_to_prior_df(prior_df: DataFrame) -> Dict[str, FloatOrDistVar]:
    """Read priors DataFrame (`params.csv`) returning fitted normal variables.
    """
    priors = {}
    for _, row in prior_df.iterrows():
        dist = parse_dist(row)
        priors[row["param"]] = (  # account for constant dist
            dist if isinstance(dist,
                               float) else fit_norm_dist_to_dist(dist)
        )

    return priors
