# AlphaCare Insurance Solutions - Data Analysis Project

## Project Overview
This repository contains the code and documentation for the data analysis project conducted for **AlphaCare Insurance Solutions (ACIS)**. The goal of this project is to analyze historical car insurance claim data to optimize marketing strategies and identify "low-risk" customer segments for premium adjustments.

## Business Objective
- **Optimize Marketing Strategy**: Identify low-risk customer segments to reduce premiums and attract new clients.
- **Risk Assessment**: Analyze historical claim data to understand risk factors across provinces, vehicle types, and demographics.
- **Predictive Modeling**: Develop machine learning models to predict optimal premium values based on vehicle, owner, and location features.

## Repository Structure
```
## Repository Structure
├── data/
│ ├── raw/ # Raw datasets (original data files)
│ └── cleaned/ # Processed and cleaned datasets
├── scripts/
│ ├── data_loader.py # Script for loading and preprocessing data
│ ├── data_analysis.py # Script for exploratory data analysis (EDA)
│ ├── data_visualize.py # Script for generating visualizations
├── .gitignore # Specifies files to ignore in Git
├── README.md # This file
└── requirements.txt # Python dependencies
```


## Key Tasks
1. **Exploratory Data Analysis (EDA)**:
   - Assess data quality (missing values, outliers, inconsistencies).
   - Analyze loss ratios by province, gender, and vehicle type.
   - Visualize trends and correlations in claims and premiums.

2. **Data Version Control (DVC)**:
   - Track dataset versions for reproducibility.
   - Ensure compliance with auditing and regulatory requirements.

3. **A/B Hypothesis Testing**:
   - Validate hypotheses about risk differences (e.g., across provinces, genders).

4. **Predictive Modeling**:
   - Build models to predict optimal premiums using features like vehicle type, owner details, and location.

## Setup
1. Clone: `git clone https://github.com/Martha3001/insurance-risk-analytics-week3.git`
2. Create venv: `python -m venv .venv`
3. Activate: `.venv\Scripts\activate` (Windows)
4. Install: `pip install -r requirements.txt`
