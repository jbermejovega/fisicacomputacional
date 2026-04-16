set term postscript colour portrait enhanced  solid "Helvetica" 20
set key right top
set border 3; set noxtics;set ytics nomirror;set xtics nomirror
set output "ldf_g_q.eps"
set size 0.95,0.5

unset surface
unset ztics

set ylabel "G (q) (10^{-4})"
set xlabel "q (10^{-4})"

set label "laser on" at (-0.00027),(-0.0001)
set label "laser off" at (-0.0005),(-0.000027)

set xtics ("-5" -0.0005,"-4" -0.0004,"-3" -0.0003, "-2" -0.0002, "-1"-0.0001, "0"0)
set ytics ("-1.5" -0.00015,"-1" -0.0001,"-0.5" -0.00005,"0" 0) 

plot [:0][:0.00001]  "ldf2_off_left.txt"  t "" w l lw 3 lc 1, "ldf2_off_right.txt" t "" w l lw 3 lc 1,   "ldf2_on.txt" t "" w l lt 5 lc 3 lw 3
