import os, sys

def pre_file(dir,file,formats):
    os.chdir(dir)
    i=1
    ls=os.listdir() 
    try:
        if os.path.exists(str(os.getcwd)):
            for x in ls: 
                if (f'.{formats}' in x) and (file not in x):
                    name='mais'+str(i)+'.jpg'
                    os.rename(x,name)
                    i += 1
    except Exception as e:
        print(f"""Sorry bro.. ur program is unable to run
and causing errror>> {e}""")
if __name__ == "__main__":
    pre_file(r"C:\Users\sahil\Downloads\Images",'main','jpg')
