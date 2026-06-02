import numpy as np

def find_critical_load(L, E, A, r, c, e, sigma_allow):

    def stress_difference(P):
        angle = (L / (2 * r)) * np.sqrt(P / (E * A))
        sigma_max = (P / A) * (1 + (e * c / r**2) * (1 / np.cos(angle)))
        return sigma_max - sigma_allow

    P_euler = (np.pi**2 * E * A * r**2) / (L**2)

    low = 0.0
    high = 0.999 * P_euler

    for _ in range(100):
        mid = (low + high) / 2

        if stress_difference(mid) > 0:
            high = mid
        else:
            low = mid

    return (low + high) / 2
