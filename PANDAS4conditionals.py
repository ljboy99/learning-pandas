import pandas as pd
people = {
    "first":["Tony", "Peter", "Louis", "Dinosaur",
             "John", "Jane"],
    "last":["Stark", "Parker", "Didomenicis", "Girl",
            "Doe", "Doe"],
    "email":["ceo@starkindustries.com", "pparker@starkindustries.com",
             "ldidomenicis@gmail.com", "happydinogirl@gmail.com",
             "johndoe@gmail.com", "janedoe@gmail.com"]
}
df = pd.DataFrame(people)
filt = df['last'] == 'Doe'
                    ###If we were to simply print the filt variable we made,
                    ###it would return the True/False values
                    ###for if each name is Doe or not.
#print(df[filt])
                    ###By processing filt through the dataframe
                    ###We are asking it for the true values in the variable
filt = (df['last'] == 'Doe') & (df['first'] == 'John')
                    ###Now we are asking for data where we match
                    ###both the first and last name to specific values
                    ###In pandas, we can't use the python and/or
                    ###But we can use bitwise operators
#print(df[filt])

filt = (df['last'] != 'Doe') & (df['first'] != 'Peter')
                    ###Now here we specify that we both dont want
                    ###the Doe's or peter to show up

print(df[filt])
                    ###if we add a - in front of the filter
                    ###it will return the opposite
print(df[-filt])