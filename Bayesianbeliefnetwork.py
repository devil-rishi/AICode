import numpy as np

P_C = np.array([0.5, 0.5])
P_S_given_C = np.array([[0.5, 0.5], [0.1, 0.9]])  
P_R_given_C = np.array([[0.8, 0.2], [0.2, 0.8]])  
P_W_given_SR = np.array([
    [[1.0, 0.1], [0.1, 0.01]],  
    [[0.0, 0.9], [0.9, 0.99]]   
])

def joint_prob(C, S, R, W):
    P = P_C[C] * P_S_given_C[C][S] * P_R_given_C[C][R] * P_W_given_SR[W][S][R]
    return P

def marginalize(C_evidence):
    P_wet_grass_given_cloudy = np.zeros(2)
    for S in [0, 1]:
        for R in [0, 1]:
            for W in [0, 1]:
                jp = joint_prob(C_evidence, S, R, W)
                P_wet_grass_given_cloudy[W] += jp
    P_wet_grass_given_cloudy /= np.sum(P_wet_grass_given_cloudy)
    return P_wet_grass_given_cloudy

P_W_given_C1 = marginalize(C_evidence=1)
print(f"p(W=0 | C=1) = {P_W_given_C1[0]:.4f}")
print(f"p(W=1 | C=1) = {P_W_given_C1[1]:.4f}")
