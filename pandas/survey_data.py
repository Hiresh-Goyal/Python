import pandas as pd;
# pd.set_option("display.max_columns", 85);
# pd.set_option("display.max_rows", 85);

df = pd.read_csv("D:\Codes\data for pandas python\survey_results_public.csv",index_col="Respondent");
# print(df.shape);   #gives a tuple with (rows,coloumn)
# print(df.info());  #gives shape as well as data type and information about each coloumn

schema_df = pd.read_csv("D:\Codes\data for pandas python\survey_results_schema.csv",index_col="Column");
# print(df.head(10)); #prints the first ten rows

# print(df['Hobbyist'].value_counts());  #prints how many of each unique value is there in the coloumn

# print(df['Hobbyist']); #prints the hobbyist coloumn

schema_df.sort_index(inplace=True);  #sort the data by alphabetically arranging index

filt_salary = df["ConvertedComp"] < 10000;
filt_country = df["Country"] == "India";
# print(df.loc[filt_salary,["Country","EdLevel","ConvertedComp","WorkWeekHrs"]]);
# print(df.loc[filt_salary & filt_country,["Country","EdLevel","ConvertedComp","WorkWeekHrs"]]);

# print(((df["ConvertedComp"] < 10000) & (df["Country"] == "India")).value_counts());

#string methods can also be used

filt_lang_worked = df["LanguageWorkedWith"].str.contains("Python" , na = False); #na = False tells teh compiler that if the any coloumn is NaN then consider that as false that is do not print that row

# print(df.loc[filt_lang_worked,["Country","ConvertedComp","WorkWeekHrs","LanguageWorkedWith"]])

# df.rename(columns={"ConvertedComp" : "SalaryUSD"},inplace=True);
# print(df.columns);

# df2 = df["Country"].value_counts();
# print(df2[df2 > 1000]);     #prints those countries with their count whose count is >1000



                            #DEALING WITH MISSING VALUES

na_val = ["NA", "Missing", "Na"];
df_miss =pd.read_csv("D:\Codes\data for pandas python\survey_results_public.csv",index_col="Respondent",na_values=na_val); #now when loading the csv file those strings in the list will get converted to NaN

df["YearsCode"].unique(); #displays all unique values in that colomn, it contains int,string,NaN
#to find mean of this coloumn we gotta convert all of the values into float

df.replace({'YearsCode':'Less than 1 year'}, 0, inplace=True);
df.replace({'YearsCode':'More than 50 years'}, 51, inplace=True);
df["YearsCode"] = df["YearsCode"].astype(float);
# print("Mean of years since coding =");
# print(df["YearsCode"].mean());