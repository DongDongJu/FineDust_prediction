call "common.gnuplot"

set zeroaxis
set yrange [0:]
set xlabel "cores" font "arial,15"
set ylabel "Speed-up" font "arial,15"
set ytics format " %.0s%c" font "arial,15"
set xtics  font "arial,15"
set title font "arial,15"
set term eps
set output 'PARSEC.eps'
set key at graph 0.35,0.85
#set linetype 1 lw 12 lc rgb '#ff0000'
set font  "arial,15"



plot \
"./data/blackscholes.txt2" every :::0::0 with lp title "blackscholes",\
"./data/bodytrack.txt2" every :::0::0 with lp title "bodytrack",\
"./data/canneal.txt2" every :::0::0 with lp title "canneal",\
"./data/dedup.txt2" every :::0::0 with lp title "dedup",\
"./data/ferret.txt2" every :::0::0 with lp title "ferret",\
"./data/freqmine.txt2" every :::0::0 with lp title "freqmine",\
"./data/raytrace.txt2" every :::0::0 with lp title "raytrace",\
"./data/swaptions.txt2" every :::0::0 with lp title "swaptions",\
"./data/streamcluster.txt2" every :::0::0 with lp title "streamcluster"

