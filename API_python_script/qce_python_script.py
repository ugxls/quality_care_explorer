# Importing Libraries

import numpy as np
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Retrieving Datasets using API Keys

# Inpatient Rehablitation Facilities
inpatient_url = "https://data.cms.gov/provider-data/sites/default/files/resources/338f3022b522e13b6eb3c771aec03389_1733414708/Inpatient_Rehabilitation_Facility-Provider_Data_Dec2024.csv"

# Home Health Agencies
home_health_url = "https://data.cms.gov/provider-data/sites/default/files/resources/b1df2daa86922407689549b515d4635d_1733947506/HH_Provider_Jan2025.csv"

# Sending a GET request to download the files
response1 = requests.get(inpatient_url)
response2 = requests.get(home_health_url)

# Checking if the request was successful
if response1.status_code == 200 and response2.status_code == 200:

    # Saving the files locally
    with open('Inpatient_Rehabilitation_Facility_Provider_Data_Dec2024.csv', 'wb') as f1:
        f1.write(response1.content)
    print('file downloaded successfully.')

    with open('HH_Provider_Jan2025.csv', 'wb') as f2:
        f2.write(response2.content)
    print('file downloaded successfully.')

    # Loading the CSV file into a DataFrame
    inpatient_df = pd.read_csv('Inpatient_Rehabilitation_Facility_Provider_Data_Dec2024.csv')
    home_health_df = pd.read_csv('HH_Provider_Jan2025.csv')

    # Displaying the first few rows of the DataFrame
    print(inpatient_df.head())
    print(home_health_df.head())
else:
    print(f'Error: {response1.status_code} - {response1.text}')



# Exploring and Cleaning the Home Health Care Dataset

# Viewing the first five rows
home_health_df.head()

# Viewing the shape of the DataFrame
home_health_df.shape

# Viewing the columns in the DataFrame
home_health_df.columns

# Dropping columns that are not useful for this project

dropped_df = home_health_df.drop(columns = ["Numerator for how often the home health team began their patients' care in a timely manner",
                 "Denominator for how often the home health team began their patients' care in a timely manner",
                 "Numerator for how often the home health team determined whether patients received a flu shot for the current flu season",
                 "Denominator for how often the home health team determined whether patients received a flu shot for the current flu season",
                 "Numerator for how often patients got better at walking or moving around",
                 "Denominator for how often patients got better at walking or moving around",
                 "Numerator for how often patients got better at getting in and out of bed",
                 'Denominator for how often patients got better at getting in and out of bed',
                 'Numerator for how often patients got better at bathing',
                 'Denominator for how often patients got better at bathing',
                 "Numerator for how often patients' breathing improved",
                 "Denominator for how often patients' breathing improved",
                 'Numerator for how often patients got better at taking their drugs correctly by mouth',
                 'Denominator for how often patients got better at taking their drugs correctly by mouth',
                 'Numerator for Changes in skin integrity post-acute care: pressure ulcer/injury',
                 'Denominator for Changes in skin integrity post-acute care: pressure ulcer/injury',
                 'Numerator for how often physician-recommended actions to address medication issues were completely timely',
                 'Denominator for how often physician-recommended actions to address medication issues were completely timely',
                 'Numerator for Percent of Residents Experiencing One or More Falls with Major Injury',
                 'Denominator for Percent of Residents Experiencing One or More Falls with Major Injury',
                 'Numerator for Discharge Function Score',
                 'Denominator for Discharge Function Score',
                 'Numerator for Transfer of Health Information to the Provider',
                 'Denominator for Transfer of Health Information to the Provider',
                 'Numerator for Transfer of Health Information to the Patient',
                 'Denominator for Transfer of Health Information to the Patient',
                 'DTC Numerator', 'DTC Denominator',
                 'DTC Risk-Standardized Rate (Lower Limit)',
                 'DTC Risk-Standardized Rate (Upper Limit)',
                 'PPR Numerator',
                 'PPR Denominator',
                 'PPR Risk-Standardized Rate (Lower Limit)',
                 'PPR Risk-Standardized Rate (Upper Limit)',
                 'PPH Numerator',
                 'PPH Denominator',
                 'PPH Risk-Standardized Rate (Lower Limit)',
                 'PPH Risk-Standardized Rate (Upper Limit)',
                               ])

# Viewing the shape of the new DataFrame
dropped_df.shape

# Viewing the columns of the new DataFrame
dropped_df.columns

# Replacing the null indicator in the dataset with actual null values
dropped_df.replace('-', np.nan, inplace=True)

# Counting the number of null values in each column
dropped_df.isnull().sum()

# Giving columns short descriptive names

