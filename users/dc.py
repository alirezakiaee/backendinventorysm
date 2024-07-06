# import pandas as pd
# import numpy as np
# from scipy.stats import zscore
# from statsmodels.robust import mad
# import warnings
# from scipy.stats import zscore
# import nltk
# from nltk.chat.util import Chat, reflections

# def report_date_columns(df):
#     potential_date_columns = []
#     for col in df.select_dtypes(include=['object']).columns:
#         with warnings.catch_warnings():
#             warnings.simplefilter("ignore")
#             try:
#                 pd.to_datetime(df[col], infer_datetime_format=True)
#                 potential_date_columns.append(col)
#             except ValueError:
#                 continue
#     if potential_date_columns:
#         print(f"Potential date columns: {', '.join(potential_date_columns)}.")
#         print("Suggestion: Consider converting these columns to datetime objects for more accurate analysis.\n")
#     else:
#         print("No columns identified for potential date conversion.\n")

# def report_missing_values(df):
#     missing_values = df.isnull().sum()
#     missing_values = missing_values[missing_values > 0]
#     if not missing_values.empty:
#         print("Missing values detected in the following columns:")
#         for col, count in missing_values.items():
#             percentage = (count / len(df)) * 100
#             print(f"{col}: {count} missing values ({percentage:.2f}% of total)")
#         print("\nSuggestion: Evaluate whether to impute or remove missing values based on their significance and percentage.\n")
#     else:
#         print("No missing values detected.\n")

# def report_outliers(df):
#     numeric_columns = df.select_dtypes(include=['number'])
#     outlier_columns = []
#     for col in numeric_columns:
#         if col.endswith("_id") or df[col].nunique() < 10:  # Exclude ID-like or low cardinality numeric columns
#             continue
#         if (np.abs(zscore(df[col].dropna())) > 3).any():
#             outlier_columns.append(col)
#     if outlier_columns:
#         print(f"Columns with potential outliers based on Z-score: {', '.join(outlier_columns)}.")
#         print("Suggestion: Investigate these outliers. Consider applying transformations, clipping, or removing extreme values.\n")
#     else:
#         print("No significant outliers detected based on Z-score analysis.\n")

# def report_low_variance(df):
#     low_variance_cols = [col for col in df.select_dtypes(include=[np.number]).columns if df[col].var() < 0.01]
#     if low_variance_cols:
#         print(f"Low variance detected in numeric columns: {', '.join(low_variance_cols)}.")
#         print("Suggestion: Columns with low variance might not be very informative. Consider removing them if they don't contribute to analysis or prediction.\n")
#     else:
#         print("No columns with critically low variance detected.\n")

# def report_duplicate_rows_and_columns(df):
#     duplicate_rows = df.duplicated().sum()
#     print(f"Total duplicate rows found: {duplicate_rows}.")
#     print("Suggestion: Evaluate and potentially remove duplicate rows to clean the dataset.\n")

#     # Check for duplicate columns
#     transposed = df.T
#     duplicate_columns = transposed.index[transposed.duplicated()].tolist()
#     if duplicate_columns:
#         print(f"Duplicate columns detected: {', '.join(duplicate_columns)}.")
#         print("Suggestion: Review these columns for redundancy. Consider removing or combining them as needed.\n")
#     else:
#         print("No duplicate columns found.\n")

# def data_quality_report(df):
#     report = {}

#     print("Data Quality Report\n" + "-"*20)

#     report['date_columns'] = []
#     report['missing_values'] = {}
#     report['outliers'] = []
#     report['low_variance'] = []
#     report['duplicate_rows'] = 0
#     report['duplicate_columns'] = []

#     report['date_columns'] = report_date_columns(df)
#     report['missing_values'] = report_missing_values(df)
#     report['outliers'] = report_outliers(df)
#     report['low_variance'] = report_low_variance(df)
#     report['duplicate_rows'], report['duplicate_columns'] = report_duplicate_rows_and_columns(df)

#     return report

# def process_uploaded_file(file_path):
#     try:
#         df = pd.read_csv(file_path)
#         return data_quality_report(df)
#     except Exception as e:
#         print(f"Error processing file: {e}")
#         return {"error": str(e)}



# #--------------------------------
# import pandas as pd
# import numpy as np
# from scipy.stats import zscore
# from statsmodels.robust import mad
# import warnings
# from scipy.stats import zscore
# import nltk
# from nltk.chat.util import Chat, reflections

# def report_date_columns(df):
#     potential_date_columns = []
#     for col in df.select_dtypes(include=['object']).columns:
#         with warnings.catch_warnings():
#             warnings.simplefilter("ignore")
#             try:
#                 pd.to_datetime(df[col], infer_datetime_format=True)
#                 potential_date_columns.append(col)
#             except ValueError:
#                 continue
#     return potential_date_columns

