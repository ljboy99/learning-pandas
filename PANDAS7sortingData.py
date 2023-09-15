import pandas as pd

def sep():
    print('-'*50)

people = {
    'first': ['Tony', 'Peter', 'Louis', 'John', 'Mark'],
    'last' : ['Stark', 'Parker', 'Didomenicis', 'Doe', 'Doe'],
    'email': ['ceo@starkindustries.com', 'pparker@starkindustries.com',
              'ldidomenicis@gmail.com', 'jdoe@gmail.com', 'mdoe@gmail.com']
}

df = pd.DataFrame(people)
print(df)
sep()
                                        ###Sort values by last name by using .sort_values
print(df.sort_values(by='last'))
sep()
                                        ###Sort by last name in desceding order
                                        ###If two people share a last name, list
                                        ###them alphabetically by first name.
print(df.sort_values(by=['last', 'first'], ascending = [False, True]))
sep()
                                        ###Indices remain the same when you
                                        ###use .sort_values. You can
                                        ###sort the data by their indices
print(df.sort_index())
sep()
                                        ###You can sort the values in a single column
print(df['last'].sort_values())