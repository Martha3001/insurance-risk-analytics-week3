import pandas as pd

class DataAnalysis:
    """Handles analysis of solar data"""

    def __init__(self, data):
        """
        Initialize with data.
        Args:
            data (pd.DataFrame): Data to analyze
        """
        self.data = data

    def calculate_statistics(self):
        """
        Calculate basic statistics of the solar data.
        Returns:
            dict: A dictionary containing mean, median, and standard deviation
        """
        stats = {
            'mean': self.data.mean(),
            'median': self.data.median(),
            'std_dev': self.data.std()
        }
        return stats

    def filter_data(self, column, threshold):
        """
        Filter the data based on a threshold for a specific column.
        Args:
            column (str): Column name to filter on
            threshold (float): Threshold value for filtering
        Returns:
            pd.DataFrame: Filtered DataFrame
        """
        filtered_data = self.data[self.data[column] > threshold]
        return filtered_data
    
    def describe_data(self, column):
        """
        Provide a descriptive summary of the data.
        Args:
            column (str): Column name to describe
        Returns:
            pd.DataFrame: Summary statistics of the DataFrame
        """
        return self.data[column].describe() if column in self.data.columns else 0

    def data_summary(self):
        """
        Generate a summary of the dataset.
        Returns:
            dict: Summary containing shape, columns, and data types
        """
        summary = {
            'shape': self.data.shape,
            'columns': self.data.columns.tolist(),
            'dtypes': self.data.dtypes.to_dict()
        }
        return summary

    def columns_overview(self, columns):
        """
        Provide an overview of the columns in the DataFrame. 
        Args:
            columns (list): List of column names to overview
        """
        print("The first 5 rows")
        print(self.data[columns].head())
        # Overview of the columns
        print("----------------------------------")
        print("The last 5 rows")
        print(self.data[columns].tail())
        # Overview of the data types of the columns
        print("----------------------------------")
        print("The date type of the columns:")
        print(self.data[columns].dtypes)
        # Overview of the unique values in the columns
        print("----------------------------------")
        print("The count of unique values in the columns:")
        print(self.data[columns].nunique())
        # Check for missing values
        print("----------------------------------")
        print("Check for missing values:")
        print(self.data[columns].isna().sum())

    def show_unique_values(self, column):
        """
        Provide sorted unique values of the column.
        Args:
            column (str): Column name to describe
        Returns:
            pd.DataFrame: Sorted unique values of the column
        """
        # if column is list iterate through it
        if isinstance(column, list):
            unique_values = {col: self.data[col].unique() for col in column}
            return unique_values
        else:
            if column in self.data.columns:
                unique_values = self.data[column].unique()
                return sorted(unique_values)
            else:
                print(f"Column '{column}' does not exist in the DataFrame.")
                return None

    def convert_to_datetime_format(self, column):
        """
        Converts the specified column to datetime format in the DataFrame.
        
        Args:
            column (str): The column name to convert.
            
        Returns:
            None: Modifies the DataFrame in place.
        """
        self.data[column] = pd.to_datetime(self.data[column], format='mixed')

    def convert_year_to_datetime_format(self, column):
        """
        Converts the specified column to datetime format in the DataFrame.
        
        Args:
            column (str): The column name to convert.
            
        Returns:
            None: Modifies the DataFrame in place.
        """
        self.data[column] = pd.to_datetime(self.data[column], format='%Y')


    def convert_to_int(self, column):
        """
        Converts the specified column to int format in the DataFrame.
        
        Args:
            column (str): The column name to convert.
            
        Returns:
            None: Modifies the DataFrame in place.
        """
        self.data[column] = self.data[column].astype('Int64')

    def fill_with_not_specified(self, column):
        """
        Fills NaN values in the specified column with 'Not specified'.
        
        Args:
            column (str): The column name to fill.
            
        Returns:
            None: Modifies the DataFrame in place.
        """
        self.data.loc[(self.data[column].isna()), column] = 'Not specified'
        # return self.data

    def calculate_missing_value(self, column):
        """
        Calculates missing value
        
        Args:
            column (str): The column name to calculate.
            
        Returns:
            number: Number of missing value.
        """
        return self.data[column].isna().sum()
    
    def length_column_value(self, column, value):
        """
        Calculates occurance of the value in the column
        Args:
            column (str): The column name to calculate.
            value: The value in the column
        Returns:
            number: Number of occurance of value in column.
        """
        return len(self.data[self.data[column] == value])

    def drop_columns(self, columns):
        """
        Drop one or more columns from the data.
        Args:
            columns (str or list): Column name or list of column names to drop
        Returns:
            pd.DataFrame: DataFrame with specified columns dropped
        """
        self.data = self.data.drop(columns=columns, axis=1)
        return self.data