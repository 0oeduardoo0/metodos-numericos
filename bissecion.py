import sys
import json
from tabulate import tabulate
from bissecion import functions as bs

file = open(sys.argv[1])
params = file.read()
file.close()

params = json.loads(params)

left, right, step = params['interval'].split(',')
bs.set_interval(float(left), float(right), float(step))

bs.function = params['function']

bs.min_error_percent = float(params['min_error_percent'])

print "\n ~ Tabla de intervalos"
bs.eval_f(True)

print " ~ Raiz entre los puntos [%s, %s] " % (bs.get_a_b())

try:
   roots = bs.bissec()
   print tabulate(roots, headers=['Punto', 'Porcentaje de error'], tablefmt="fancy_grid")

   bs.plot()

except:
   print "La raiz tomaria mucho tiempo en ser encontrada D:"