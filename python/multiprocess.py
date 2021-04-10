#multiprocessing
import multiprocessing
def square(x):
    #print(x)
    for i in range(10,x):
        print(i*i)
def add(x):
    #print(x)
    for i in range(0,x):
        print(i+i)
        
p1=multiprocessing.Process(target=square,args=(20,))
p2=multiprocessing.Process(target=add,args=(10,))

p1.start()
p2.start()
p1.join()
p2.join()

/*
--output--
100
121
144
169
196
225
256
289
324
361
0
2
4
6
8
10
12
14
16
18
*/