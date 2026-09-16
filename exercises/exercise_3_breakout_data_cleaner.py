"""
Exercise 3: Breakout activity, the DataCleaner class

Work with a partner. You have a DataCleaner class that wraps a pandas
DataFrame. Add three methods, using Copilot's suggestions to help, but
read every suggestion before you accept it.

  1. drop_missing()        - drop rows with any missing values
  2. drop_duplicate_rows() - remove duplicate rows
  3. summary()             - return summary statistics for the DataFrame

Requirement: accept at least two Copilot suggestions, reject at least
one, and write one comment that improves a suggestion Copilot gave
you.

Before you finish: find one suggestion that was wrong or incomplete
and fix it yourself. Be ready to explain what it got wrong.
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