# def report_missing_values(df):
#     missing_values = df.isnull().sum()
#     missing_values = missing_values[missing_values > 0]
#     result = {}
#     if not missing_values.empty:
#         for col, count in missing_values.items():
#             percentage = (count / len(df)) * 100
#             result[col] = {"count": int(count), "percentage": float(percentage)}
#     return result

# def report_outliers(df):
#     numeric_columns = df.select_dtypes(include=['number'])
#     outlier_columns = []
#     for col in numeric_columns:
#         if col.endswith("_id") or df[col].nunique() < 10:  # Exclude ID-like or low cardinality numeric columns
#             continue
#         if (np.abs(zscore(df[col].dropna())) > 3).any():
#             outlier_columns.append(col)
#     return outlier_columns

# def report_low_variance(df):
#     low_variance_cols = [col for col in df.select_dtypes(include=[np.number]).columns if df[col].var() < 0.01]
#     return low_variance_cols

# def report_duplicate_rows_and_columns(df):
#     duplicate_rows = df.duplicated().sum()
#     duplicate_columns = set(df.columns[df.columns.duplicated()])
#     return duplicate_rows, list(duplicate_columns)

# def data_quality_report(df):
#     report = {}

#     report['date_columns'] = report_date_columns(df)
#     report['missing_values'] = report_missing_values(df)
#     report['outliers'] = report_outliers(df)
#     report['low_variance'] = report_low_variance(df)
#     report['duplicate_rows'], report['duplicate_columns'] = report_duplicate_rows_and_columns(df)

#     return report

# def process_uploaded_file(file_path):
#     try:
#         df = pd.read_csv(file_path)
#         return data_quality_report(df)
    
#     except Exception as e:
#         print(f"Error processing file: {e}")
#         return {"error": str(e)}

import pandas as pd
import numpy as np
from scipy.stats import zscore
from statsmodels.robust import mad
import warnings


def report_date_columns(df):
    potential_date_columns = []
    for col in df.select_dtypes(include=['object']).columns:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                pd.to_datetime(df[col], infer_datetime_format=True)
                potential_date_columns.append(col)
            except ValueError:
                continue

    if potential_date_columns:
        return {
            'potential_date_columns': potential_date_columns,
            'message': "Consider converting these columns to datetime objects for more accurate analysis."
        }
    else:
        return {'message': "No columns identified for potential date conversion."}

def report_missing_values(df):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    report = {'missing_values': {}}
    if not missing_values.empty:
        report['message'] = "Evaluate whether to impute or remove missing values based on their significance and percentage."
        for col, count in missing_values.items():
            percentage = (count / len(df)) * 100
            report['missing_values'][col] = f"{count} missing values ({percentage:.2f}% of total)"
    else:
        report['message'] = "No missing values detected."

    return report

def report_outliers(df):
    numeric_columns = df.select_dtypes(include=['number'])
    outlier_columns = []
    for col in numeric_columns:
        if col.endswith("_id") or df[col].nunique() < 10:
            continue
        if (np.abs(zscore(df[col].dropna())) > 3).any():
            outlier_columns.append(col)
    if outlier_columns:
        return {
            'outlier_columns': outlier_columns,
            'message': "Investigate these outliers. Consider applying transformations, clipping, or removing extreme values."
        }
    else:
        return {'message': "No significant outliers detected based on Z-score analysis."}
def report_low_variance(df):
    low_variance_cols = [col for col in df.select_dtypes(include=[np.number]).columns if df[col].var() < 0.01]
    if low_variance_cols:
        return {
            'low_variance_columns': low_variance_cols,
            'message': "Columns with low variance might not be very informative. Consider removing them if they don't contribute to analysis or prediction."
        }
    else:
        return {'message': "No columns with critically low variance detected."}

def report_duplicate_rows(df):
    duplicate_rows_count = df.duplicated().sum()
    if duplicate_rows_count > 0:
        return {
            'duplicate_rows': duplicate_rows_count,
            'message': "Evaluate and potentially remove duplicate rows to clean the dataset."
        }
    else:
        return {
            'duplicate_rows': [],
            'message': "No duplicate rows found."
        }

def report_duplicate_columns(df):
    transposed = df.T
    duplicate_columns = transposed.index[transposed.duplicated()].tolist()
    if duplicate_columns:
        return {
            'duplicate_columns': duplicate_columns,
            'message': "Review these columns for redundancy. Consider removing or combining them as needed."
        }
    else:
        return {
            'duplicate_columns': [],
            'message': "No duplicate columns found."
        }
   
def data_quality_report(df):
    report = {}

    report['date_columns'] = report_date_columns(df)
    report['missing_values'] = report_missing_values(df)
    report['outliers'] = report_outliers(df)
    report['low_variance'] = report_low_variance(df)
    report['duplicate_rows']= report_duplicate_rows(df)
    report['duplicate_columns'] = report_duplicate_columns(df)

    return report



def process_uploaded_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return data_quality_report(df)
    
    except Exception as e:
        print(f"Error processing file: {e}")
        return {"error": str(e)}