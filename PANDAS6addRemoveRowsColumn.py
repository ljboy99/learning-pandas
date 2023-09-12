import pandas as pd
people = {
    "first":["Tony", "Peter", "Louis", "Dinosaur"],
    "last":["Stark", "Parker", "Didomenicis", "Girl"],
    "email":["ceo@starkindustries.com", "pparker@starkindustries.com", "ldidomenicis@gmail.com", "happydinogirl@gmail.com"]
}
df = pd.DataFrame(people)
#add / remove rows video 6
#https://www.youtube.com/watch?v=HQ6XO9eT-fc&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=6

df['fullname'] = df['first'] + ' ' + df['last']
###Create a new database column
df.drop(columns=['first', 'last'], inplace = True)
###Remove database column(s)

df['fullname'].str.split(' ', expand=True)
###Split the fullname into separate values
###the expand boolean will determine whether they will
###in separate columns. If false, they will be
###Together in lists.
df[['first', 'last']] = df['fullname'].str.split(' ', expand=True)
###Here we take the two columns we made and assign them labels
df.drop(columns='fullname', inplace=True)
###The last 3 minutes of this video is lost on me
###.append() doesn't work and removing a row
###by it's index also didn't work.
print(df)
