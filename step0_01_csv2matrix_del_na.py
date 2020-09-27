import pandas as pd 
from pandas import DataFrame

matrix_df_ori = pd.read_excel("index_by_stage.xlsx", index_col= 0, header= 0, sep="\t", usecols=[0])
# print(matrix_df)
# print(matrix_df.index.is_unique) # True
# print(matrix_df)

matrix_df = matrix_df_ori

def csv2single_pd(csv_file):
    global csv_df
    global stage_df
    csv_path = csv_file + ".csv"
    csv_df= pd.read_csv(csv_path, index_col= 0, header= 0,names= [csv_file])
    csv_df = csv_df[csv_df[csv_file] > 4]
    print(csv_df)
    csv_df.dropna(axis=0, how="any", inplace=True)
    print(csv_df)
    stage_df = stage_df.join(csv_df)
    

def single_pd2stage_pd(stage):
    global matrix_df
    for i in stage:
        csv2single_pd(i)
    print(stage_df)
    stage_df.dropna(axis=0, how="any", inplace=True)
    print("stage_df_dropna", stage_df)
    matrix_df = matrix_df.join(stage_df)
    print("matrix_df:", matrix_df)

Spgonia = ["day8_Sp'gonia", "day10_Sp'gonia", "day12_Sp'gonia", "day14_Sp'gonia", "day16_Sp'gonia", "day18_Sp'gonia"]
PL = ["day8_PL", "day10_PL", "day12_PL", "day14_PL", "day16_PL", "day18_PL"]
EL = ["day8_EL", "day10_EL", "day12_EL", "day14_EL", "day16_EL", "day18_EL"]
LL_Z = ["day8_LL+Z", "day10_LL+Z", "day12_LL+Z", "day14_LL+Z", "day16_LL+Z", "day18_LL+Z"]
LL_Z_EP = ["day8_LL+Z+EP", "day10_LL+Z+EP", "day12_LL+Z+EP", "day14_LL+Z+EP", "day16_LL+Z+EP", "day18_LL+Z+EP"]
EP = ["day8_EP", "day10_EP", "day12_EP", "day14_EP", "day16_EP", "day18_EP"]
EP_LP_D = [ "day8_EP+LP+D", "day10_EP+LP+D", "day12_EP+LP+D", "day14_EP+LP+D", "day16_EP+LP+D", "day18_EP+LP+D"]
LP_D = ["day8_LP+D", "day10_LP+D", "day12_LP+D", "day14_LP+D", "day16_LP+D", "day18_LP+D"]

stage_df = matrix_df_ori
stage = Spgonia
single_pd2stage_pd(stage)

stage_df = matrix_df_ori
stage = PL
single_pd2stage_pd(stage)

stage_df = matrix_df_ori
stage = LL_Z
single_pd2stage_pd(stage)

stage_df = matrix_df_ori
stage = LL_Z_EP
single_pd2stage_pd(stage)

stage_df = matrix_df_ori
stage = EP
single_pd2stage_pd(stage)

stage_df = matrix_df_ori
stage = EP_LP_D
single_pd2stage_pd(stage)

stage_df = matrix_df_ori
stage = LP_D
single_pd2stage_pd(stage)

matrix_df.dropna(axis=0, how="all", inplace=True)

matrix_df.to_csv("matrix_auto_dropna.csv")