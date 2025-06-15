import pandas as pd

class DataLoader:
    """Handles loading of solar data from various sources"""

    def load_and_save_as_csv(self, filepath):
        """
        Load data from a specified file and save it as a CSV file.
        Args:
            filepath (str): Path to the input file
        """
        csvfile = '../data/MachineLearningRating_v3.csv'
        try:
            # Load data from the specified file
            data = pd.read_csv(filepath, sep='|')
            # Save the loaded data as a CSV file
            data.to_csv(csvfile, index=False)
            print(f"Data loaded and saved as {csvfile}")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")