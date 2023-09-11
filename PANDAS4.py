import pandas as pd
###CSV FILES ARE 2019 SURVEY DATA FROM
###https://insights.stackoverflow.com/survey
###i AM LEARNING FROM THIS PLAYLIST
###https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=1
###Changes are from video #4

df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

high_salary = (df['ConvertedComp']) > 70000
                                            ###We created a variable to filter
                                            ###for people who make more than $70,000 a year
#print(df.loc[high_salary, ['ConvertedComp', 'LanguageWorkedWith']])
                                            ###We called on the variable, and asked to see the
                                            ###convertedcomp and the languages they said they work with
countries = ['United States', 'Portugal', 'Canada']
filt = df['Country'].isin(countries)
                                            ###We made a list of countries and used it to specify
                                            ###The contries surveyed
#print(df.loc[filt & high_salary, ['Country', 'ConvertedComp']])
                                            ###Video called for me to use the country filter
                                            ###I used the bitwise & to use both filters
filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
print(df.loc[filt, 'LanguageWorkedWith'])
                                            ###We now defined filt as being any string that contains
                                            ###The word python in the column 'LanguageWorkedWith'
                                            ###All results will be ones that include Python