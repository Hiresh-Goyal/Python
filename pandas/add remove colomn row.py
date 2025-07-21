import pandas as pd;
people = {
    "first_name" : ["corey","jane","John","Farrah"],
    "last_name" : ["smith","doe","doe","doe"],
    "age" : [24,43,12,22]
};

df = pd.DataFrame(people);

df["Full_Name"] = df["first_name"] + " " + df["last_name"];     #Add Coloumn
print(df);

df.drop(columns=["first_name","last_name"],inplace=True);       #Remove Coloumn
print(df);

print(df["Full_Name"].str.split(" ",expand=True));

df[["First","Last"]] = df["Full_Name"].str.split(" ",expand=True);
print(df);

df.drop(columns="Full_Name",inplace=True);
print(df);

people2 = {
    "First" : ["Hiresh","Harshi"],
    "Last" : ["Goyal","Garg"],
    "age" : [18,21]
};

df2 = pd.DataFrame(people2);

df = pd.concat([df,df2],ignore_index=True);
print(df);

df.drop(index=3,inplace=True);
print(df);

df.drop(index=df[df["Last"] == "doe"].index,inplace=True);
print(df);