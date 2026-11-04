#Kensi and Autumn
import matplotlib.pyplot as plt
from plotting_fxns import *
ls=[]
fh=open("StudentExercise.csv")
next(fh)
for line in fh:
    words=line.split(",")
    exercise=words[0]
    if exercise != '':
        exercise=float(exercise)
        ls.append(exercise)
def histo(ls):
    plt.hist(ls,5)
    plt.ylabel('y-axis')
    plt.title('Letters')
    plt.show()
histo(ls)
def average(ls):
    i=0
    s=0
    count=0
    for number in ls:
        s=s+number
        count += 1
    return (s/count)
print(average(ls))
def prob_above(ls):
    a=average(ls)
    count=0
    for student in ls:
        if student > a:
            count += 1
    return count/len(ls)
print(prob_above(ls))
def median(ls):
    ls.sort()
    order=ls
    x=len(order)
    if len(order) % 2 == 0:
        upper=order[(int(x/2))]
        lower=order[(int(x/2-1))]
        average=upper+lower/2
    else:
        average=order[(int(x/2))]
    return average
print(median(ls))
        
        
