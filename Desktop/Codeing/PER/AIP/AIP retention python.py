# This File serves to convert the AIP Retetion document into pyton form for data visulization and for GitHub updates 
# Comments such as these will be made either at key points along the code to inform readers or to serve as markers for updates
# print("hello world")

#install the necesary code to convert exel files and push to github
# used pip3 install pandas 
import pandas as pd
# imported matplot for data.
import matplotlib.pyplot as plt
import numpy as np 


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
print("rember to uncoment recursion, and carnagee orginization and comment this line")

# generic histograms
# CURRENTLY PRODUCES HISTOGRAMS BUT NOT OF PROPER TYPE TO BE FIXED ASAP 4-5-24

def row_1(n):
    if n >= 20:
        print(n, "is this")
        # Selecting the row and columns B-F from DataFrame dfm
        selected_row = dfm.iloc[n,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        print(selected_row)
        # Plotting a histogram of the selected row
        # selected_row.plot.hist()
        plt.bar(categories, selected_row)
        # Add data labels above each bar
        for i, value in enumerate(selected_row):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.show() 
        print('end')
    else:
        print(n)
        # Selecting the row and columns B-F from DataFrame dfm
        selected_row = dfm.iloc[n,[1, 2, 3, 4, 5]]
        print(selected_row)
        # Plotting a histogram of the selected row
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        plt.bar(categories, selected_row)
        # Add data labels above each bar
        for i, value in enumerate(selected_row):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n))
        plt.ylabel("Values")
        plt.xlabel('Groups')
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
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.35
        plt.bar(x-bar_width/2, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x+bar_width/2, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width/2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row2):
            plt.text(i + bar_width/2, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+1))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+1
        print(n)
        rows_2(n)

def rows_5(n): 
    if n > 15:
        print(n, "final n")
        dfm.iloc[n:n+5,[1, 2, 3, 4, 5]] 
        print('end')
        # dfm.plot.hist()
        # print(dfm.plot.hist())
    else: 
        print(n)
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        selected_row3 = dfm.iloc[n+2,[1, 2, 3, 4, 5]]
        selected_row4 = dfm.iloc[n+3,[1, 2, 3, 4, 5]]
        selected_row5 = dfm.iloc[n+4,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.1
        plt.bar(x-bar_width*4, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x-bar_width*3, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        plt.bar(x-bar_width*2, selected_row3, width=bar_width, label="Data for" + str(2002+n+2))
        plt.bar(x-bar_width, selected_row4, width=bar_width, label="Data for" + str(2002+n+3))
        plt.bar(x, selected_row5, width=bar_width, label="Data for" + str(2002+n+4))
        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width*4, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row2):
            plt.text(i - bar_width*3, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row3):
            plt.text(i - bar_width*2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row4):
            plt.text(i - bar_width, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row5):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+5))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+5
        print(n)
        rows_5(n)

def rows_10(n): 
    if n >= 11:
        print(n, "final n")
        dfm.iloc[n:n+10,[1, 2, 3, 4, 5]] 
        print('end')
        # dfm.plot.hist()
        # print(dfm.plot.hist())
    else: 
        print(n)
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        selected_row3 = dfm.iloc[n+2,[1, 2, 3, 4, 5]]
        selected_row4 = dfm.iloc[n+3,[1, 2, 3, 4, 5]]
        selected_row5 = dfm.iloc[n+4,[1, 2, 3, 4, 5]]
        selected_row6 = dfm.iloc[n+5,[1, 2, 3, 4, 5]]
        selected_row7 = dfm.iloc[n+6,[1, 2, 3, 4, 5]]
        selected_row8 = dfm.iloc[n+7,[1, 2, 3, 4, 5]]
        selected_row9 = dfm.iloc[n+8,[1, 2, 3, 4, 5]]
        selected_row10 = dfm.iloc[n+9,[1, 2, 3, 4, 5]]
        selected_row11 = dfm.iloc[n+10,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.1
        plt.bar(x-bar_width*10, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x-bar_width*9, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        plt.bar(x-bar_width*8, selected_row3, width=bar_width, label="Data for" + str(2002+n+2))
        plt.bar(x-bar_width*7, selected_row4, width=bar_width, label="Data for" + str(2002+n+3))
        plt.bar(x-bar_width*6, selected_row5, width=bar_width, label="Data for" + str(2002+n+4))
        plt.bar(x-bar_width*5, selected_row6, width=bar_width, label="Data for" + str(2002+n+5))
        plt.bar(x-bar_width*4, selected_row7, width=bar_width, label="Data for" + str(2002+n+6))
        plt.bar(x-bar_width*3, selected_row8, width=bar_width, label="Data for" + str(2002+n+7))
        plt.bar(x-bar_width*2, selected_row9, width=bar_width, label="Data for" + str(2002+n+8), color='green')
        plt.bar(x-bar_width, selected_row10, width=bar_width, label="Data for" + str(2002+n+9),color='red' )
        plt.bar(x, selected_row11, width=bar_width, label="Data for" + str(2002+n+10),color= 'brown')

        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width*10, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row2):
            plt.text(i - bar_width*9, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row3):
            plt.text(i - bar_width*8, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row4):
            plt.text(i - bar_width*7, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row5):
            plt.text(i - bar_width*6, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row6):
            plt.text(i - bar_width*5, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row7):
            plt.text(i - bar_width*4, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row8):
            plt.text(i - bar_width*3, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row9):
            plt.text(i - bar_width*2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row10):
            plt.text(i - bar_width, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row11):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+10))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+10
        print(n)
        rows_10(n)
        # dfm.plot.hist()
        # print(dfm.plot.hist())

