set term postscript portrait colour enhanced  solid "Helvetica" 20
set border 3; set noxtics;set ytics nomirror;set xtics nomirror
set lmargin 12
set output 'memsvar.eps'
set size 0.95,0.45

set key right center

unset surface
unset ztics

set noxtics
set xtics nomirror

set xtics ("0.83"0.83,"0.86".86, "0.89".89, "0.92".92, "0.95".95, "0.98".98,"1"1)

set xlabel "{/Symbol g}"
set ylabel 

plot [0.828:1]  "memsvar.dat" u 1:(0-$3) t "" w l
