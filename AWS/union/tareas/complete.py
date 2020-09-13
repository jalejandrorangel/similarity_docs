import os
from similitud import *

num_tareas = len(os.listdir()) - 4
name = 'tarea'
for i in range(1,num_tareas+1):
    cal = 0
    for j in range(1, num_tareas+1):
        
        if i == j:
            continue
        a_b = similitud(name+str(i), name+str(j))
        if a_b > cal:
            cal = a_b
        #if a_b > 40 or b_a >40:
        #print("posible plagio entre",name+str(i)+' y '+name+str(j),a_b,b_a )
    print(name+str(i),str(int(cal))+'/100')

