# This File serves to convert the AIP Retetion document into pyton form for data visulization and for GitHub updates 
# Comments such as these will be made either at key points along the code to inform readers or to serve as markers for updates
# print("hello world")

#install the necesary code to convert exel files and push to github
# used pip3 install pandas 
import pandas as pd
# imported matplot for data.
import matplotlib.pyplot as plt


# Read the Excel file into a pandas DataFrame
df = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/AIP Retention.xlsx")
# Specify the sheet name or index
Retention = 'Retention'  
Math = 'Math'
# Read data from the specified sheet
dfr = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/AIP Retention.xlsx", sheet_name=Retention) # Full Data set trimed for ease
dfm = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/AIP Retention.xlsx", sheet_name=Math) #simplified math data


# Now you can work with the data in the DataFrame
# print(dfm.head())  # Print the first few rows of the DataFrame
# print(dfm) # prints the data frame

#Push to git  using git push -u origin main ()

#Go to the Math Sheet via pandas and write code to make the graphs 
# need to select the rows 2-22 then for each of those make a histogram
# repeate process for rows in patters of 1 year, 2 year, 5 year, 10 year, 20 year so 2-3, 4-5,... 2-4, 5-7,... 2-7, 8-12, ... 2-12, 13-22 ... 2-22 
# use code df.loc[row wanted],or for multiple df.iloc[first row wanted:last row wanted]
#df.iloc[:, [1, 2, 5]] Select columns in positions 1, 2 and 5 (firstcolumn is 0).

num_rows = len(dfm)
print("Number of rows:", num_rows)
print("rember to uncoment recursion and comment this line")

# generic histograms
# CURRENTLY PRODUCES HISTOGRAMS BUT NOT OF PROPER TYPE TO BE FIXED ASAP 4-5-24

def row_1(n):
    if n >= 20:
        print(n, "is this")
        # Selecting the row and columns B-F from DataFrame dfm
        selected_row = dfm.iloc[n,[1, 2, 3, 4, 5]]
        print(selected_row)
        # Plotting a histogram of the selected row
        selected_row.plot.hist()
        plt.title("Data for " + str(2002+n))
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.show()
        print('end')
    else:
        print(n)
        # Selecting the row and columns B-F from DataFrame dfm
        selected_row = dfm.iloc[n,[1, 2, 3, 4, 5]]
        print(selected_row)
        # Plotting a histogram of the selected row
        selected_row.plot.hist()
        plt.title("Data for " + str(2002+n))
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.show()
        n = n + 1
        row_1(n)

def rows_2(n): 
    if n >= 20:
        print(n, "is this")
        #dfm.iloc[20,[1, 2, 3, 4, 5]] (wont need cause 19-20 has the 2 year)
        print('end')
    else: 
        print(n)
        dfm.iloc[n:n+1,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        n=n+1
        print(n)
        rows_2(n)
        # dfm.plot.hist()
        # print(dfm.plot.hist())

def rows_5(n): 
    if n >= 15:
        print(n, "final n")
        dfm.iloc[n:n+5,[1, 2, 3, 4, 5]] 
        print('end')
        # dfm.plot.hist()
        # print(dfm.plot.hist())
    else: 
        print(n)
        dfm.iloc[n:n+5,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        n=n+5
        print(n)
        rows_5(n)
        # dfm.plot.hist()
        # print(dfm.plot.hist())

def rows_10(n): 
    if n >= 10:
        print(n, "final n")
        dfm.iloc[n:n+10,[1, 2, 3, 4, 5]] 
        print('end')
        # dfm.plot.hist()
        # print(dfm.plot.hist())
    else: 
        print(n)
        dfm.iloc[n:n+10,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        n=n+5
        print(n)
        rows_10(n)
        # dfm.plot.hist()
        # print(dfm.plot.hist())

def rows_20(n): 
    if n >= 0:
        print(n, "final n")
        dfm.iloc[n:n+20,[1, 2, 3, 4, 5]] 
        print('end')
        # dfm.plot.hist()
        # print(dfm.plot.hist())
    else: 
        print("error")

# create data sets for the CARNAGE data classifies the US into 9 regions (in obreg collum):
# issue will have to use og data set, good news already have the stuff that i need to do it
# collum x for the obreg so need to be at 23 (increment form 0) over each year to create a adata set for each year
#Full data set (df)CODE, the following are the year break points 765, 1529, 2296, 3060, 3820, 4583, 5346, 6107, 6866, 7619, 8370, 
# 9123, 9875, 10627, 11378, 12138, 12899, 13667, 14430, 15185, 15931
#so will read over each line find what group it belongs to asign it to the apropriate data set for analysis 
# groups are 0-8 for the different regions


# Calls for the recursion 
# row_1(0)
# rows_2(0)
# rows_5(0)
# rows_10(0)
# rows_20(0)

# CURRENT ISSUE HISTOGRAMS NOT PRINTING OUT 
# FIXED BY ADDING MATPLOT

# FIX FOR MORNING, GET GITHUB WORKING