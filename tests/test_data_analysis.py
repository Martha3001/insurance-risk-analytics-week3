import pandas as pd
import pytest
from scripts.data_analysis import DataAnalysis

def sample_df():
    return pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 1, 2, 2, None],
        'D': ['2020', '2021', '2022', '2023', '2024']
    })

def test_calculate_statistics():
    da = DataAnalysis(sample_df())
    stats = da.calculate_statistics()
    assert 'mean' in stats and 'median' in stats and 'std_dev' in stats
    assert stats['mean']['A'] == 3

def test_filter_data():
    da = DataAnalysis(sample_df())
    filtered = da.filter_data('A', 3)
    assert all(filtered['A'] > 3)

def test_describe_data():
    da = DataAnalysis(sample_df())
    desc = da.describe_data('A')
    assert desc['count'] == 5

def test_data_summary():
    da = DataAnalysis(sample_df())
    summary = da.data_summary()
    assert summary['shape'] == (5, 4)
    assert 'A' in summary['columns']

def test_show_unique_values():
    da = DataAnalysis(sample_df())
    unique = da.show_unique_values('C')
    assert set(unique) == {1.0, 2.0, None}

def test_convert_to_datetime_format():
    da = DataAnalysis(sample_df())
    da.convert_to_datetime_format('D')
    assert pd.api.types.is_datetime64_any_dtype(da.data['D'])

def test_convert_to_int():
    da = DataAnalysis(sample_df())
    da.convert_to_int('A')
    assert pd.api.types.is_integer_dtype(da.data['A'])

def test_fill_with_not_specified():
    da = DataAnalysis(sample_df())
    da.fill_with_not_specified('C')
    assert 'Not specified' in da.data['C'].values

def test_calculate_missing_value():
    da = DataAnalysis(sample_df())
    missing = da.calculate_missing_value('C')
    assert missing == 1

def test_length_column_value():
    da = DataAnalysis(sample_df())
    count = da.length_column_value('C', 1)
    assert count == 2

def test_drop_columns():
    da = DataAnalysis(sample_df())
    df2 = da.drop_columns(['B', 'C'])
    assert 'B' not in df2.columns and 'C' not in df2.columns
