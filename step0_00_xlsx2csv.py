import pandas as pd 

def xlsx2pd(sheet_range):
    global data_xls
    global sheet_name_list
    global stage_name

    data_xls = pd.ExcelFile("GSE72833_GeneLists.xlsx")
    sheet_name_list = data_xls.sheet_names

    stage_list = []
    for i in range(sheet_range):
        #sheet_name=None表示读取全部sheet，或者sheet_name=[0,10]
        stage_name = sheet_name_list[i]
        stage_list.append(stage_name)
        df_tmp = data_xls.parse(stage_name)
        df_tmp.to_csv(stage_name + ".csv", index= False)
        print(stage_name)




def group_by_stage2stage_day(stage_name):
    usecols = list(range(6, 34))
    usecols.append(0)
    # print(usecols)

    ori_df = pd.read_csv(stage_name + ".csv", usecols= usecols)
    ori_df.set_index(["gene_id"], inplace= True)
    ori_df.index.name = None
    # print(ori_df.head())

    col_names = list(ori_df.columns)
    # print(col_names)
    # print("\n")

                                                                                                
    day_sample_dict = {}
    for col_name in col_names:
        if "_" in col_name:
            day_sample_num = col_name.split(r"_")
            day = int(day_sample_num[0])
            sample_num = int(day_sample_num[1])
            day_sample_dict[day] = sample_num
            # print(day_sample_dict) 
        else:
            continue

    # df_mean_by_day = pd.DataFrame(index= ori_df.index, columns= day_sample_dict.keys())
    df_mean_by_day = pd.DataFrame(index= ori_df.index)
    # print(day_sample_dict)
    # print(df_mean_by_day)


    for day, sample_num in day_sample_dict.items():
        col_list_for_everyday_mean = []
        for i in range(1, sample_num+1):
            col_name = str(day) + "_" + str(i)
            col_list_for_everyday_mean.append(col_name)
            # print(col_list_for_everyday_mean)
            try:
                df_mean_by_day[str(day)] = ori_df[col_list_for_everyday_mean].mean(axis= 1)
                df_mean_by_day.to_csv("day" + str(day) + "_" + stage_name + ".csv", columns= [str(day)])
            except KeyError:
                continue
            # print(df_mean_by_day)
            


sheet_range = 8


xlsx2pd(sheet_range) 

for stage_name in sheet_name_list[:sheet_range]:
    group_by_stage2stage_day(stage_name)
