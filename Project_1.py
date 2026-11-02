#Kensi and Autumn
ls=[]
fh=open("StudentExercise.csv")
next(fh)
for line in fh:
    words=line.split(",")
    exercise=words[0]
    if exercise != '':
        exercise=float(exercise)
        ls.append(exercise)
   
print(ls)
        
