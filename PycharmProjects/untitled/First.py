__author__ = 'hyw356'
import re
import numpy
from untitled.michaelwicz_function import Michaelwicz_function
from untitled.second import second

My_list= []

for member in dir(re):
    if "find" in member:
        My_list.append(member)


#print sorted(My_list)
MF= Michaelwicz_function()
print ("the result",MF.compute([.5,.6],2))
x = numpy.random.uniform(0,1,4)
xx = numpy.sort(x)
y = numpy.argsort(x)
print (x)
print(xx)
print(y)
x= x[y]
print(x)
xxx = numpy.random.uniform(0,1,4)
print(xxx)
xxx = xxx[y]
print(xxx)
scale = numpy.ones(2) * abs(4 - 0)
print(scale)
a=[[1,2],[3,4]]
b=[[11,3],[13,14]]
print(numpy.multiply(a,b))
print(numpy.random.uniform(0,1,(2,2)))
print(numpy.clip(b, 0, 4))
s= second(40,10,2)
print (s)
#print ("the result",MF.compute([.5,.6],2))
values = numpy.random.uniform(0,1,2)
print (values)
