import os, sys
import pandas as pd 
import numpy as np 
from first import *

def initial(): #option for selecting diff csv file/ recommend name of csv files 
    global df 
    req_file = input("[+] Enter file name(CSV): ")
    try:
        df = pd.read_csv(req_file)
    except Exception as e:
        print("Ki kita yar glt name prta file da :(")
        initial()

def phase_one():
    print()

    print("____________________________________________________________________________________________________________________")
    print("____________________________________________________________________________________________________________________")

    print("""
                                    ******  ******* ***     **  *********** ****      
                                    ******  **   ** ***     **  *********** ****
                                    **      ******* **********      ***     ****
                                    ******  ******* **********      ***     ****    
                                        **  **   ** ***     **      ***     ****
                                    ******  **   ** ***     **  *********** ***********
                                    ******  **   ** ***     **  *********** ***********

                                                ***
                                            ***    ***
                                            ***  ***      
                                               ***
                                            ***    ***   ***
                                          ***          ***
                                            ***      ***  ***
                                                ***          ***

                                    *******     *******    **********  *******  ***      **
                                    *******     **   **    **********  **   **  ****     ** 
                                    **   **     *******        **      *******  ** **    **
                                    **   **     *******        **      *******  **  **   ** 
                                    *******     **   **        **      **   **  **   **  ** 
                                    *******     **   **        **      **   **  **    ** **
                                    ** **       **   **        **      **   **  **     ****
                                    **   **     **   **        **      **   **  **      ***   
    """)
    print("____________________________________________________________________________________________________________________")
    print("____________________________________________________________________________________________________________________")

    print("\nThis Project was great headache but we make it :)\n")

    print("[1] For Display Database")
    print("[2] For Edit Database")
    print("[3] Rough Database\n")
    print("[0] Press 0 for exit\n")
    phase_two()

