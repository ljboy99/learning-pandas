import pandas as pd

df = pd.read_csv("data/survey_results_public.csv", index_col='Respondent')
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.sort_values(["Country", "ConvertedComp"], ascending=[True, False], inplace = True)
#print(df[['Country', 'ConvertedComp']].head(50))

###.nlargest() will return the largest numerical values
###of a category
#print(df['ConvertedComp'].nlargest(10))
###You can also use nlargest to sort by placing the
###column title in the second argument
topearn = df.nlargest(10, "ConvertedComp")
print(topearn[["Country", "ConvertedComp", "Sexuality", "Trans"]])
print(schema_df)