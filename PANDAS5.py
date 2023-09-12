import pandas as pd
###CSV FILES ARE 2019 SURVEY DATA FROM
###https://insights.stackoverflow.com/survey
###i AM LEARNING FROM THIS PLAYLIST
###https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=1
###Changes are from video #5

df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace = True)
                                                ###Here, .rename() is used to rename a
                                                ###column label ConvertedComp to SalaryUSD

df['Hobbyist']=df['Hobbyist'].map({'Yes':True,
                                   'No':False})
                                                ###Here we use .map and change all yes
                                                ###values to true and no values to false
print(df)