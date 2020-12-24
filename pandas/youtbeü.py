import pandas as pd
import numpy as np


data=pd.read_csv("US.csv")



result=data

result=result.columns


#result=data[5:15].head()

result=len(result)


result=data.drop(["description"],axis=1)

result=data["likes"].mean()
result=data["dislikes"].head(10).mean()


result=data.head(50)[["title","likes","dislikes"]]

result=data[data["views"].max()==data["views"]][["title"]].iloc[0]


result=data[data["views"].min()==data["views"]]["title"].iloc[0]

result=data.sort_values(["views"]).head()[["title","likes"]]

result=data.groupby("category_id").mean()["likes"]

result=data.groupby("category_id").mean().sort_values("likes",ascending=False)["likes"]


result=data["category_id"].value_counts()





a=[]
def pop(datas):
    likes_list=list(datas["likes"].head())
    dislikes_list=list(datas["dislikes"].head())

    liste=list(zip(likes_list,dislikes_list))

    oran=[]

    for like,dislike in liste:
        if (like+dislike)==0:
            oran.append(0)
        else:
            oran.append(like/(like+dislike))
            
        return oran

result["beğeni"]=pop(data)
print(data.sort_values("beğeni"),ascending=False)[["title","likes"]]

