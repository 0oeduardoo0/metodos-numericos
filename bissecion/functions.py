from numpy import sin
from numpy import cos
from numpy import arange
from tabulate import tabulate
import matplotlib.pyplot as plt

function = None
interval = None
interval_source = None
results  = None
min_error_percent = 1
a = None
b = None
root = None

def f(x):
   global function
   return eval(function)

def eval_f(print_table):
   global function
   global interval
   global results

   results = []
   table = []

   for x in interval:
      result = f(x)
      results.append(result)
      table.append([x,result])
      
   if print_table:
      print tabulate(table, headers=['x', 'f(x) = ' + function], tablefmt="fancy_grid")
      print ""

def set_interval(_from, _to, step_length):
   global interval
   global interval_source

   interval_source = [_from, _to, step_length]

   step = _from
   interval = []

   while step <= _to:
      interval.append(step)
      step += step_length

def plot():
   global root
   global interval
   global interval_source
   global results
   global function

   interval = arange(interval_source[0], interval_source[1], 0.05)
   eval_f(False)

   plt.plot(interval, results)
   
   plt.annotate('raiz', xy=(root[0], root[1]), xytext=(root[0] + 0.5, root[1] + 0.5), arrowprops=dict(facecolor='black', shrink=0.05),)

   plt.grid(True)
   plt.title(function)
   plt.ylabel('f(x)')
   plt.xlabel('x')
   plt.show()

def get_a_b():
   global interval
   global results
   global a
   global b

   a = results[0]

   count = 1

   for result in results:
      if (result >= 0 and a < 0) or (result < 0 and a >= 0):
         a = interval[count - 2]
         b = interval[count - 1]
         return a, b
      else:
         a = result

      count += 1

def error_percent(xr, a):
   return abs(((xr - a) / xr) * 100)

def bissec():
   global root
   global a
   global b
   global min_error_percent

   roots = []

   xr = (a + b) / 2
   ep = error_percent(xr, a)

   roots.append([xr, str(ep) + "%"])

   if(ep <= min_error_percent):
      root = [xr, 0]
      return roots

   faxr = f(a) * f(xr)

   if faxr > 0:
      a = xr
   else:
      b = xr

   roots.extend(bissec())
   return roots