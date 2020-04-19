###Some anotations

#Dealing with missing values

#The best practice is replace the missing values, options:
#Option 1: Replace de missing values with de Average value of entries data
#Option 2: Replace it by Frequency
#Option 3: Leave it as missing values

df.dropna(subset = ["Price", axis = 0, inplace = True]);
#inplace true allow the modification to be done to the dataset directly


#Replace using mean

mean = df["Normalizes-Losses"].mean()
df.["Normalized-Losses"].replace(np.nan, mean)


#Data formating in python
#like when you receive datas from diferent parts refering as New York in diferent ways, like:
#New york
#new York
#N.Y
#ny
#n.Y
#N.y
#we need to normalize this,

###DATA NORMALIZATION IN PYTHON
#1st method : Simple featuring scale 
#Xnew = Xold /Xmax
#EX:
df["Length"] = df["Length"]/df["Length"].max()

#2nd Method: Mim-Max
# Xnew = (Xold - xMin)/ (Xmax-xMin)
#EX:
df["Length"] = (df["Length"] - df["Length"].min())/(df["Length"].max() - df["Length"].min())
#3rd Method: Z-score
#Xnew = Xold - MU(the avg of the feature) / standard deviation
#EX:
df["Length"]=(df["Length"]-df["Length"].mean())/df["Length"].std()



#Binning values
#Binning is when you group values together into bins. 
# For example, you can bin “age”
#into [0 to 5], [6 to 10], [11 to 15] and so on.
bins = np.linspace(min(df["Price"]),max(df["Price"]),4)
#4 equally spaced numbers over the specified interval of the price.
group_names=["Low","Medium","High"]

df["Price-binned"] = df.cut(df["Price"],bins,labels=group_names,incluse_lowest=True)
#We create a list “group_names “ that contains the different bin names.
##You can then use histograms to visualize the distribution of the data after they’ve been
#divided into bins.


###TURNING CATEGORICAL VARIABLES INTO QUANTITATIVE VARIABLES IN PYTHON
pd.get_dummies(df["Fuel"])

