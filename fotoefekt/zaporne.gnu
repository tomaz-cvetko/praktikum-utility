#!\C:\Program Files\gnuplot\bin

set term pdf enh font ",14"

set out 'fotoefekt_graf.pdf'

set title "Odvisnost U_{max}(f)"

set xlabel 'f [10^{14} Hz]'
set ylabel 'U_{max} [V]'

set key below

f(x) = h*x + A
fit f(x) 'zaporne.dat' u (3e3/$1):2 via h,A
plot [0:][]'zaporne.dat' u (3e3/$1):2 t 'meritve' w p, f(x) t 'linear fit' w l