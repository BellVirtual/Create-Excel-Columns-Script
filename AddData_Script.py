
import pandas as pd
import os
import sys

########generate file path
'getcwd:      ', os.getcwd()
osfile, maindir =('__file__:    ', __file__)
filename = os.path.basename(sys.argv[0])
inpath = maindir.replace(filename,"Excels")
outpath = maindir.replace(filename,"BulkFile.xlsx")


#########pandas script
def add_column(inpath,outpath):
    for root, dirs, files in os.walk(inpath):
        print(files)
        for f in files:
            path = os.path.join(root, f)
            excelframe = pd.read_excel(path)
            # if column is a number or need to be converted it has to be defined like
            # excelfram['num'].astype(str)
            excelframe['full_name'] = excelframe.first_name + " " + excelframe.last_name
            dataframe = [excelframe]
            compactframe = pd.concat(dataframe)
            compactframe.to_excel(outpath)


add_column(inpath,outpath)

