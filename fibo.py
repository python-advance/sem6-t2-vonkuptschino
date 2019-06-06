from itertools import tee

def fibo():
     a, b = 0, 1
     while True:           
         yield a            
         a, b = b, a + b
max_numb = 100
for i, f in zip(range(max_numb), fibo()):
      print('{i:3}: {f:3}'.format(i=i+1, f=f))
          

def recur_fibo():
    yield 0
    yield 1
    f, tf = tee(recur_fibo()) 
    next(tf)
    for a, b in zip(f, tf):
        yield a + b
for i, f in zip(range(max_numb), recur_fibo()):
     print('{i:3}: {f:3}'.format(i=i+1, f=f))
 
