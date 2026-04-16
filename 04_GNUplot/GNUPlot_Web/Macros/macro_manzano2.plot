set term postscript colour portrait enhanced  "Helvetica" 20
set key right top
set border 3; set noxtics;set ytics nomirror;set xtics nomirror
set lmargin 8
set output 'heat_classical_temp.eps'
set size 0.75,0.45
unset surface
unset ztics

set xtics ("0"0, "10"10,"20"20,"30"30,"40"40,"50"50)
set ytics ("1"0.0001,"2"0.0002,"3"0.0003,"4"0.0004,"5"0.0005,"6"0.0006,"7"0.0007,"8"0.0008,"9"0.0009)

set xlabel "T_1"
set label "10^{-4}J" at (-16),(0.0006)

set line style 1 lt 1 lw 3
set line style 2 lt 7 lw 3
set line style 3 lt 3 lw 3

plot [.1:50][:] "heat-classic-temp.dat" u 1:2 t "N=2000" w l ls 1, "heat-classic-temp.dat" u 1:3 t "N=1000" w l ls 7, "heat-classic-temp.dat" u 1:4 t "N=500" w l ls 3