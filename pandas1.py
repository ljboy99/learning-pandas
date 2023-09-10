import pandas as pd
###CSV FILES ARE 2019 SURVEY DATA FROM
###https://insights.stackoverflow.com/survey
###PLACED IN DATA FOLDER
###i AM LEARNING FROM THIS PLAYLIST
###https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=1

#df = pd.read_csv('data/survey_results_public.csv')
#print(df)       ###Print out the entire database/table
#print(df.shape)  ### Print the size of the table (rows, cols)
#print(df.info()) ### return the range index
                 ### and what the data points are titled
pd.set_option('display.max_columns', 85) ### Allow python to display
### the maximum 85 columns at once
pd.set_option('display.max_rows', 85) ### Allow python to display
#maximium of 85 rows at once

schema_df = pd.read_csv('data/survey_results_schema.csv')
#print(schema_df) ###display the table in the schema csv
print(schema_df.head(10)) ###return the first 10 rows of table
###if left empty, .head() returns the first 5 rows
print(schema_df.tail()) ###return the last 5 rows
