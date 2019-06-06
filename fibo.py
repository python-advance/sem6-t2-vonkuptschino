def fibo():
     a, b = 0, 1
     while True:           
         yield a            
         a, b = b, a + b
max_numb = 100
for index, curr_number in zip(range(max_numb), fibo()):
      print('{i:3}: {f:3}'.format(i=index+1, f=curr_number))
