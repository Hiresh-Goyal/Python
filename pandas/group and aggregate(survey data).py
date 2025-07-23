import pandas as pd;
df = pd.read_csv("D:\Codes\data for pandas python\survey_results_public.csv",index_col="Respondent");
schema_df = pd.read_csv("D:\Codes\data for pandas python\survey_results_schema.csv",index_col="Column");

# print("Median of salary in USD = "+ str(df["ConvertedComp"].median()));

# print("\nMedian on the whole df :-");
# print(df.median());  #this looks for coloumns with numerical values and return their medians, gives error if coloumns with both numerica nd str types are present in the data frame

# print(df.describe());

# print(df["Hobbyist"].value_counts(normalize=True));  #gives the answer in form of percentage of people that answered that

country_grp = df.groupby(["Country"]);

# print(country_grp.get_group("India"));

# print(country_grp["SocialMedia"].value_counts());
# print(country_grp["SocialMedia"].value_counts().loc["India"]);
# print(country_grp["ConvertedComp"].median());
# print(country_grp["ConvertedComp"].agg(["median","mean"]));

# print(country_grp["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum())); #sum just counts how many true values were there so we just get how many people in that country do know python

# print(country_grp.size()); #prints the number of rows in a group




            #These below(upto lire 46) are 3 ways of printing % of people that know python



# ctr_knows_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python', na=False).value_counts(normalize=True));
# ctr_knows_python.rename({False:'%Don\'t Know Python', True:'%Know Python'}, inplace=True)

# print(country_grp["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum()/len(x)*100))

# print(ctr_knows_python);

country_respondents = df['Country'].value_counts();
country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum());
python_df = pd.concat([country_respondents, country_uses_python], axis='columns', sort=False);
python_df.rename(columns={'count': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True);
python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents']) * 100;
print(python_df);