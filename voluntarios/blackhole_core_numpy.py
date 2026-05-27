import numpy as np

G = 1.0
EPSILON = 0.05
DT = 1e-3


def softened_acceleration(q, Mbh=100.0):
    r2 = np.sum(q**2)
    denom = (r2 + EPSILON**2)**1.5
    return -G * Mbh * q / denom


def verlet_step(q, p, m):
    a = softened_acceleration(q)
    p_half = p + 0.5 * DT * a
    q_new = q + DT * p_half / m
    a_new = softened_acceleration(q_new)
    p_new = p_half + 0.5 * DT * a_new
    return q_new, p_new


def angular_momentum(q, p):
    return np.cross(q, p)
