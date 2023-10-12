school={'Boys':[70,40,58,43,11],'Girls':[67,54,45,34,10]}

li4=[]
for i in range(0,len(school['Boys'])):
    li4.append({'Boys':school['Boys'][i],'Girls':school['Girls'][i]})
print(li4)