def rows_20(n): 
    if n >= 0:
        print(n, "final n")
        selected_row1 = dfm.iloc[n,[1, 2, 3, 4, 5]] # this should be selecting the individual row and the B-F collum for the data
        selected_row2 = dfm.iloc[n+1,[1, 2, 3, 4, 5]]
        selected_row3 = dfm.iloc[n+2,[1, 2, 3, 4, 5]]
        selected_row4 = dfm.iloc[n+3,[1, 2, 3, 4, 5]]
        selected_row5 = dfm.iloc[n+4,[1, 2, 3, 4, 5]]
        selected_row6 = dfm.iloc[n+5,[1, 2, 3, 4, 5]]
        selected_row7 = dfm.iloc[n+6,[1, 2, 3, 4, 5]]
        selected_row8 = dfm.iloc[n+7,[1, 2, 3, 4, 5]]
        selected_row9 = dfm.iloc[n+8,[1, 2, 3, 4, 5]]
        selected_row10 = dfm.iloc[n+9,[1, 2, 3, 4, 5]]
        selected_row11 = dfm.iloc[n+10,[1, 2, 3, 4, 5]]
        selected_row12 = dfm.iloc[n+11,[1, 2, 3, 4, 5]]
        selected_row13 = dfm.iloc[n+12,[1, 2, 3, 4, 5]]
        selected_row14 = dfm.iloc[n+13,[1, 2, 3, 4, 5]]
        selected_row15 = dfm.iloc[n+14,[1, 2, 3, 4, 5]]
        selected_row16 = dfm.iloc[n+15,[1, 2, 3, 4, 5]]
        selected_row17 = dfm.iloc[n+16,[1, 2, 3, 4, 5]]
        selected_row18 = dfm.iloc[n+17,[1, 2, 3, 4, 5]]
        selected_row19 = dfm.iloc[n+18,[1, 2, 3, 4, 5]]
        selected_row20 = dfm.iloc[n+19,[1, 2, 3, 4, 5]]
        selected_row21 = dfm.iloc[n+20,[1, 2, 3, 4, 5]]
        categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
        # set bar lenght
        x = np.arange(len(categories))
        # Set the width of the bars
        bar_width = 0.045
        plt.bar(x-bar_width*20, selected_row1, width=bar_width, label="Data for" + str(2002+n))
        plt.bar(x-bar_width*19, selected_row2, width=bar_width, label="Data for" + str(2002+n+1))
        plt.bar(x-bar_width*18, selected_row3, width=bar_width, label="Data for" + str(2002+n+2))
        plt.bar(x-bar_width*17, selected_row4, width=bar_width, label="Data for" + str(2002+n+3))
        plt.bar(x-bar_width*16, selected_row5, width=bar_width, label="Data for" + str(2002+n+4))
        plt.bar(x-bar_width*15, selected_row6, width=bar_width, label="Data for" + str(2002+n+5))
        plt.bar(x-bar_width*14, selected_row7, width=bar_width, label="Data for" + str(2002+n+6))
        plt.bar(x-bar_width*13, selected_row8, width=bar_width, label="Data for" + str(2002+n+7))
        plt.bar(x-bar_width*12, selected_row9, width=bar_width, label="Data for" + str(2002+n+8), color='green')
        plt.bar(x-bar_width*11, selected_row10, width=bar_width, label="Data for" + str(2002+n+9),color='red' )
        plt.bar(x-bar_width*10, selected_row11, width=bar_width, label="Data for" + str(2002+n+10),color= 'brown')
        plt.bar(x-bar_width*9, selected_row12, width=bar_width, label="Data for" + str(2002+n+11))
        plt.bar(x-bar_width*8, selected_row13, width=bar_width, label="Data for" + str(2002+n+12))
        plt.bar(x-bar_width*7, selected_row14, width=bar_width, label="Data for" + str(2002+n+13))
        plt.bar(x-bar_width*6, selected_row15, width=bar_width, label="Data for" + str(2002+n+14))
        plt.bar(x-bar_width*5, selected_row16, width=bar_width, label="Data for" + str(2002+n+15))
        plt.bar(x-bar_width*4, selected_row17, width=bar_width, label="Data for" + str(2002+n+16))
        plt.bar(x-bar_width*3, selected_row18, width=bar_width, label="Data for" + str(2002+n+17))
        plt.bar(x-bar_width*2, selected_row19, width=bar_width, label="Data for" + str(2002+n+18), color='green')
        plt.bar(x-bar_width, selected_row20, width=bar_width, label="Data for" + str(2002+n+19),color='red' )
        plt.bar(x, selected_row21, width=bar_width, label="Data for" + str(2002+n+20),color= 'brown')

        # Add data labels above each bar
        for i, value in enumerate(selected_row1):
            plt.text(i - bar_width*20, value + 1, str(value), ha='center', va='bottom')
        '''
        for i, value in enumerate(selected_row2):
            plt.text(i - bar_width*19, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row3):
            plt.text(i - bar_width*18, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row4):
            plt.text(i - bar_width*17, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row5):
            plt.text(i - bar_width*16, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row6):
            plt.text(i - bar_width*15, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row7):
            plt.text(i - bar_width*14, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row8):
            plt.text(i - bar_width*13, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row9):
            plt.text(i - bar_width*12, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row10):
            plt.text(i - bar_width*11, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row11):
            plt.text(i - bar_width*10, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row12):
            plt.text(i - bar_width*9, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row13):
            plt.text(i - bar_width*8, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row14):
            plt.text(i - bar_width*7, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row15):
            plt.text(i - bar_width*6, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row16):
            plt.text(i - bar_width*5, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row17):
            plt.text(i - bar_width*4, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row18):
            plt.text(i - bar_width*3, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row19):
            plt.text(i - bar_width*2, value + 1, str(value), ha='center', va='bottom')
        for i, value in enumerate(selected_row20):
            plt.text(i - bar_width, value + 1, str(value), ha='center', va='bottom')
        '''    
        for i, value in enumerate(selected_row21):
            plt.text(i, value + 1, str(value), ha='center', va='bottom')
        plt.title("Data for " + str(2002+n)+'-'+str(2002+n+20))
        plt.ylabel("Values")
        plt.xlabel('Groups')
        plt.xticks(x, categories)
        plt.show()  
        n=n+10
        print(n)
    else: 
        print("error")


