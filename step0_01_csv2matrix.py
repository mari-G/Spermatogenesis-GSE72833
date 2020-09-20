import os 

work_path = os.getcwd()
csv_file_path = work_path + "/*.csv"

from glob import glob 

totle_csv = glob(csv_file_path)
total_csv_list = [i.split(work_path + "\\")[-1].split(".csv")[0] for i in totle_csv]

# print(total_csv_list)
# print(len(total_csv_list))
# print(work_path)
import pandas as pd 
from pandas import DataFrame

matrix_df = pd.read_table("GSE72833_GeneExpressionTPM.txt", index_col= 0, header= 0, sep="\t", usecols=[0])
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

for csv_file in total_csv_list:
    csv2pd(csv_file)


matrix_df.dropna(axis=0, how="all", inplace=True)
matrix_df = matrix_df.fillna(0)
# matrix_df.iloc[~(matrix_df == 0).all(axis= 1), :] fail
# print(matrix_df)
matrix_df.to_csv("matrix.csv")

def classification_csv():
    classification_df = pd.DataFrame(index= total_csv_list)
    classification_df["sample"] = total_csv_list
    classification_df["day_stage"] = total_csv_list
    classification_df["stage"] = classification_df["day_stage"].map(lambda x: x.split(r"_")[1])
    classification_df.to_csv("classification.csv")

classification_csv()
