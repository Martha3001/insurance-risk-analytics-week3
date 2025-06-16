import matplotlib.pyplot as plt

class DataVisualize:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['x'], self.data['y'], marker='o')
        plt.title('Data Visualization')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()

    def plot_value_counts_distributions(self, columns, figsize=(10, 6), rotation=45, subplots=False):
        """
        Plots bar charts of value counts for specified columns in a DataFrame.
        
        Parameters:
        - data: pandas DataFrame
        - columns: str or list, column name(s) to plot
        - figsize: tuple, size of each figure (default is (10, 6))
        - rotation: int, rotation angle for x-axis labels (default is 45)
        - subplots: bool, whether to use subplots (default False)
        """
        # Convert single column name to list for uniform processing
        if isinstance(columns, str):
            columns = [columns]

        if subplots:
            # Create subplot grid
            n_cols = 2  # Number of columns in subplot grid
            n_rows = (len(columns) + 1) // n_cols  # Calculate needed rows
            
            fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
            fig.tight_layout(pad=5.0)
            
            # Flatten axes array for easy iteration
            axes = axes.flatten()
            
            for i, column in enumerate(columns):
                value_counts = self.data[column].value_counts()
            
                if i < len(axes):  # Ensure we don't exceed available subplots
                    value_counts.plot(kind='bar', ax=axes[i])
                    axes[i].set_title(f'{column} Distribution')
                    axes[i].set_xlabel(column)
                    axes[i].set_ylabel('Count')
                    axes[i].tick_params(axis='x', rotation=rotation)
        
            # Hide any unused subplots
            for j in range(i+1, len(axes)):
                axes[j].axis('off')
                
            plt.tight_layout()
            plt.show()

        else:
            for column in columns:
                value_counts = self.data[column].value_counts().sort_index()
                plt.figure(figsize=(figsize[0], figsize[1]//2))
                value_counts.plot(kind='bar')
                plt.title(f'{column} Distribution')
                plt.xlabel(column)
                plt.ylabel('Count')
                plt.xticks(rotation=rotation)
                plt.tight_layout()
                plt.show()

    def plot_pie_chart(self, columns, figsize=(8, 8)):
        """
        Plots a pie chart for the value counts of a specified column.
        
        Parameters:
        - column: str, column name to plot
        - figsize: tuple, size of the figure (default is (8, 8))
        """
        # Convert single column name to list for uniform processing
        if isinstance(columns, str):
            columns = [columns]

        for column in columns:
            value_counts = self.data[column].value_counts()
            plt.figure(figsize=figsize)
            patches, texts, autotexts = plt.pie(
                value_counts,
                labels=None,            # No labels on the chart
                autopct='%1.1f%%',
                startangle=90,
                pctdistance=1.15
            )
            plt.title(f'{column} Distribution')
            plt.ylabel('')
            plt.legend(patches, value_counts.index, title=column, loc="best") 
            plt.show()
            