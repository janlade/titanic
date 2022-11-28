import pandas as pd
from collections import Counter

def value_counts(df):
    for col in df.columns:
        print('Count is:',len(Counter(df[col])))
        print(df[col].value_counts(),end="\n")

def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # Print some summary information
        print ("Dein Datensatz hat " + str(df.shape[1]) + " columns.\n"      
            "Es gibt " + str(mis_val_table_ren_columns.shape[0]) +
              " Spalten mit missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns