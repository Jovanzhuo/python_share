#convert the following matlab code to python code
#FilepathMain = 'E:\data_dir\'
#ExcelName = 'ADC_8M.csv'
#Fs=8*10^6
#Rawdata_Now = xlsread([FilepathMain ExcelName]);
#Rawdata_Now(:,[1]) = []
#Ns=size(Rawdata_Now)
#Column = Ns(1,2)
#Row = Ns(1,1)
#tt = Column
#for i = 1:1000
#    a=2*i
#    Rawdata(:,i)=Rawdata_Now(:,a)
#end
#Rawdata_text=Rawdata(1,:)
#t=1:1:Column/2;
#tet=1:1:999;
#figure(5)
#plot(t,Rawdata(),'-*')
#Rawdata(1,:)=Rawdata(1,:)-mean(Rawdata(1,:))
#plot(t,Rawdata(1,:),'-*')

import pandas as pd
import matplotlib.pyplot as plt

FilepathMain = 'E:/data_dir/'
ExcelName = 'ADC_8M.csv'

Fs = 8*10^6
Rawdata_Now = pd.read_csv(FilepathMain + ExcelName, header=None)
Rawdata_Now.drop(Rawdata_Now.columns[0], axis=1, inplace=True)
Ns = Rawdata_Now.shape
Column = Ns[1]
Row = Ns[0]
tt = Column
Rawdata = pd.DataFrame()
for i in range(1,1000):
    a = 2*i
    Rawdata[:,i] = Rawdata_Now[:,a]
Rawdata_text = Rawdata[1,:]
t = range(1,Column/2)
tet = range(1,999)
plt.figure(5)
plt.plot(t,Rawdata(),'-*')
Rawdata[1,:] = Rawdata[1,:] - Rawdata[1,:].mean()
plt.plot(t,Rawdata[1,:],'-*')
plt.show()
