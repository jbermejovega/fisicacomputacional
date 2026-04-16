set term gif animate

set key left
set xtics; set ytics;
set output 'plots/ising.gif'
set size 1,1
#

N=40

set yr[0:N-1]
set xr[0:N-1]



do for [i=1:30] {plot for [j=1:N*N] 'plots/ising.txt' u 3*j-2:3*j-1:3*j every ::i::i t "" w p pt 7 lc variable}
