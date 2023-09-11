import pandas as pd
###CSV FILES ARE 2019 SURVEY DATA FROM
###https://insights.stackoverflow.com/survey
###i AM LEARNING FROM THIS PLAYLIST
###https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=1
###Changes are from video #3

df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

#print(schema_df.loc['MgrIdiot', 'QuestionText'])
                                ###Here we went to the schema file which told us what all the data means,
                                ###And had Python/Pandas navigate to the column titled MgrIdiot.
                                ###If we leave it to read that column alone, it will cutoff the text.
                                ###By adding in 'QuestionText' as the second parameter, we are telling it exactly
                                ###What we want it to readout to us.

print(schema_df.sort_index())
                                ###This will sort the columns in alphabetical order
                                ###You can reverse this by typing .sort_index(ascending = False)