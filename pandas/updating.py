import pandas as pd;
people = {
    "first_name" : ["corey","jane","John","Farrah"],
    "last_name" : ["smith","doe","doe","doe"],
    "age" : [24,43,12,22]
};

df = pd.DataFrame(people);

df.columns = [x.upper() for x in df.columns]; #makes the names of each colomn to be uppercase

df.columns = [x.lower() for x in df.columns]; #makes the names of each colomn to be lowercase

df.rename(columns={"first_name" : "first",
                   "last_name" : "last"},inplace=True);  #changes first_name to be first etc i.e. u can pass a dict to rename stuff

# df.loc[2] = ["Hiresh","Goyal",18];
# print(df);

# df.loc[2,["first"]] = ["Harshita"];
# print(df);

                        #APPLY(Series) - applies a func to all members of a series
                        #you can use any function even those that u have written
# print(df["last"].apply(len));

#                         #APPLY(DF) - 

# print(df.apply(len));  #will give len on colomns
# print(len(df["last"]));
# print(df.apply(len,axis="columns")); #will aply len on rows
# print(df.apply(pd.Series.min)); #returns the minimum value fom that col


                        #APPLYMAP(only for DF)

# print(df.applymap(len));     #Would apply len func to each cell of DF but as int(age) has no length it gives error

                        #MAP

print(df["first"].map({"corey" : "Karen","jane" : "Tom","Farrah" : "Meenu"})); #u need to do inplace = True for it to reflect in DF, Those that you do not put in this dict will get converted to NaN

                        #REPLACE

print(df["first"].replace({"corey" : "Karen","jane" : "Tom","Farrah" : "Meenu"})); #u need to do inplace = True for it to reflect in DF