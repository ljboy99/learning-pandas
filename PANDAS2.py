import pandas as pd
###CSV FILES ARE 2019 SURVEY DATA FROM
###https://insights.stackoverflow.com/survey
###i AM LEARNING FROM THIS PLAYLIST
###https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=1
###Changes are from video #2

df = pd.read_csv('data/survey_results_public.csv')
#print(df)
                            ###Print out the entire database/table
#print(df.shape)
                            ### Print the size of the table (rows, cols)
#print(df.info())
                            ### return the range index
                            ### and what the data points are titled

schema_df = pd.read_csv('data/survey_results_schema.csv')

#print(df['Hobbyist'].value_counts())
                            ### Remember you can narrow down specific columns by calling them in brackets
                            ### 'value_counts()' will return the total in which each different value appears
print(df.loc[0:20, 'Hobbyist':'Employment'])
                            ###when you want a range / to slice, it does not stay in brackets
                            ###you can do this to both rows and columns for their names or indices

