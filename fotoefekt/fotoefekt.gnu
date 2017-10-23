#!\C:\Program Files\gnuplot\bin

set term pdf enh font ",14"

set out 'lambda577.pdf'

set title "Odvisnost I(U_{zap}) pri {/Symbol l}=577nm"

set xlabel 'U[V]'
set ylabel 'I[10^{-12}]'

set key below

f(x) = a*x + b
fit f(x) 'lambda577nm.dat' u 1:2 via a,b
plot 'lambda577nm.dat' t 'meritve' w p, f(x) t 'linear fit' w l