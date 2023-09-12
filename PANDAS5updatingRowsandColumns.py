import pandas as pd
people = {
    "first":["Tony", "Peter", "Louis", "Dinosaur"],
    "last":["Stark", "Parker", "Didomenicis", "Girl"],
    "email":["ceo@starkindustries.com", "pparker@starkindustries.com", "ldidomenicis@gmail.com", "happydinogirl@gmail.com"]
}
df = pd.DataFrame(people)
#modifying data VIDEO 5
#https://www.youtube.com/watch?v=DCDe29sIKcE&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=5

df.columns = ['first_name', 'last_name', 'email']
                                                    ### Here we are relabelling the data with new names
                                                    ### printing df now will return with the new column names
                                                    ### instead of the old ones
df.columns = df.columns.str.replace('_', '')
                                                    ###Here i used .replace() to remove the
                                                    ### underscores in the labels
df.columns = [x.upper() for x in df.columns]
                                                    ###We used a for loop to and string modifiers to
                                                    ###capitalize the labels.
df.rename(columns={'FIRSTNAME':'FIRST', 'LASTNAME':'LAST'}, inplace=True)
                                                    ###You can use .rename() while specifying
                                                    ###column names to relabel individual columns
                                                    ###Remember that inplace=True makes it so that the
                                                    ###change actually happens to the dataframe
                                                    ###You can print the rename wihtout inplace=True,
                                                    ###But it would not make changes to the actual dataframe
#print(df.loc[1])
df.loc[1] = ['Peter', 'Porker', 'spiderham@storkindustries.com']
                                                    ###We can change a row on the datatable
                                                    ###by rewriting each data parameter
#print(df.loc[1])
df.loc[1, ['LAST', 'EMAIL']] = ['Parker', 'notspiderman@starkindustries.com']
                                                    ###We can select individual data parameters
                                                    ###To change by using a second parameter in loc
#print(df.loc[1])
df.at[1, 'EMAIL'] = 'maybespiderman@starkindustries.com'
#print(df.loc[1, 'EMAIL'])
                                                    ###For single parameter changes, we may use either
                                                    ###.loc[] or .at[]

df['LAST'] = df['LAST'].str.upper()
df['FIRST'] = df['FIRST'].str.upper()
df['EMAIL'] = df['EMAIL'].str.upper()
#print(df)

#Continue video from 17:30

#print(df['EMAIL'].apply(len))
                                                    ### This will return the lengths of the values in a column
#print(df.apply(len))
                                                    ### Rather than the individual value lengths, this will actually
                                                    ### Return the length of how many values are in the column
                                                    ### Think of it as the len function applied to the column
                                                    ### rather than the values in the column
print(df.map(len))
                                                    ###This will return the length of each indivdiual data point.
                                                    ###This used to be called .applymap()
                                                    ###map will apply functions to all items in the dataframe
#df['FIRST'] = df['FIRST'].map({'TONY' : 'CHRIS',
#                               'LOUIS' : 'MARY'})
#print(df)
                                                    ###This will replace the specified values
                                                    ###But anything not specified will be replaced with NaN
                                                    ###To replace individual values, and leave everything else
                                                    ###Intact, use .replace()
df['FIRST'] = df['FIRST'].replace({'TONY':'CHRIS',
                                   'LOUIS':'LUCAS'})
print(df)