# AIP TRIMED 
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
df = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/Cleaned AIP Retention.xlsx")
# Specify the sheet name or index
Retention = 'Retention'  
Math = 'Math'
# Read data from the specified sheet
# dfr = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/Cleaned AIP Retention.xlsx", sheet_name=Retention) # Full Data set trimed for ease
# dfm = pd.read_excel("/Users/Chris/Desktop/Codeing/PER/AIP/Cleaned AIP Retention.xlsx", sheet_name=Math) #simplified math data


# Now you can work with the data in the DataFrame
# print(dfm.head())  # Print the first few rows of the DataFrame
# print(dfm) # prints the data frame

#Push to git  using git push -u origin main ()

#Go to the Math Sheet via pandas and write code to make the graphs 
# need to select the rows 2-22 then for each of those make a histogram
# repeate process for rows in patters of 1 year, 2 year, 5 year, 10 year, 20 year so 2-3, 4-5,... 2-4, 5-7,... 2-7, 8-12, ... 2-12, 13-22 ... 2-22 
# use code df.loc[row wanted],or for multiple df.iloc[first row wanted:last row wanted]
#df.iloc[:, [1, 2, 5]] Select columns in positions 1, 2 and 5 (firstcolumn is 0).

num_rows = len(df)
print("Number of rows:", num_rows)
print("rember to uncoment recursion, and carnagee orginization and comment this line")

# generic histograms
# CURRENTLY PRODUCES HISTOGRAMS BUT NOT OF PROPER TYPE TO BE FIXED ASAP 4-5-24
'''
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
# KEEEP TK COMEMNTED OUT 
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
''' 

# Calls for the recursion 
# row_1(0)
# rows_2(0)
# rows_5(0)
# rows_10(0)
# rows_20(0)

filtered_data = df[df['year'] > 2011] 

# Group by 'obereg' and 'year' and perform aggregation 

filtered_data = df[df['year'] > 2011] 

grouped_data = filtered_data.groupby(['obereg', 'year']).agg(
    n=('year', 'count'),
    total_grad=('grad_total', 'sum'),
    total_international=('grad_foreign', 'sum'),
    total_first=('grad_first', 'sum'),
    total_mast=('degree_m', 'sum'),
    total_phd=('degree_p', 'sum')
).reset_index()

# Calculate total_domestic and total_degree columns
grouped_data['total_domestic'] = grouped_data['total_grad'] - grouped_data['total_international']
grouped_data['total_degree'] = grouped_data['total_mast'] + grouped_data['total_phd']

grouped_data = grouped_data.sort_values(by=['obereg', 'year']) 

grouped_data['total_lost'] = (-grouped_data['total_grad'] + grouped_data['total_first'] -  

                             grouped_data['total_degree'] + grouped_data['total_grad'].shift(1))

grouped_data.dropna(inplace=True)

grouped_data = grouped_data[grouped_data['year'] > 2012]

total_atrition = grouped_data['total_lost']/grouped_data['total_grad'] * 100 
total_retention = 100 - total_atrition

print('Total ATRITION %', total_atrition)
print('Total RETENTION %', total_retention)

print(grouped_data['total_lost'])

unique_obereg = grouped_data['obereg'].unique()

# Plot each unique 'obereg' group separately
for obereg_value in unique_obereg:
    obereg_group = grouped_data[grouped_data['obereg'] == obereg_value]
    
    # Create a new figure for each plot
    plt.figure(figsize=(10, 6))
    
    # Plot the data
    plt.plot(obereg_group['year'], obereg_group['total_grad'], label='Total Graduates')
    plt.plot(obereg_group['year'], obereg_group['total_international'], label='Total International Graduates')
    plt.plot(obereg_group['year'], obereg_group['total_domestic'], label='Total Domestic Graduates')
    plt.plot(obereg_group['year'], obereg_group['total_first'], label='Total First Years')
    plt.plot(obereg_group['year'], obereg_group['total_degree'], label='Total Degrees Earned')
    plt.plot(obereg_group['year'], obereg_group['total_lost'], label='Retention Value')
    
    
    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Number of Graduates')
    plt.title(f'Total Graduates Over the Years - {obereg_value}')
    plt.legend(loc='upper right', bbox_to_anchor=(1.45, 1))
    plt.grid(True)
    
    # Show plot
    plt.tight_layout()
    plt.show()


# Group by 'obereg' and 'year' and perform aggregation 

grouped_data = filtered_data.groupby(['basic2021', 'year']).agg(
    n=('year', 'count'),
    total_grad=('grad_total', 'sum'),
    total_international=('grad_foreign', 'sum'),
    total_first=('grad_first', 'sum'),
    total_mast=('degree_m', 'sum'),
    total_phd=('degree_p', 'sum')
).reset_index()

# Calculate total_domestic and total_degree columns
grouped_data['total_domestic'] = grouped_data['total_grad'] - grouped_data['total_international']
grouped_data['total_degree'] = grouped_data['total_mast'] + grouped_data['total_phd']


print(grouped_data) 

import matplotlib.pyplot as plt

# Filter the grouped_data DataFrame
filtered_grouped_data = grouped_data[(grouped_data['basic2021'] >= 12) & (grouped_data['basic2021'] <= 20)]

# Get unique values in the 'basic2021' column after filtering
unique_basic2021 = filtered_grouped_data['basic2021'].unique()

# Plot each unique 'basic2021' group separately
for basic2021_value in unique_basic2021:
    basic2021_group = filtered_grouped_data[filtered_grouped_data['basic2021'] == basic2021_value]
    
    # Create a new figure for each plot
    plt.figure(figsize=(10, 6))
    
    # Plot the data
    plt.plot(basic2021_group['year'], basic2021_group['total_grad'], label='Total Graduates')
    plt.plot(basic2021_group['year'], basic2021_group['total_international'], label='Total International Graduates')
    plt.plot(basic2021_group['year'], basic2021_group['total_domestic'], label='Total Domestic Graduates')
    plt.plot(basic2021_group['year'], basic2021_group['total_first'], label='Total First Year')
    plt.plot(basic2021_group['year'], basic2021_group['total_degree'], label='Total Degrees')
    
    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Number of Graduates')
    plt.title(f'Total Graduates Over the Years - Basic2021: {basic2021_value}')
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.tight_layout()
    plt.show()


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

#Current Issue Histograms for new data are working, but only for 1 year at a time
# 

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
    # Histograms for new data are working but not right 
        # FIXED AND FUNCTIONAL
