#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:06:21 2019

@author: rachellu
"""

import pandas as pd

#data02 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickjob/PickJob_02.csv")
#data03 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickjob/PickJob_03.csv")
#data04 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickjob/PickJob_04.csv")
#data05 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickjob/05.csv")
#data06 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickjob/06.csv")
#data07 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickjob/07.csv")


data02 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorder/02.csv")
data03 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorder/03.csv")
data04 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorder/04.csv")
data05 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorder/05.csv")
data06 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorder/06.csv")
data07 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorder/07.csv")



#data02 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorderdetail/PickOrderDetail_02.csv")
#data03 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorderdetail/PickOrderDetail_03.csv")
#data04 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorderdetail/PickOederDetail_04.csv")
#data05 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorderdetail/05.csv")
#data06 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorderdetail/06.csv")
#data07 = pd.read_csv("/Users/rachellu/Dropbox/capstone/pickorderdetail/07.csv")

frames = [data02,data03, data04,data05,data06,data07]

result = pd.concat(frames)
result.drop_duplicates(['ID'], keep='last', inplace=True) 
export_csv = result.to_csv (r'/Users/rachellu/Dropbox/capstone/merge_wo_duplicate/pickorder_lyp.csv', index = None, header=True)




