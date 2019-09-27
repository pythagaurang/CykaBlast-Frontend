import pandas as pd

columns=['image','latitude','longitude','depth','width','location','fixed']

potholes=pd.DataFrame(columns=columns)

list=[['image','latitude','longitude','depth','width','location','fixed']]

loc=[[15.526141, 73.966466 ],[15.526226, 73.966562],[15.525828, 73.966401],[15.525823, 73.966457],[15.526162, 73.966556],[15.401246, 74.002902],[15.401234, 74.002933],[15.401089, 74.003062],[15.403073, 74.008132],[15.403040, 74.008056],[15.402678, 74.007713],[15.402637, 74.007563],[15.398516, 74.003073],[15.398515, 74.003051],[15.398396, 74.003020]]
categories=['small','medium','large']
lane=['left','right']
fix=[True,False]
img="image"

columns.index

for i in range(len(loc)):
    j=0
    for column in columns:
        if(j==1 or j==2):
            list[0][j]=loc[i][j-1]
        if(j==0): 
            list[0][j]=img + str(i)
        if(j==3):
            list[0][j]=categories[i%3]
        if(j==4):
            list[0][j]=categories[(i+1)%3]
        if(j==5):
            list[0][j]=lane[i%2]
        if(j==6):
            list[0][j]=fix[i%2]
        j+=1
    potholes=potholes.append(pd.DataFrame(list,columns=columns))

print(potholes.head())

potholes.to_csv('potholes.csv')