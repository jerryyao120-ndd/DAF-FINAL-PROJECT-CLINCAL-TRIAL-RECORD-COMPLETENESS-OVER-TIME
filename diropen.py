# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:44:56 2020

@author: jerryyao
"""


import numpy as np

import xml.etree.ElementTree as ET
import pandas as pd
import os
parent_path='G:\\AllAPIXML\\'

def generate_pathlist(parent_path):
    paths=[]
    dirs=os.listdir(parent_path)
    for dire in dirs:
        dirpath=os.path.join(parent_path,dire)
        files=os.listdir(dirpath)
        for file in files:
            paths.append(os.path.join(dirpath,file))
    return paths

paths=generate_pathlist(parent_path)
numofrec=len(paths)
data=pd.DataFrame(index=range(0,numofrec))

for i in range(0,numofrec): 
    tree = ET.parse(paths[i])
    for elem in tree.iter():
        if elem.tag=='Field':
            if elem.attrib['Name'] not in data.columns:
                data[elem.attrib['Name']]=[[] for _ in range(0,numofrec)]
            
             
            data[elem.attrib['Name']][i].append(elem.text)
            
            
                
    