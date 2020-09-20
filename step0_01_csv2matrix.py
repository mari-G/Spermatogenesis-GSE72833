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

matrix_df = matrix_df.fillna(0)
# print(matrix_df)
matrix_df.to_csv("matrix.csv")