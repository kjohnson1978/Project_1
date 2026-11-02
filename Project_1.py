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
