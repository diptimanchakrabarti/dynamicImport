import pandas as pd
import sys
import json
import os
from configparser import ConfigParser


def main(src_key):

    resp=parser(src_key)
    return resp

def parser(src_key):
   thisfolder = os.path.dirname(os.path.dirname(__file__))
   # print(f"folder path is{thisfolder}")

   configfile = os.path.join(thisfolder, 'fileConfig/config.ini')
   config = ConfigParser(interpolation=None)
   config.read(configfile)
   folderpath = config.get('abs_paths', 'csv_path')
   targetfile = config.get('abs_paths', 'csv_file')
   filepath = os.path.join(folderpath, targetfile)
   print(f"The csv file name with path is: {filepath}")
   csvdata=pd.read_csv(filepath)
   csvdata['src_key']=src_key
   print(f"read the csv file")
   print(csvdata.head(4))
   return csvdata



if __name__=="__main__":
    src_key="CSV"
    main(src_key)