column_renames = {
    'Quality of patient care star rating': 'Patient Care Star Rating',
    'Footnote for quality of patient care star rating': 'Patient Care Star Footnote',
    "How often the home health team began their patients' care in a timely manner": 'Timely Care Start Rate',
    "Footnote for how often the home health team began their patients' care in a timely manner": 'Timely Care Start Footnote',
    'How often the home health team determined whether patients received a flu shot for the current flu season': 'Flu Shot Rate',
    'Footnote for how often the home health team determined whether patients received a flu shot for the current flu season': 'Flu Shot Footnote',
    'How often patients got better at walking or moving around': 'Walking Improvement Rate',
    'Footnote for how often patients got better at walking or moving around': 'Walking Improvement Footnote',
    'How often patients got better at getting in and out of bed': 'Bed Mobility Rate',
    'Footnote for how often patients got better at getting in and out of bed': 'Bed Mobility Footnote',
    'How often patients got better at bathing': 'Bathing Improvement Rate',
    'Footnote for how often patients got better at bathing': 'Bathing Improvement Footnote',
    "How often patients' breathing improved": 'Breathing Improvement Rate',
    "Footnote for how often patients' breathing improved": 'Breathing Improvement Footnote',
    'How often patients got better at taking their drugs correctly by mouth': 'Drug Adherence Rate',
    'Footnote for how often patients got better at taking their drugs correctly by mouth': 'Drug Adherence Footnote',
    'Changes in skin integrity post-acute care: pressure ulcer/injury': 'Skin Integrity Change',
    'Footnote Changes in skin integrity post-acute care: pressure ulcer/injury': 'Skin Integrity Footnote',
    'How often physician-recommended actions to address medication issues were completely timely': 'Timely Med Action Rate',
    'Footnote for how often physician-recommended actions to address medication issues were completely timely': 'Timely Med Action Footnote',
    'Percent of Residents Experiencing One or More Falls with Major Injury': 'Fall Injury Rate',
    'Footnote for Percent of Residents Experiencing One or More Falls with Major Injury': 'Fall Injury Footnote',
    'Discharge Function Score': 'Discharge Score',
    'Footnote for Discharge Function Score': 'Discharge Score Footnote',
    'Transfer of Health Information to the Provider': 'Info Transfer to Provider',
    'Footnote for Transfer of Health Information to the Provider': 'Provider Transfer Footnote',
    'Transfer of Health Information to the Patient': 'Info Transfer to Patient',
    'Footnote for Transfer of Health Information to the Patient': 'Patient Transfer Footnote',
    'DTC Observed Rate': 'DTC Obs Rate',
    'DTC Risk-Standardized Rate': 'DTC Risk Rate',
    'DTC Performance Categorization': 'DTC Performance Category',
    'Footnote for DTC Risk-Standardized Rate': 'DTC Rate Footnote',
    'PPR Observed Rate': 'PPR Obs Rate',
    'PPR Risk-Standardized Rate': 'PPR Risk Rate',
    'PPR Performance Categorization': 'PPR Performance Category',
    'Footnote for PPR Risk-Standardized Rate': 'PPR Rate Footnote',
    'PPH Observed Rate': 'PPH Obs Rate',
    'PPH Risk-Standardized Rate': 'PPH Risk Rate',
    'PPH Performance Categorization': 'PPH Performance Category',
    'Footnote for PPH Risk-Standardized Rate': 'PPH Rate Footnote',
    'How much Medicare spends on an episode of care at this agency, compared to Medicare spending across all agencies nationally': 'Medicare Spend Comparison',
    'Footnote for how much Medicare spends on an episode of care at this agency, compared to Medicare spending across all agencies nationally': 'Medicare Spend Footnote',
    'No. of episodes to calc how much Medicare spends per episode of care at agency, compared to spending at all agencies (national)': 'Episodes for Medicare Spend'
}

dropped_df.rename(columns=column_renames, inplace=True)

# Viewing the new column names
dropped_df.columns

# Saving the DataFrame to an Excel file
dropped_df.to_excel('QCE_HHCA_Dataset.xlsx', index=False)




# Exploring and Cleaning the IRF Dataset

# Viewing the first five rows of the DataFrame
inpatient_df.head()

# Checking the number of unique Measure Codes
inpatient_df['Measure Code'].nunique()

# Viewing the shape of the DataFrame
inpatient_df.shape

# Transforming the Dataframe to have the measure codes as columns and the Score as values
df_pivot = inpatient_df.copy().pivot_table(
    index=["CMS Certification Number (CCN)", "Provider Name", "Address Line 1", "City/Town", "State", "ZIP Code", "County/Parish", "Telephone Number", "CMS Region", "Footnote"],
    columns="Measure Code",
    values="Score",
    aggfunc="first"
).reset_index()

# Removing column index name (Measure Code)
df_pivot.columns.name = None

# Displaying the first five rows of the DataFrame
df_pivot.head()

# Viewing the shape of the new DataFrame
df_pivot.shape

# Viewing the columns of the new DataFrame
df_pivot.columns

# Dropping columns that are not useful for this project

columns_to_drop = [
    'I_011_05_DENOMINATOR',
    'I_011_05_NUMERATOR',
    'I_012_05_DENOMINATOR',
    'I_012_05_NUMERATOR',
    'I_013_01_DENOMINATOR',
    'I_013_01_NUMERATOR',
    'I_016_01_DENOMINATOR',
    'I_016_01_NUMERATOR',
    'I_021_01_DENOMINATOR',
    'I_021_01_NUMERATOR',
    'I_022_01_DENOMINATOR',
    'I_022_01_NUMERATOR',
    'I_023_02_DENOMINATOR',
    'I_023_02_NUMERATOR',
    'I_024_01_DENOMINATOR',
    'I_024_01_NUMERATOR',
    'I_025_02_DENOMINATOR',
    'I_025_02_NUMERATOR',
    'I_026_01_DENOMINATOR',
    'I_026_01_NUMERATOR'
]

