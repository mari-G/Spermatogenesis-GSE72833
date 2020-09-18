import pandas as pd 

def xlsx2pd(sheet_range):
    global data_xls
    global sheet_name_list
    global stage_name

    data_xls = pd.ExcelFile("GSE72833_GeneLists.xlsx")
    sheet_name_list = data_xls.sheet_names

    for i in range(sheet_range):
        #sheet_name=None表示读取全部sheet，或者sheet_name=[0,10]
        stage_name = sheet_name_list[i]
        df_tmp = data_xls.parse(stage_name)
        df_tmp.to_csv(stage_name + ".csv", index= False)
        print(stage_name)

xlsx2pd(8)    
print("stages:\t", sheet_name_list)

# new DataFrame columned by day

import pandas as pd 

usecols = list(range(6, 34))
usecols.append(0)
# print(usecols)

stage_filename = "LL+Z.csv"
ori_df = pd.read_csv(stage_filename, usecols= usecols)
ori_df.set_index(["gene_id"], inplace= True)
ori_df.index.name = None
print(ori_df.head())

col_names = list(ori_df.columns)
# print(col_names)
# print("\n")

                                                                                            
day_list = []
for col_name in col_names:
    if "_" in col_name:
        day_sample_num = col_name.split(r"_")
        day = day_sample_num[0]
        sample_num = day_sample_num[1]
        # print(day, sample_num)
        day_list.append(day)
        # day_set=set(day_list)
        # print(day_list)

    else:
        continue
day_col = sorted(set(day_list), key= day_list.index)
df_mean_by_day = pd.DataFrame(index= ori_df.index, columns= day_col)
print(df_mean_by_day)
