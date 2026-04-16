set term gif animate

set key left
set xtics; set ytics;
set output 'planetas.gif'
set size 1,1
#
set yr[-10:10]
set xr[-10:10]

do for [ii=1:628] {plot 'salida.txt' u 1:2 every ::ii::ii w p pt 7 ps 2 lc rgb "yellow" t '','' u 3:4 every ::ii::ii  w p pt 7 ps 1 lc rgb "black"  t '','' every ::ii::ii u 5:6 w p pt 7 ps 1 lc rgb "black"  t '','' every ::ii::ii u 7:8 w p pt 7 ps 1 lc rgb "black"  t '','' every ::ii::ii u 9:10 w p pt 7 ps 1 lc rgb "black"  t '','' every ::ii::ii u 11:12 w p pt 7 ps 1 lc rgb "black"  t '','' every ::ii::ii u 13:14 w p pt 7 ps 1 lc rgb "black"  t ''}