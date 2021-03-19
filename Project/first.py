import pandas as pd 
import numpy as np 
import os , sys
from main import *
# use reset index after edit 
# basic input in other(main) file 
# command just display or change database

def info(data): # basic info_   #display
    print(data.info())

def first_n(data, x=4): #to get first n records of a DataFrame  #display
    print(data.iloc[:x])



def group_by(data, col, index="COLUMN"): #display
    value = data.groupby([col]).size().reset_index(name=index)
    print(value)

def col_max_value(data, col): #display
    print(data[col].argmax())

def sum_(data, col):  #display
    print( sum( data[col] ))

def mean( data, col):  #display
    print( mean( data[col] ))

def is_col(data, col): #Pandas program to check whether a given column is present in a DataFrame or not.
    if col in data.columns:
        print(f"Column {col} is present") #display
    else:
        print(f"Column {col} is absent")

def d_type(data): #display
    print(data.dtypes)

def reverse_order(data): #display
    os.system("cls||clear")
    print("[1] Reverse column order:")
    print("[2] Reverse row order:")
    # print("[3] Reverse row order and reset index:")
    
    command = int(input(">>> "))
    if command == 1:
        print(data.loc[:, ::-1])
    elif command == 2:
        print(data.loc[::-1])
    else:
        print("[ERROR] Krta k ni ohi kam jehda mnu drr c :)")
    # elif command == 3:
    #     print(data.loc[::-1].reset_index(drop = True))

def between_n(data,x=0,y=9):  #display
    
    print(data.iloc[x:y])

def get_col_index(data, col): #to get column index from column name
    print(data.columns.get_loc(col))#display

def except_col(data,col): #to select all columns, except one given column
    df = data.loc[:, data.columns != col] #display
    print(df)

def select_col_by_dtype(data): #to select columns by data type of a given DataFrame.
    os.system("cls||clear")
    print("[1] Select numerical columns") #display
    print("[2] Select string columns")
    command = int(input(">>> "))
    if command == 1:
        print(data.select_dtypes(include = "number"))
    elif command == 2:
        print(data.select_dtypes(include = "object"))

def single_select_column(data, col):   #display
    # print(col)
    print(data[[col]])

def select_rows(data,col, value): # Pandas program to select rows from a given DataFrame based on values in some columns
    print(data.loc[data[col] == value]) #display

def greater_than( data, col, n=2): # if nol doesnt contain int than solve error    #display 
    print( data[ data[col]>n ])

def less_than( data, col, n=2): # if nol doesnt contain int than solve error    #display 
    print( data[ data[col]<n ])

def n_rows_cols(data): #display
    print(f"Number of rows: {len(data.axes[0])}\nNumber of columns: {len(data.axes[1])}")

def find_nan(data,col): #to select the rows where the score is missing  #display
    print( data[data[col].isnull() ])

def value_between(data,col,from_, to_): #display
    print( data[data[col].between(from_, to_)] )

def less_greater_than(data,col, from_, to_):  #display
    print(data[(data[col] < from_) & (df[col] > to_)])

def memory_usage(data): #display
    print()
    print(data.memory_usage(deep = True))

def random_data(data,x=3):  # how many / random data_   #display
    sample_ = data.sample( n=x )
    print( sample_ )

def remove_first_n(data, n):  #edit
    global df
    df = data.iloc[n:]
    print(df)

def remove_last_n(data, n): #edit
    global df
    df = data.iloc[:n]
    print(df)

def prefix_suffix(data, string_): #edit
    global df 
    print("[1] For adding prefix")
    print("[2] For adding suffix")
    print("[3] For adding both prefix and suffix")

    command = int(input(">>> "))
    if command == 1:
        df = data.add_prefix(string_)
        print(df)
    elif command == 2:
        df = data.add_suffix(string_)
        print(df)
    elif command == 3:
        df = data.add_prefix(string_)
        df = df.add_suffix(string_)
        print(df)
        



def change_value(data, row, col, alter_value):  #edit
    data.iloc[row,col] = alter_value
    print(data)



def append_col( data, col): #edit
    input_ = int(input("Enter the column values")) # to input string and output as list sep by commas 
    data[col] = input_

def drop_row(data, row):  #edit
    global df 
    df = data.drop(row)
    print(df)

# def sort_order(data, *col):
#     data.sort_values(by=[col],ascending=[])

def replace_value(data, col, from_, to_):  #edit
    try:
        data[col] = data[col].replace(from_, to_)
        print(data)
    except Exception as e:
        print("[+] Value not found")

def del_col(data, col):  #edit
    data.pop(col)
    print(data)

def list_col(data): #Pandas program to get list from DataFrame column headers #display
    print(list(data.columns.values))

def rename_col_(data): #edit
    n = int(input("Enter number of col to rename: "))
    d = {}
    for i in range(n):
        keys = input("Original: ") 
        values = input("After_Rename: ") 
        print()
        d[keys] = values
    re = data.rename(columns=d)
    print(re)
    # data_ = data.rename(columns = re)
    # print(data_)



def drop_nan(data, col): #edit
    value = data.loc[pd.isna(data["gender"]), :].index
    df = data.drop(value)
    print(df)

def dropby_index(data, *index_): 
    global df 
    df = data.drop(data.index[index_])
    print(df)
    
def reset_index(data): 
    global df 
    df = data.reset_index()
    print(df)


def change_type(data, col): 
    global df
    print()
    print("[1] From int to float")
    print("[2] From float to int")
    print()
    command = int(input(">>> "))
    if command == 1:
        data[col] = data[col].astype(float)
        df = data
        print(data)
    elif command == 2:
        data[col] = data[col].astype(int)
        df = data
        print(data)
    else:
        print("[ERROR] ohh hoo krta k ni ohi kam :(")

def remove_inf(data): 
    global df 
    data = data.replace([np.inf, -np.inf], np.nan)
    df = data
    print(df)

def col_insert(data,new_col,position,col_name="col1"): 
    global df 
    df.insert(loc=position, column=col_name, value=new_col)
    command = int(input(">>> "))
    if command == 1:
        print(data.select_dtypes(include = "number"))
    elif command == 2:
        print(data.select_dtypes(include = "object"))

def create_df(): 
    os.system("cls||clear") 
    print("-*-*-*-*-*- Rough DataFrame -*-*-*-*-*-")
    print("[1] Create Random value DF")
    print("[2] Create Missing value DF")
    print("[3] Create Datetime DF")
    print("[4] Create Mixed value DF")
    print("\n[0] Hit 0 for back and 1 for exit\n")
    command = int(input(">>> "))
    if command == 1:
        df1 = pd.util.testing.makeDataFrame() 
        print(df1)
    elif command == 2:
        df2 = pd.util.testing.makeMissingDataframe() 
        print(df2)
    elif command == 3:
        df3 = pd.util.testing.makeTimeDataFrame() 
        print(df3)
    elif command == 4:
        df4 = pd.util.testing.makeMixedDataFrame() 
        print(df4)
    elif command == 0:
        phase_one()
    elif command == 1:
        sys.exit()


if __name__ == "__main__":
    df = pd.read_csv("sample.csv")
    drop_nan(df,'gender')
    memory_usage(df)