from cgi import print_environ
import xml.etree.ElementTree as et
from lxml import etree 
import numpy as np
import pandas as pd

mytree=et.parse("Sample.xml")
myroot=mytree.getroot()

""" 1. Extracting data from xml and storing it in dataframe"""

df_cols = ["category","item", "description", "calories"]
rows = []

for node in myroot: 
    s_category=node.tag
    s_item = node.find("item").attrib.get("name")
    s_description = node.find("description").text
    s_calories = node.find("calories").text
    
    rows.append({"category":s_category,"item": s_item, "description": s_description, 
                 "calories": s_calories})


out_df = pd.DataFrame(rows, columns = df_cols)
 
print(out_df)  
    
    
"""2. inserting price data into xml document"""
#Adding new subelement to nodes
for i in range(len(etree.parse("Sample.xml").getroot().getchildren())):
    et.SubElement(myroot[i],'price')

#Adding values to the subelement
for x in myroot.iter('price'):
    b=str(np.random.randint(5,25))+' Euro'
    x.text=str(b)

# creating a new file with the changes(we can overwrite same file if we need)
mytree.write('with_price.xml')