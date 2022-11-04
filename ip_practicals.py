import pandas as pd 
import numpy as np
import matplotlib.pyplot as pt


def First():
    dict1 = {"Name":"Dhakshinesh","Class":1}
    array1 = np.array([1,2,3,4])

    Ser1 = pd.Series(dict1)
    Ser2= pd.Series(array1)
    print(Ser1)
    print(Ser2)

def Second():
    Ser1 = pd.Series([25,35,45,75,85,95,105])
    print(Ser1[Ser1>75])

def Third():
    dict1 = {"Category":["Food","Furniture","Books"],"Item Name":["Jim Jam","Ikea Table","Flamingo"],"Cost":[20,5000,100000]}
    df1 = pd.DataFrame(dict1)
    group = df1.groupby('Category')
    print(df1)
    print(group['Category','Cost'].sum())

def Fourth():
    dict1 = {"Name":["Dhakshinesh","Pantangii","Jamula"],"Marks":[101,99,100]}
    df1 = pd.DataFrame(dict1) #Result
    print(df1)
    print(df1.index)
    print(df1.columns)
    print(df1.dtypes)
    print(df1.ndim)
    print(df1.shape)

def Fifth():
    dict1 = {"Name":["Ramu","Somu","Meenu","Seenu"],"Class":[10,10,11,12]}
    df1 = pd.DataFrame(dict1)
    print(df1[df1.duplicated("Class",keep=False)])

def Sixth():
    df1 = pd.read_csv("Sixth.csv")
    print(df1)
    df2 = pd.DataFrame({"Name":["Random name"],"Class":[11],"Work":["of course nothing"]})
    df2.to_csv("Sixth.csv")

#Pandas Questions
#First()
#Second()
#Third()
#Fourth()
#Fifth()
#Sixth()

def Seventh():
    subject = ['Physic','Chemistry','Mathematics', 'Biology','Computer']
    marks =[80,75,70,78,82]
    pt.plot(subject,marks,'r',marker ='*')
    pt.title('Marks Scored')
    pt.xlabel('SUBJECT')          
    pt.ylabel('MARKS')
    pt.show()

def Eighth():
    pt.show()

def Nineth():
    df1 = pd.read_csv("Datasheet_eighth.csv")
    pt.barh(df1["State/UT"],df1["2021"])
    pt.show()

#Matplot-lib Questions
#Seventh()
#Eighth()
#Nineth()