# Calls for the recursion 
# row_1(0)
# rows_2(0)
# rows_5(0)
# rows_10(0)
# rows_20(0)

# create data sets for the CARNAGE data classifies the US into 9 regions (in obreg collum):
# issue will have to use og data set, good news already have the stuff that i need to do it
# collum x for the obreg so need to be at 23 (increment form 0) over each year to create a adata set for each year
#Full data set (df)CODE, the following are the year break points 765, 1529, 2296, 3060, 3820, 4583, 5346, 6107, 6866, 7619, 8370, 
# 9123, 9875, 10627, 11378, 12138, 12899, 13667, 14430, 15185, 15931
#so will read over each line find what group it belongs to asign it to the apropriate data set for analysis 
# groups are 0-9 for the different regions

# Year breakpoints
year_breakpoints = [765, 1529, 2296, 3060, 3820, 4583, 5346, 6107, 6866, 7619, 8370, 
                    9123, 9875, 10627, 11378, 12138, 12899, 13667, 14430, 15185, 15931]

# Initialize a dictionary to hold datasets for each year
datasets = {}

# Iterate over each year

for i in range(len(year_breakpoints)):
    start_index = year_breakpoints[i-1] if i > 0 else 0
    end_index = year_breakpoints[i]
    
    # Create a dataset for the current year
    dfy = datasets[f"year_{i+1}"] = df.iloc[start_index:end_index]
    # grouping by the 'Carnege' column
    dfo = dfy.sort_values('obereg') # sorts dataset by obreg value
    # print(dfo)
    dfo0 = dfy[dfy['obereg'] == 0].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo0)
    dfo1 = dfy[dfy['obereg'] == 1].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo1)
    dfo2 = dfy[dfy['obereg'] == 2].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo2)
    dfo3 = dfy[dfy['obereg'] == 3].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo3)
    dfo4 = dfy[dfy['obereg'] == 4].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo4)
    dfo5 = dfy[dfy['obereg'] == 5].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo5)
    dfo6 = dfy[dfy['obereg'] == 6].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo6)
    dfo7 = dfy[dfy['obereg'] == 7].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo7)
    dfo8 = dfy[dfy['obereg'] == 8].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo8)
    dfo9 = dfy[dfy['obereg'] == 9].sort_values('obereg') # Creates a data frame for each year for the classifications
    # print(dfo9)

