import pandas

squirrel_df = pandas.read_csv("./2018_Central_Park_Squirrel_Census.csv")
# black_count = len(squirrel_df.groupby(["Primary Fur Color"]).indices["Black"])
# gray_count = len(squirrel_df.groupby(["Primary Fur Color"]).indices["Gray"])
# cinnamon_count = len(squirrel_df.groupby(["Primary Fur Color"]).indices["Cinnamon"])

# new_df = pandas.DataFrame({
#     "Fur Color" : ["Black", "Gray", "Cinnamon"],
#     "Count" : [black_count,gray_count,cinnamon_count]
#     }
# )

# print(new_df)

count_series = squirrel_df["Primary Fur Color"].value_counts()

new_df = pandas.DataFrame({"fur color" : count_series.index, "count" : count_series.values})

new_df.to_csv("./count_data.csv")