SEED ML Internship — Synthetic Datasets
========================================

All datasets are synthetic and generated for educational purposes.
Each file contains exactly 10,000 records.

Files
-----
project1_internship_retention.csv
  Target: Returned (Yes/No)
  Features: Department, Internship_Duration_Weeks, Feedback_Score,
            Supervisor_Rating, Commute_Distance_km, Monthly_Stipend_XAF,
            Remote_Work_Option

project2_system_anomaly.csv
  Target: Label (Normal / Suspicious)
  Features: Login_Attempts_Per_Hour, CPU_Usage_Percent, Data_Transfer_MB,
            Access_Hour, Active_Sessions, Error_Count
  Note: Drop the Label column before training unsupervised models.
        It is provided for post-hoc evaluation only.

project3_market_segmentation.csv
  Task: Clustering (unsupervised)
  Features: Age, Distance_From_Market_km, Monthly_Spending_XAF,
            Visit_Frequency_Monthly, Category_Preference, Payment_Method,
            Items_Per_Visit, Years_As_Customer
  Note: True_Segment column is for evaluation only — do NOT use as input.

project4_waste_generation.csv
  Target: Weekly_Waste_Weight_kg
  Features: Population_Density_per_km2, Number_of_Businesses,
            Avg_Household_Size, Market_Present, Industrial_Zone,
            Collection_Frequency_per_Week, Month

Tools
-----
  Python 3.x, Pandas, Scikit-learn, Matplotlib/Seaborn, Streamlit

Region
------
  Cameroon — North-West Region
  SEED Training Institute
