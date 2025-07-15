import pandas as pd;
people = {
    "first_name" : ["corey","jane","John"],
    "last_name" : ["smith","doe","doe"],
    "age" : [24,43,12]
};

df = pd.DataFrame(people);
# print(df);
# print("\n\nage :-")
# print(df["age"]);   #can also use df.age
# print(df[["first_name","age"]]);

print(df.columns);

print(df.iloc[0]);  #prints first row
print(df.iloc[[0,1]]);

print(df.iloc[0,1]); #prints second coloumn of first row

print(df.loc)