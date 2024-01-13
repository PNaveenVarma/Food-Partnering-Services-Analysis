import pandas as pd
import regex
import re
import matplotlib.pyplot as plt
import numpy as np
     
data =  pd.read_csv(r'/Users/naveenvarma/Desktop/PDS/final/project-deliverable-2-osu-crackers/data/stillwater/stillwater_dataset.csv', sep=",", index_col=[0])
data.rename(columns = {'rating description':'rating_description'}, inplace = True)
nor =[]
for k in range(len(data.index)):
    info = data.rating_description[k]
    info1 = info.split(' ')
    nor1= info1[len(info1)-2]
    nor.insert(len(nor),nor1)

nor_df = pd.DataFrame(nor)
print()
nor_df.columns = ['No_of_Reviews']
final_df = [data,nor_df]
table = pd.concat(final_df,axis=1,ignore_index = True)
table.columns=['Resturant','Rating_description','Ratings','Cuisine','No_of_Reviews']
table.to_csv(r'/Users/naveenvarma/Desktop/PDS/final/project-deliverable-2-osu-crackers/data/stillwater/final_stillwater.csv',sep='\t',encoding='utf-8')
filtered_data = table[(table.Ratings >= 4.5)]
filtered_data.reset_index(inplace=True)
filtered_data.to_csv(r'/Users/naveenvarma/Desktop/PDS/final/project-deliverable-2-osu-crackers/data/stillwater/stillwater_dataset_filtered.csv',sep='\t',encoding='utf-8')

## need to count how many American key words in the dataset.
count = [0,0,0,0,0,0,0,0]
for i in range(len(table.index)):
    x = re.search("American", table.Cuisine[i])
    if x:
     count[0] = count[0]+1

    x = re.search("Asian", table.Cuisine[i])
    if x:
     count[1] = count[1]+1

    x = re.search("Bakery", table.Cuisine[i])
    if x:
     count[2] = count[2]+1

    x = re.search("Mexican", table.Cuisine[i])
    if x:
     count[3] = count[3]+1

    x = re.search("Chinese", table.Cuisine[i])
    if x:
     count[4] = count[4]+1

    x = re.search("Fast Food", table.Cuisine[i])
    if x:
     count[5] = count[5]+1

    x = re.search("Coffee and Tea", table.Cuisine[i])
    if x:
     count[6] = count[6]+1     

    x = re.search("Sandwich", table.Cuisine[i])
    if x:
     count[7] = count[7]+1  

print(count)

## need to count how many American key words in the dataset.
count1= [0,0,0,0,0,0,0,0]

for j in range(len(filtered_data.index)):
    x = re.search("American", filtered_data.Cuisine[j])
    if x:
     count1[0] = count1[0]+1

    x = re.search("Asian", filtered_data.Cuisine[j])
    if x:
     count1[1] = count1[1]+1

    x = re.search("Bakery", filtered_data.Cuisine[j])
    if x:
     count1[2] = count1[2]+1

    x = re.search("Mexican", filtered_data.Cuisine[j])
    if x:
     count1[3] = count1[3]+1

    x = re.search("Chinese", filtered_data.Cuisine[j])
    if x:
     count1[4] = count1[4]+1

    x = re.search("Fast Food", filtered_data.Cuisine[j])
    if x:
     count1[5] = count1[5]+1

    x = re.search("Coffee and Tea", filtered_data.Cuisine[j])
    if x:
     count1[6] = count1[6]+1     

    x = re.search("Sandwich", filtered_data.Cuisine[j])
    if x:
     count1[7] = count1[7]+1  
print(count1)   

# grouped plot
x = np.arange(8)
width = 0.40
fig,ax= plt.subplots()
# plot data in grouped manner of bar type
rects1 = ax.bar(x - width/2, count, width, label='Total Resturants')
rects2 = ax.bar(x + width/2, count1, width, label='Top Rated Resturants > 4.5')
ax.set_xlabel('Cuisines')
ax.set_ylabel('No of Resturants')
ax.set_title('Comparisons of Cusines after filtering top resutrants based on ratings')
ax.set_xticks(x,['American', 'Asian', 'Bakery', 'Mexican','Chinese','Fast Food','Coffee and Tea','Sandwich'])
ax.legend()
ax.bar_label(rects1,padding=3)
ax.bar_label(rects2,padding=3)
fig.tight_layout()
plt.show()