df_cleaned = df_pivot.drop(columns=columns_to_drop)

# Viewing new columns
df_cleaned.columns

# Giving the columns short descriptive names

# Create a dictionary with the old column names as keys and the new column names as values
column_renames = {
    'I_006_01_CI_LOWER': 'CAUTI SIR Lower CI',
    'I_006_01_CI_UPPER': 'CAUTI SIR Upper CI',
    'I_006_01_COMP_PERF': 'CAUTI Comparative Performance',
    'I_006_01_DOPC_DAYS': 'CAUTI Catheter Days',
    'I_006_01_ELIGCASES': 'CAUTI Predicted Infections',
    'I_006_01_NUMERATOR': 'CAUTI Reported Infections',
    'I_006_01_SIR': 'CAUTI SIR',

    'I_015_01_CI_LOWER': 'CDI SIR Lower CI',
    'I_015_01_CI_UPPER': 'CDI SIR Upper CI',
    'I_015_01_COMP_PERF': 'CDI Comparative Performance',
    'I_015_01_DOPC_DAYS': 'CDI Patient Days',
    'I_015_01_ELIGCASES': 'CDI Predicted Infections',
    'I_015_01_NUMERATOR': 'CDI Reported Infections',
    'I_015_01_SIR': 'CDI SIR',

    'I_011_05_OBS_RATE': 'Self-Care Discharge Rate',
    'I_012_05_OBS_RATE': 'Mobility Discharge Rate',
    'I_026_01_OBS_RATE': 'Overall Self-Care & Mobility',

    'I_013_01_OBS_RATE': 'Falls with Major Injury Rate',
    'I_022_01_OBS_RATE': 'Pressure Injury Rate',
    'I_022_01_ADJ_RATE': 'Adjusted Pressure Injury Rate',

    'I_016_01_OBS_RATE': 'Flu Vaccination Rate',
    'I_023_02_OBS_RATE': 'COVID-19 Vaccination Rate',

    'I_017_01_PPR_PD_OBS_RATE': 'PPR Post-Discharge Rate',
    'I_017_01_PPR_PD_OBS_READM': 'PPR Post-Discharge Readmissions',
    'I_017_01_PPR_PD_RSRR': 'PPR Post-Discharge RSRR',
    'I_018_01_PPR_WI_OBS_RATE': 'PPR During Stay Rate',
    'I_018_01_PPR_WI_OBS_READM': 'PPR During Stay Readmissions',
    'I_018_01_PPR_WI_RSRR': 'PPR During Stay RSRR',

    'I_019_02_DTC_OBS_RATE': 'DTC Observed Rate',
    'I_019_02_DTC_RS_RATE': 'DTC Standardized Rate',
    'I_019_02_DTC_NUMBER': 'DTC Number of Discharges',

    'I_021_01_OBS_RATE': 'Med Review Follow-Up Rate',

    'I_020_01_MSPB_SCORE': 'MSPB Score',
    'I_020_01_MSPB_NUMB': 'MSPB Eligible Episodes',

    'I_024_01_OBS_RATE': 'Med List to Next Provider',
    'I_025_02_OBS_RATE': 'Med List to Patient'
}

column_renames.update({
    'I_017_01_PPR_PD_COMP_PERF': 'PPR Post-Discharge Comparative Performance',
    'I_017_01_PPR_PD_RSRR_2_5': 'PPR Post-Discharge RSRR Lower CI',
    'I_017_01_PPR_PD_RSRR_97_5': 'PPR Post-Discharge RSRR Upper CI',
    'I_017_01_PPR_PD_VOLUME': 'PPR Post-Discharge Volume',

    'I_018_01_PPR_WI_COMP_PERF': 'PPR During Stay Comparative Performance',
    'I_018_01_PPR_WI_RSRR_2_5': 'PPR During Stay RSRR Lower CI',
    'I_018_01_PPR_WI_RSRR_97_5': 'PPR During Stay RSRR Upper CI',
    'I_018_01_PPR_WI_VOLUME': 'PPR During Stay Volume',

    'I_019_02_DTC_COMP_PERF': 'DTC Comparative Performance',
    'I_019_02_DTC_RS_RATE_2_5': 'DTC Risk-Standardized Lower CI',
    'I_019_02_DTC_RS_RATE_97_5': 'DTC Risk-Standardized Upper CI',
    'I_019_02_DTC_VOLUME': 'DTC Volume'
})

df_cleaned.rename(columns=column_renames, inplace=True)

# Viewing the newly named columns
df_cleaned.columns

# Replacing the null indicator in the dataset with actual null values
df_cleaned.replace('-', np.nan, inplace=True)

# Saving the DataFrame to an Excel File
df_cleaned.to_excel('QCE_IRF_Dataset.xlsx', index = False)