'''
#iterate over Canrage Clasification
'''

for i in range(len(year_breakpoints)):
    start_index = year_breakpoints[i-1] if i > 0 else 0
    end_index = year_breakpoints[i]
    
    # Create a dataset for the current year
    dfy = datasets[f"year_{i+1}"] = df.iloc[start_index:end_index]
    # Convert 'basic2021' column to numeric type, and removes errors
    dfy.loc[:, 'basic2021'] = pd.to_numeric(dfy['basic2021'], errors='coerce')
    # Sort the DataFrame by the 'basic2021' column
    dfc = dfy.sort_values('basic2021') # sorts dataset by basic2021 value 0-23, 27, 28, 32, 34, 35
    # print(dfc)
    dfc0 = dfy[dfy['basic2021'] == 0].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc0)
    dfc1 = dfy[dfy['basic2021'] == 1].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc1)
    dfc2 = dfy[dfy['basic2021'] == 2].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc2)
    dfc3 = dfy[dfy['basic2021'] == 3].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc3)
    dfc4 = dfy[dfy['basic2021'] == 4].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc4)
    dfc5 = dfy[dfy['basic2021'] == 5].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc5)
    dfc6 = dfy[dfy['basic2021'] == 6].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc6)
    dfc7 = dfy[dfy['basic2021'] == 7].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc7)
    dfc8 = dfy[dfy['basic2021'] == 8].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc8)
    dfc9 = dfy[dfy['basic2021'] == 9].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc9)
    dfc10 = dfy[dfy['basic2021'] == 10].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc10)
    dfc11 = dfy[dfy['basic2021'] == 11].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc11)
    dfc12 = dfy[dfy['basic2021'] == 12].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc12)
    dfc13 = dfy[dfy['basic2021'] == 13].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc13)
    dfc14 = dfy[dfy['basic2021'] == 14].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc14)
    dfc15 = dfy[dfy['basic2021'] == 15].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc15)
    dfc16 = dfy[dfy['basic2021'] == 16].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc16)
    dfc17 = dfy[dfy['basic2021'] == 17].sort_values('basic2021') # Creates a data frame for each year for the classifications
    print(dfc17)
    num_rows = len(dfc17)
    print("Number of rows:", num_rows)
        # histogran ineach year
    # ISSUE NEED TO COELATE THE DATA INTO A SINGULAR HISTOGRAM, 2nd GET RID OF NaN VALUES FOR THE GRAP
    # POSSIBLE SOLUTION, STORE CATGORIES AS VARIABLE AND PRINT AT THE END OF RECUSION LOOP UNDER THE IF STATEMENT 
    Grad_Total = 0
    International = 0
    Domestic = 0
    First_year = 0
    Degree_Master = 0
    Degree_Phd = 0
    Degree_Total = 0  
    def row_1(n):
        global Grad_Total
        global International
        global Domestic
        global First_year
        global Degree_Master
        global Degree_Phd 
        global Degree_Total 
        if n >= len(dfc17):
            print(n, "is this")
            print (Grad_Total)
            print (International)
            print (Domestic)
            print (First_year)
            print (Degree_Total)
            # Selecting the row and columns B-F from DataFrame dfm
            categories = ['GRAD Total', 'International', 'Domestic','First year','DEGREE TOTAL']
            values = [Grad_Total, International, Domestic , First_year, Degree_Total]  # Sample values for each category
            # print(selected_row) **** 
            # Plotting a histogram of the selected row
            # selected_row.plot.hist()
            plt.bar(categories, values)
            # Add data labels above each bar
            for i, value in enumerate(values):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+n))
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show() 
            print('end')
        else:
            print(n)
            # Selecting the row and columns from DataFrame dfc
            selected_row = dfc17.iloc[n,[10, 11, 12, 14, 15]] 
            # ISSUE NOT ICRIMENTING VALUE 
            Grad_Total += Grad_Total + pd.notnull(dfc17.iloc[n,[10]])
            International += International + pd.notnull(dfc17.iloc[n,[11]])
            Domestic += Grad_Total - International
            First_year += First_year + pd.notnull(dfc17.iloc[n,[12]])
            Degree_Master += Degree_Master + pd.notnull(dfc17.iloc[n,[14]])
            Degree_Phd += Degree_Phd+ pd.notnull(dfc17.iloc[n,[15]]) 
            Degree_Total += Degree_Master + Degree_Phd 
            # Plotting a histogram of the selected row 
            '''
            categories = ['GRAD Total', 'International','First year','DEGREE Master', 'DEGREE Phd']
            plt.bar(categories, selected_row)
            # Add data labels above each bar
            for i, value in enumerate(selected_row):
                plt.text(i, value + 1, str(value), ha='center', va='bottom')
            plt.title("Data for " + str(2002+n))
            plt.ylabel("Values")
            plt.xlabel('Groups')
            plt.show()
            '''  
            n = n + 1
            row_1(n)
    row_1(0)

    dfc18 = dfy[dfy['basic2021'] == 18].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc18)
    dfc19 = dfy[dfy['basic2021'] == 19].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc19)
    dfc20 = dfy[dfy['basic2021'] == 20].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc20)
    dfc21 = dfy[dfy['basic2021'] == 21].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc21)
    dfc22 = dfy[dfy['basic2021'] == 22].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc22)
    dfc23 = dfy[dfy['basic2021'] == 23].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc23)
    dfc27 = dfy[dfy['basic2021'] == 27].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc27)
    dfc28 = dfy[dfy['basic2021'] == 28].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc28)
    dfc32 = dfy[dfy['basic2021'] == 32].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc32)
    dfc34 = dfy[dfy['basic2021'] == 34].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc34)
    dfc35 = dfy[dfy['basic2021'] == 35].sort_values('basic2021') # Creates a data frame for each year for the classifications
    # print(dfc35)


#SO now with data frames for obreg regional clasifications and frames for carnagee now need to do histograms for them following the inital set
# LOOK AT ROWS K, L, M, O, P for 'GRAD Total', 'International', 'Domestic','First year','DEGREE Master', 'Degree PHD' 
# So rows 10, 11, 12, 14, 15 





# Calls for the recursion 
# row_1(0)
# rows_2(0)
# rows_5(0)
# rows_10(0)
# rows_20(0)


# CURRENT WORK GRAPHS for new organization

#Current Issue Histograms for new data are working but not right 
# FIX THEM

#CURRENT ISSUE 
#Data has visualization issues (overlaping text)


# OLD ISSUES
    # HISTOGRAMS NOT PRINTING OUT 
        # FIXED BY ADDING MATPLOT
    # Git HUB not working 
        # FIX USE THE FOLLOWING TO PUSH
            # git add /Users/Chris/Desktop/Codeing/PER/AIP
            # git commit -m "stuff"
            # git push origin main
    #Current Issue Histograms produced are not correct 
        #Fixed: using bar and group bar graphs    
    #Current Issue Histograms produced are not correct 
        #Sollution: redo the basic matplot code 