def phase_two():
    global df
    command_ = int(input(">>> "))

    os.system("cls||clear")

    def one():
        def exit_():
            print("\n[-] Hit 0 to go back or 1 to exit")
            command_two = int(input(">>> "))
            if command_two == 0:
                os.system("cls||clear")
                one()
            elif command_two == 1:
                sys.exit()

        if command_ == 0:
            sys.exit()

        elif command_ == 1:
            print("[1]  to display information of DataFrame")
            print("[2]  to get first n records of a DataFrame")
            print("[3]  to group_by col")
            print("[4]  to get column max value")
            print("[5]  to get sum of particular column")
            print("[6]  to find mean value of particular column")
            print("[7]  to check if there is specific column")
            print("[8]  to check data types of DataFrame")
            print("[9]  to reverse the order of column and row")
            print("[10] to find data between any two value")
            print("[11] to get column index from column name ")
            print("[12] to select all columns, except one given column")
            print("[13] to select columns by data type of a given DataFrame")
            print("[14] to select single column")
            print("[15] to select row")
            print("[16] to find any value greater than **")
            print("[17] to select the rows where the value is missing")
            print("[18] to find value which is less than **")
            print("[19] to display the memory usage")
            print("[20] to display random data from Dataframe\n")
            print("[0]  Hit enter to go back")

            command_one = int(input(">>> "))
            print()

            if command_one == 0:
                os.system("cls||clear")
                phase_one()

            if command_one == 1:
                os.system("cls||clear")
                info(df)
                exit_()
            
            if command_one == 2:
                os.system("cls||clear")
                num = int(input("[+] Enter number of first rows you want to see: "))
                first_n(df,num)
                exit_()

            if command_one == 3:
                os.system("cls||clear")
                # print("Columns: ")
                print(f"\nColumns: {[x for x in df.columns]}\n")
                column=input("[+] Enter name of column: ")
                group_by(df,column)
                exit_()

            if command_one == 4:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                print()
                column=input("[+] Enter name of column: ")
                col_max_value(df,column)
                exit_()

            if command_one == 5:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                column=input("[+] Enter name of column: ")
                sum_(df,column)
                exit_()

            if command_one == 6:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                column=input("[+] Enter name of column: ")
                mean(df,column)
                exit_()

            if command_one == 7:
                os.system("cls||clear")
                print(f"\nColumns: {[x for x in df.columns]}\n")
                column=input("[+] Enter name of column: ")
                is_col(df, column)
                exit_()

            if command_one == 8:
                os.system("cls||clear")
                d_type(df)
                exit_()

            if command_one == 9: #use functionality here/ clear previous data
                os.system("cls||clear")
                reverse_order(df)
                exit_()

            if command_one == 10:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                from_ = int(input("[+] From: "))
                to_ = int(input("[+] To: "))
                between_n(df,from_,to_)
                exit_()
            
            if command_one == 11:
                os.system("cls||clear")
                print(f"\nColumns: {[x for x in df.columns]}\n")
                column=input("[+] Enter name of column: ")
                get_col_index(df,column)
                exit_()

            if command_one == 12:
                os.system("cls||clear")
                print(f"\nColumns: {[x for x in df.columns]}\n")
                column=input("[+] Enter name of column: ")
                except_col(df, column)
                exit_()

            if command_one == 13:
                os.system("cls||clear")
                select_col_by_dtype(df)
                exit_()
            
            if command_one == 14:
                os.system("cls||clear")
                print(f"\nColumns: {[x for x in df.columns]}\n")
                column=input("[+] Enter name of column: ")
                single_select_column(df,column)
                exit_()


            if command_one == 15:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                value = int(input("[+] Enter value: "))
                column=input("[+] Enter name of column: ")
                select_rows(df,column,value)
                exit_()

            if command_one == 16:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                column=input("[+] Enter name of column: ")
                num = int(input("Value greater from: "))
                greater_than(df,column,num)
                exit_() 

            if command_one == 17:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                column=input("[+] Enter name of column: ")
                find_nan(df,column)
                exit_()

            if command_one == 18:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                column=input("[+] Enter name of column: ")
                num = int(input("Value less from: "))
                less_than(df,column,num)
                exit_()

            if command_one == 19:
                os.system("cls||clear")
                memory_usage(df)
                exit_()
            
            if command_one == 20:
                os.system("cls||clear")
                num = int(input("Number of random values: "))
                random_data(df,num)
                exit_()
                
        elif command_ == 3:
            def create_df(): 

                def exit_():
                    os.system("cls||clear")
                    create_df()
                    
                os.system("cls||clear") 
                print("-*-*-*-*-*- Rough DataFrame -*-*-*-*-*-")
                print("[1] Create Random value DF")
                print("[2] Create Missing value DF")
                print("[3] Create Datetime DF")
                print("[4] Create Mixed value DF")
                print("\n[0] Hit 0 for back \n")
                command = int(input(">>> "))
                if command == 1:
                    df1 = pd.util.testing.makeDataFrame() 
                    print(df1)
                    input("\n[-]Press Enter")
                    exit_()

                elif command == 2:
                    df2 = pd.util.testing.makeMissingDataframe() 
                    print(df2)
                    input("\n[-]Press Enter")
                    exit_()
                    
                elif command == 3:
                    df3 = pd.util.testing.makeTimeDataFrame() 
                    print(df3)
                    input("\n[-]Press Enter")
                    exit_()
                    
                elif command == 4:
                    df4 = pd.util.testing.makeMixedDataFrame()
                    print(df4)
                    input("\n[-]Press Enter")
                    exit_()
                    
                elif command == 0:
                    phase_one()
                
            create_df()
        
        elif command_ == 2:
            print("[1] to remove first n rows: ")
            print("[2] to remove last n rows: ")
            print("[3] to apply prefix and suffix to column header: ")
            print("[4] to alter value: ")
            print("[5] to append column: ")
            print("[6] to drop row: ")
            print("[7] to replace any value of row: ")
            print("[8] to delete column: ")
            print("[9] to get list of column: ")
            print("[10] to rename any column: ")
            print("[11] to drop rows with NaN value: ")
            print("[12] to reset index: ")
            print("[13] to change data-type: ")
            print("[14] to remove infinty value: ")
            print("\n[0] Hit 0 to go back \n")
            command = int(input("\n>>> "))

            if command == 1:
                os.system("cls||clear")
                num = int(input("[+] Enter number of rows: "))
                remove_first_n(df,num)
                exit_()
            
            elif command == 0:
                os.system("cls||clear")
                phase_one()

            elif command == 2:
                os.system("cls||clear")
                num = int(input("[+] Enter number of rows: "))
                remove_last_n(df, num)
                exit_()

            elif command == 3:
                os.system("cls||clear")
                string_ = input("[+] Enter String: ")
                prefix_suffix(df, string_)
                exit_()

            elif command == 4:
                os.system("cls||clear")
                print(f"\nColumns: {[x for x in df.columns]}\n")
                row = int(input("[+] Target Row[index]: "))
                column = int(input("[+] Target Column[index]: "))
                type_ = input("[+] Input Type: ")
                
                if type_ == "int":
                    alter_value = int(input("[+] Enter final value: "))
                elif type_ == "string":
                    alter_value = input("[+] Enter final value: ")

                change_value(df, row, column, alter_value)   
                exit_()             

            elif command == 5:  
                os.system("cls||clear")
                column = input("[+] Enter column name: ")
                print("[-] Sorry sir ji this function is on modification :{ ")
                exit_()

            elif command == 6:
                os.system("cls||clear")
                row = int(input("[+] Target Row[index]: "))
                drop_row(df, row)
                exit_()
            
            elif command == 7:
                os.system("cls||clear")
                int_value = df.select_dtypes(include = "number").columns
                print(f"\nColumns: {[x for x in int_value]}\n")
                column = input("[+] Target column: ")
                from_ = int(input("[+] Value[From]: "))
                to_ = int(input("[+] Value[To]: "))
                replace_value(df, column, from_, to_)
                exit_()

            elif command == 8:
                os.system("cls||clear")
                print(f"\nColumns: {[x for x in df.columns]}\n")
                column = input("[+] Target column: ")
                del_col(df, column)
                exit_()
                
            elif command == 9:
                os.system("cls||clear")
                list_col(df)
                exit_()

            elif command == 10:
                os.system("cls||clear")
                rename_col_(df)
                exit_()
            
            elif command == 11:
                os.system("cls||clear")
                column = input("[+] Target column: ")
                drop_nan(df, column)
                exit_()

            elif command == 12:
                os.system("cls||clear")
                reset_index(df)
                exit_()

            elif command == 13:
                os.system("cls||clear")
                column = input("[+] Target column: ")
                change_type(df, column)
                exit_()
            
            elif command == 14:
                os.system("cls||clear")
                remove_inf(df)
                exit_()
                            
         
    os.system("cls||clear")
    one()

if __name__ == "__main__":
    initial()
    
    os.system("cls||clear")
    phase_one() 