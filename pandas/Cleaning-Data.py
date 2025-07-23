import pandas as pd;
import numpy as np;
people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
};

df = pd.DataFrame(people);


# print(df.dropna());  #Removes rows with missing values i.e. containing None or NaN
                     #Default arguments of dropna => axis = "index", how = "any"
                    
#axis = index or columns i.e. if there is a missing value then drop that row or drop that coloumn
#how  = any :- if any value is missing drop
#       all :- if all the values in a row or coloumn(acc to axis) drop
#subset = list of colomns u wanna check for missing values

# print(df.dropna(axis='index',how="any",subset=["email"]));
# print(df.dropna(axis='index',how="all",subset=["email","last"])); #either last name present or email present = keep the row i.e. if both emaila nd last are absent remove the row



                            #CUSTOM MISSING VALUES

#FOR CSV FILE IMPORT - CHECK survey_data.py

#FOR DATA SET YOU WROTE         
df.replace('NA', np.nan, inplace=True);
df.replace('Missing', np.nan, inplace=True);

# df.fillna("MISSING"); #replace all NaN and None values with MISSING

df["age"] = df["age"].astype(float); #change age from str to float
print(df);
