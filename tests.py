from random import random, seed
from time import perf_counter, time
import matplotlib.pyplot as plt
import numpy as np

from UndirectedRobertsFlores import UndirectedRobertsFlores
from DirectedRobertsFlores import DirectedRobertsFlores
from UndirectedFleury import UndirectedFleury
from DirectedFleury import DirectedFleury

# adjustable
max_nodes = 20
density = [i/10 for i in range(1, 10)]
nodes = [i for i in range(10, max_nodes+1)]
n_tries = 1
seed(time())

def create_adjacency_matrix(class_, n, d):
    obj = class_()
    obj.v = n
    e = 0

    G = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            if random() < d:
                G[i][j] = G[j][i] = 1
                e += 1

    obj.e = e
    obj.am = G

    return obj


def create_graph_matrix(class_, n, d):
    obj = class_()
    obj.v = n
    e = 0

    ln = [[] for _ in range(n)]
    lp = [[] for _ in range(n)]
    lb = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            if random() < d:
                ln[i].append(j)
                lp[j].append(i)
                e += 1

    obj.e = e
    obj.create_gm(ln, lp, lb)

    return obj


times_urf = [[[] for _ in density] for _ in nodes]
times_uf = [[[] for _ in density] for _ in nodes]
times_drf = [[[] for _ in density] for _ in nodes]
times_df = [[[] for _ in density] for _ in nodes]

for num_n, n in enumerate(nodes):
    print(n)
    for num_d, d in enumerate(density):
        for _ in range(n_tries):
            URF = create_adjacency_matrix(UndirectedRobertsFlores, n, d)
            start = perf_counter()
            URF.find()
            times_urf[num_n][num_d].append(perf_counter() - start)

            UF = create_adjacency_matrix(UndirectedFleury, n, d)
            start = perf_counter()
            UF.find()
            times_uf[num_n][num_d].append(perf_counter() - start)

            DRF = create_graph_matrix(DirectedRobertsFlores, n, d)
            start = perf_counter()
            DRF.find()
            times_drf[num_n][num_d].append(perf_counter() - start)

            DF = create_graph_matrix(DirectedFleury, n, d)
            start = perf_counter()
            DF.find()
            times_df[num_n][num_d].append(perf_counter() - start)

density_mesh, nodes_mesh = np.meshgrid(density, nodes)


times_urf = np.array(times_urf)
mean_times_urf = np.mean(times_urf, axis=2)
std_times_urf = np.std(times_urf, axis=2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(density_mesh, nodes_mesh, mean_times_urf,
                cmap='viridis', label='Undirected Roberts-Flores')
ax.errorbar(density_mesh.flatten(), nodes_mesh.flatten(), mean_times_urf.flatten(),
            yerr=std_times_urf.flatten(), fmt='.', color='black', label='Std Dev')

ax.set_title('Undirected Roberts-Flores')
ax.set_xlabel('Density')
ax.set_ylabel('Number of Nodes')
ax.set_zlabel('Compute Time (s)')

plt.savefig('figures/UndirectedRobertsFlores.png')
plt.show()


times_uf = np.array(times_uf)
mean_times_uf = np.mean(times_uf, axis=2)
std_times_uf = np.std(times_uf, axis=2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(density_mesh, nodes_mesh, mean_times_uf,
                cmap='viridis', label='Undirected Fleury')
ax.errorbar(density_mesh.flatten(), nodes_mesh.flatten(), mean_times_uf.flatten(),
            yerr=std_times_uf.flatten(), fmt='.', color='black', label='Std Dev')

ax.set_title('Undirected Fleury')
ax.set_xlabel('Density')
ax.set_ylabel('Number of Nodes')
ax.set_zlabel('Compute Time (s)')

plt.savefig('figures/UndirectedFleury.png')
plt.show()


times_drf = np.array(times_drf)
mean_times_drf = np.mean(times_drf, axis=2)
std_times_drf = np.std(times_drf, axis=2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(density_mesh, nodes_mesh, mean_times_drf,
                cmap='viridis', label='Directed Roberts-Flores')
ax.errorbar(density_mesh.flatten(), nodes_mesh.flatten(), mean_times_drf.flatten(),
            yerr=std_times_drf.flatten(), fmt='.', color='black', label='Std Dev')

ax.set_title('Directed Roberts-Flores')
ax.set_xlabel('Density')
ax.set_ylabel('Number of Nodes')
ax.set_zlabel('Compute Time (s)')

plt.savefig('figures/DirectedRobertsFlores.png')
plt.show()


times_df = np.array(times_df)
mean_times_df = np.mean(times_df, axis=2)
std_times_df = np.std(times_df, axis=2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(density_mesh, nodes_mesh, mean_times_df,
                cmap='viridis', label='Directed Fleury')
ax.errorbar(density_mesh.flatten(), nodes_mesh.flatten(), mean_times_df.flatten(),
            yerr=std_times_df.flatten(), fmt='.', color='black', label='Std Dev')

ax.set_title('Directed Fleury')
ax.set_xlabel('Density')
ax.set_ylabel('Number of Nodes')
ax.set_zlabel('Compute Time (s)')

plt.savefig('figures/DirectedFleury.png')
plt.show()
