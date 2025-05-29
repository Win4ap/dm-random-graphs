# test_distributions.py
import pytest
import numpy as np
from graph_utils.distributions import (
    generate_exp,
    generate_lognormal,
    generate_normal,
    generate_skewnormal,
)


def test_generate_exp():
    data = generate_exp(1000, lam=1.0)
    assert len(data) == 1000
    assert np.mean(data) == pytest.approx(1.0, rel=0.1)  # E[X] = 1/λ


def test_generate_lognormal():
    data = generate_lognormal(1000, sigma=1.0)
    assert len(data) == 1000
    assert np.mean(np.log(data)) == pytest.approx(0.0, abs=0.1)  # mean of log is 0


def test_generate_normal():
    data = generate_normal(1000, sigma=1.0)
    assert len(data) == 1000
    assert np.mean(data) == pytest.approx(0.0, abs=0.1)
    assert np.std(data) == pytest.approx(1.0, rel=0.1)


def test_generate_skewnormal():
    data = generate_skewnormal(1000, skew=5.0)
    assert len(data) == 1000
    assert np.mean(data) > 0.0  # Положительное skewness сдвигает среднее вправо
