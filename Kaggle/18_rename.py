import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col = 0)

renamed = reviews.rename(columns={'points':'score'})  #Rename points with score
print(renamed)

reindexed = reviews.rename_axis('entries')  #Change index with entries
print(reindexed)

index_rename = reviews.rename(index={0:'first entry', 1:'second entry'})  #Change 0 index with first entry & 1st with second entry
print(index_rename)

renamed_index = reviews.rename_axis("wines", axis='index').rename_axis("fields", axis='columns')
print(renamed_index)
