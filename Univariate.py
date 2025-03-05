class univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtype=='O'):
                print("qual")
                qual.append(columnName)
            else:
                print("quan")
                quan.append(columnName)
        return quan,qual     

    def freqtable(columName,dataset): 
        freqtable=pd.DataFrame(columns=["UniqueValues","Frequency","RelativeFrequency","CumSum"])
        freqtable["UniqueValues"]=dataset["ssc_p"].value_counts().index
        freqtable["Frequency"]=dataset["ssc_p"].value_counts().values
        freqtable["RelativeFrequency"]=(freqtable["Frequency"]/103)
        freqtable["CumSum"]=freqtable["RelativeFrequency"].cumsum()
        return freqtable
    
    def univari(dataset,quan):
        descriptive=pd.DataFrame(index="mean","median","mode","Q1:25","Q2:50","Q3:75","99%","Q4:100","IQR",
                                  "1.5Rule","Lesser","Greater","Min","Max"],columns=quan)     
        for columnName in quan:
                descriptive[columnName]["mean"]=dataset[columnName].mean()
                descriptive[columnName]["median"]=dataset[columnName].median()
                descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
                descriptive[columnName]["Q1:25"]=dataset.describe()[columnName]["25%"]
                descriptive[columnName]["Q2:50"]=dataset.describe()[columnName]["50%"]
                descriptive[columnName]["Q3:75"]=dataset.describe()[columnName]["75%"]
                descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
                descriptive[columnName]["Q4:100"]=dataset.describe()[columnName]["max"]
                descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75"]- descriptive[columnName]["Q1:25"]
                descriptive[columnName]["1.5Rule"]=1.5*descriptive[columnName]["IQR"]
                descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25"]-descriptive[columnName]["1.5Rule"]
                descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75"]+descriptive[columnName]["1.5Rule"]
                descriptive[columnName]["Min"]=dataset[columnName].min()
                descriptive[columnName]["Max"]=dataset[columnName].max()
        return descriptive  
        
    def Findingoutlier_columnname(descriptive,quan):
        for columnName in quan:
            if(descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]):
               lesser.append(columnName)
            if(descriptive[columnName]["Max"]>descriptive[columnName]["Greater"]):  
               greater.append(columnName)
        return lesser,greater

    def Replacing_outlier(dataset,descriptive,quan):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["Lesser"]]=descriptive[columnName]["Lesser"]
        for columnName in greater:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["Greater"]]=descriptive[columnName]["Greater"]
        return dataset  