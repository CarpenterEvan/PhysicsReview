import numpy as np
import matplotlib.pyplot as plt
def get_phi(M,target):
    N = M+1
    dx = 1.0
    x = np.zeros(N)
    phi = np.zeros([N,N],float)
    phiprime = np.empty([N,N],float)
    for i in range(N):
        phi[i,-1] = 1
        phi[i, 0] = 0
        phi[0, i] = (i/M)**2
        phi[-1,i] = (i/M)**4-(i/M)**2+i/M
        x[i] = i
    while dx > target:
        for i in range(N):
            for j in range(N):
                if i==0 or i== M or j==0 or j==M:
                    phiprime[i,j] = phi[i,j]
                else: 
                    phi[i,j] = 0.25*(phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1])
        dx = np.max(np.abs(phi-phiprime))
        phi,phiprime = phiprime,phi
    return x,phi

M,target = 20, 1e-8
x,phi = get_phi(M, target)
fig,ax = plt.subplots(1,1)
fig.colorbar(ax.contourf(x/M,x/M,phi))
plt.title("$\phi(x,y)$", fontsize=15)
plt.xlabel("x", fontsize=15)
plt.ylabel("y", fontsize=15)
plt.show()