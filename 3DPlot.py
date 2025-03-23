from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import PotentialFields as pf
import config
import Geometrie

config.target_x, config.target_y = 0,0
config.center = (-5, 5)
config.radius = 5
config.rho_0 = 15
config.k = 1
 
# defining surface and axes
#x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
#y = x.copy().T
x = np.linspace(-15, 15, 30)
y = np.linspace(-15, 15, 30)
  
X, Y = np.meshgrid(x, y)

#Z = pf.u_att_function((x, y), (config.target_x, config.target_y), 1)
 
# Calculate Z values (potential field) for each (x, y) position in the meshgrid
Z = np.zeros_like(X)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        pos_ee = (X[i, j], Y[i, j])
        #rho_b = Geometrie.distance_to_circle(config.center, config.radius, pos_ee)
        rho_b = Geometrie.distance_to_circle(config.center, config.radius, pos_ee)
        if(rho_b <= 0):
            Z[i, j] = 30
        #Z[i, j] =np.linalg.norm(pf.v_att_function(pos_ee, (config.target_x, config.target_y), config.zeta))# - pf.v_rep_function(pos_ee, config.rho_0, config.k)
        else:
            Z[i, j] =np.linalg.norm(pf.v_att_function(pos_ee, (config.target_x, config.target_y), config.zeta))*1.5 + np.linalg.norm(pf.v_rep_function(pos_ee, config.rho_0, config.k))*10000
            #Z[i, j] =np.linalg.norm(pf.v_rep_function(pos_ee, config.rho_0, config.k)) * 1000
            #print(f"Z wert = {Z[i, j]}, i = {i}, j = {j}")
            if(Z[i, j] > 30):
                Z[i, j] = 30


fig = plt.figure()
 
# syntax for 3-D plotting
ax = plt.axes(projection='3d')
 
# syntax for plotting
ax.plot_surface(X, Y, Z, cmap='viridis',\
                edgecolor='green')
#ax.set_title('Surface plot geeks for geeks')
#plt.savefig("./PDF_Figures/RepPF3D.pdf", bbox_inches='tight')
plt.show()