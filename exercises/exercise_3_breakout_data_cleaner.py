"""
Exercise 3: Breakout activity, the DataCleaner class

Work together in a breakout room to fill in the missing methods. You have a DataCleaner class that wraps a pandas
DataFrame. Add three methods, using Copilot's suggestions and Tab Completion to help, but
read every suggestion before you accept it.

  1. drop_missing()        - drop rows with any missing values
  2. drop_duplicate_rows() - remove duplicate rows
  3. summary()             - return summary statistics for the DataFrame

Once you have finished writing the methods using Copilot's Tab Completion, 
run this file and analyze how well Copilot wrote this DataCleaner class by answering the questions at the bottom of this file. 
"""

import pandas as pd


class DataCleaner:
    def __init__(self, dataframe):
        self.df = dataframe

    def drop_missing(self):
        # Drop rows with any missing values.
        pass

    def drop_duplicate_rows(self):
        # Remove duplicate rows.
        pass

    def summary(self):
        # Return summary statistics for the DataFrame.
        pass


if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    cleaner = DataCleaner(df)
    print(cleaner.df)



# once you have finished writing and running the code, discuss the following questions:
# 1. Where in your AI Studio project could Copilot genuinely save you time?
# 2. What's one risk you want to watch for as you use it?
# 3. What's one norm you want to commit to as a team for how you'll use it?

# Optional extension (if you finish early): Use GitHub Copilot to write a new Python file that:
#      1. Loads extension_clustering_data.csv
#      2. Cleans it the same way your DataCleaner class does (drop missing values, drop duplicates)
#      3. Fits a K-means model with 2 clusters on the age and score columns, using scikit-learn
