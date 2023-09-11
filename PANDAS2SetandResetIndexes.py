import pandas as pd
people = {
    "first":["Tony", "Peter", "Louis", "Dinosaur"],
    "last":["Stark", "Parker", "Didomenicis", "Girl"],
    "email":["ceo@starkindustries.com", "pparker@starkindustries.com", "ldidomenicis@gmail.com", "happydinogirl@gmail.com"]
}
df = pd.DataFrame(people)
#print(df.set_index('email'))
                                #print the dataframe with the email as the index
df.set_index('email', inplace=True)
                                ###Set the index as the default index for the database
                                ###So if you would previously call 0 or 1 (the indices
                                ###to pull info, in this example, the email is the label
                                ###you'd call now
print(df.loc['ldidomenicis@gmail.com'])
df.reset_index(inplace=True)
                                ###This will revert back to using indices instead of a specified value
                                ###as the default label for your data
