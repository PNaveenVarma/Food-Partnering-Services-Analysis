from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import re
 
rest = pd.read_csv(r'/Users/naveenvarma/Desktop/PDS/final/project-deliverable-2-osu-crackers/data/stillwater/stillwater_dataset.csv', index_col=[0])
print(rest)

cu = rest['cusine'].unique
print(cu)

count = [0,0,0,0,0,0,0,0]
for i in range(len(rest.index)):
    x = re.search("American", rest.cusine[i])
    if x:
     count[0] = count[0]+1

    x = re.search("Asian", rest.cusine[i])
    if x:
     count[1] = count[1]+1

    x = re.search("Bakery", rest.cusine[i])
    if x:
     count[2] = count[2]+1

    x = re.search("Mexican", rest.cusine[i])
    if x:
     count[3] = count[3]+1

    x = re.search("Chinese", rest.cusine[i])
    if x:
     count[4] = count[4]+1

    x = re.search("Sandwich", rest.cusine[i])
    if x:
     count[5] = count[5]+1

    x = re.search("Fast Food", rest.cusine[i])
    if x:
     count[6] = count[6]+1     

    x = re.search("Coffee and Tea", rest.cusine[i])
    if x:
     count[7] = count[7]+1

print(count)

df6=rest['cusine'].unique()
print(df6)


fig = plt.figure(figsize =(7, 5))
plt.pie( count, labels = df6, autopct='%.0f%%')
plt.title('Percentage of different cuisine restaurants in Stillwater')
plt.show()
 


rest[['ratings']] = rest[['ratings']].apply(pd.to_numeric)
b=rest.boxplot(column=['ratings'], by="cusine", patch_artist=True, figsize =(10, 10))
plt.grid(False)
plt.title('Overall ratings of restaurants based on cuisine')
plt.show()

