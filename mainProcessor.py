import importlib.util
import importlib
import os
import pandas as pd
import sys
from configparser import ConfigParser


file_path='dynamicimport/callableComponent'
sys.path.append('/dynamicimport/callableComponent/')
from callableComponent import readcsv
def main():
    print("test")
    thisfolder = os.path.dirname(os.path.dirname(__file__))
    # print(f"folder path is{thisfolder}")
    argList = sys.argv
    srcConfig=argList[1]

    configfile = os.path.join(thisfolder, os.path.join('dynamicimport',srcConfig))
    print(f"config file path is:{configfile}")
    config = ConfigParser(interpolation=None)
    config.read(configfile)
    filename = config.get('configuration_items', 'application_name')
    srckey = config.get('configuration_items', 'src_key')

    packagename=config.get('configuration_items', 'package_name')
    modulename=filename.split('.')[0]


    finalpath=packagename+"."+modulename


    module = importlib.import_module(finalpath, packagename)
    print(f"get the file:{module}")
    module.parser(srckey)



if __name__=="__main__":
    main()

