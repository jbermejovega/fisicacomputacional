from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

np.random.seed(1000 + rank)

N_local = 128

q = np.random.randn(N_local, 3)
p = np.random.randn(N_local, 3)

print(f'rank={rank} systems={N_local}')

flux_local = np.sum(np.linalg.norm(q, axis=1) < 0.5)
flux_total = comm.reduce(flux_local, op=MPI.SUM, root=0)

if rank == 0:
    print('GLOBAL FLUX:', flux_total)
