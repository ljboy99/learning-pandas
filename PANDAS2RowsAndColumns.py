import pandas as pd
people = {
    "first":["Tony", "Peter", "Louis", "Dinosaur"],
    "last":["Stark", "Parker", "Didomenicis", "Girl"],
    "email":["ceo@starkindustries.com", "pparker@starkindustries.com", "ldidomenicis@gmail.com", "happydinogirl@gmail.com"]
}
df = pd.DataFrame(people)
#print(df[['last', 'email']])
                              ###If you want to call multiple columns
                              ###you can input a list, don't forget the list brackets.
#print(df['email'])
#print(df.email)
                              ### same thing
#print(df.columns)
                              ### Will return with a list of columns in the dataset
#print(df.iloc[[0, 1]])
                              ###iloc (integer location) will return a specified row or range of rows according to the first parameter
#print(df.iloc[2, 2])
                              ### we can specify what column we want from the chosen rows with the second parameter, for example, this will only print ldidmonenicis@gmail.com
#print(df.loc[[0]])
                              ### This locates rows by label rather than by index.
                              ### It may seem similar, only because the rows are labelled by their index by default.
print(df.loc[[2, 3], 'email'])
                              ### As you can see, here I can call on 'email' instead of the index of the email column, and python will find it by name
