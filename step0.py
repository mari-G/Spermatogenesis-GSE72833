import pandas as pd 

def xlsx2pd(sheet_range):
    global data_xls
    global sheet_name_list

    data_xls = pd.ExcelFile("GSE72833_GeneLists.xlsx")
    sheet_name_list = data_xls.sheet_names

    for i in range(sheet_range):
        #sheet_name=None表示读取全部sheet，或者sheet_name=[0,10]
        sheet_name = sheet_name_list[i]
        df_tmp = data_xls.parse(sheet_name)
        df_tmp.to_csv(sheet_name + ".csv", index= False)

xlsx2pd(7)    
