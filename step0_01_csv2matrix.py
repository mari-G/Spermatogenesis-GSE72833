# import os 

# work_path = os.getcwd()
# csv_file_path = work_path + "/*.csv"

# from glob import glob 

# totle_csv = glob(csv_file_path)
# total_csv_list = [i.split(work_path + "\\")[-1].split(".csv")[0] for i in totle_csv]

# print(total_csv_list)
# print(len(total_csv_list))
# print(work_path)
import pandas as pd 
from pandas import DataFrame

matrix_df = pd.read_excel("index_by_stage.xlsx", index_col= 0, header= 0, sep="\t", usecols=[0])
# print(matrix_df)
# print(matrix_df.index.is_unique) # True
# print(matrix_df)

def csv2pd(csv_file):
    global csv_df
    global matrix_df
    csv_path = csv_file + ".csv"
    csv_df= pd.read_csv(csv_path, index_col= 0, header= 0,names= [csv_file])
    # print(csv_df)
    matrix_df = matrix_df.join(csv_df)
    # print(matrix_df)

# csv2pd("day16_EP+LP+D")
# print(csv_df)


total_csv_list = ["day8_Sp'gonia", "day10_Sp'gonia", "day12_Sp'gonia", "day14_Sp'gonia", "day16_Sp'gonia", "day18_Sp'gonia", "day8_PL", "day10_PL", "day12_PL", "day14_PL", "day16_PL", "day18_PL", "day8_EL", "day10_EL", "day12_EL", "day14_EL", "day16_EL", "day18_EL", "day8_LL+Z", "day10_LL+Z", "day12_LL+Z", "day14_LL+Z", "day16_LL+Z", "day18_LL+Z", "day8_LL+Z+EP", "day10_LL+Z+EP", "day12_LL+Z+EP", "day14_LL+Z+EP", "day16_LL+Z+EP", "day18_LL+Z+EP", "day8_EP", "day10_EP", "day12_EP", "day14_EP", "day16_EP", "day18_EP", "day8_EP+LP+D", "day10_EP+LP+D", "day12_EP+LP+D", "day14_EP+LP+D", "day16_EP+LP+D", "day18_EP+LP+D", "day8_LP+D", "day10_LP+D", "day12_LP+D", "day14_LP+D", "day16_LP+D", "day18_LP+D"]

for csv_file in total_csv_list:
    csv2pd(csv_file)


matrix_df.dropna(axis=0, how="all", inplace=True)
matrix_df = matrix_df.fillna(0)
# matrix_df.iloc[~(matrix_df == 0).all(axis= 1), :] fail
# print(matrix_df)
matrix_df.to_csv("matrix.csv")

# def classification_csv():
#     classification_df = pd.DataFrame(index= total_csv_list)
#     classification_df["sample"] = total_csv_list
#     classification_df["day_stage"] = total_csv_list
#     classification_df["stage"] = classification_df["day_stage"].map(lambda x: x.split(r"_")[1])
#     classification_df.to_csv("classification.csv")

# classification_csv()
