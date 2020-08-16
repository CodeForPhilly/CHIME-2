# -*- coding: utf-8 -*-
"""
"""
from scipy.stats import beta, gamma
from scipy.optimize import fmin


def gamma_from_q(l, u, quantiles_percent=0.95):
    def loss(params):
        a, b = params
        lq = (1 - quantiles_percent) / 2
        uq = 1 - lq
        return (gamma.cdf(l, a, scale=b) - lq) ** 2 + (
                gamma.cdf(u, a, scale=b) - uq
        ) ** 2

    start_params = (5, 5)
    fit = fmin(loss, start_params, disp=0)
    return fit


def beta_from_q(l, u, quantiles_percent=0.95):
    def loss(params):
        a, b = params
        lq = (1 - quantiles_percent) / 2
        uq = 1 - lq
        return (beta.cdf(l, a, b) - lq) ** 2 + (beta.cdf(u, a, b) - uq) ** 2

    start_params = (1, 1)
    fit = fmin(loss, start_params, disp=0)
    return fit
