import pandas as pd;
people = {
    "first_name" : ["corey","jane","John","Farrah","Hiresh","Vibha"],
    "last_name" : ["smith","doe","doe","doe","Goyal","Singla"],
    "age" : [24,43,12,22,22,22]
};

df = pd.DataFrame(people);

df.sort_values(by="age",ascending=False,inplace=True);
print(df);

df.sort_values(by=["age","first_name"],inplace=True);   #if age is same then it will check for first name
print(df);

df.sort_values(by=["age","first_name"],ascending=[True,False], inplace=True);   #if age is same then it will check for first name, also age will be in asc and first name will be in desc
print(df);

print(df["age"].nlargest(2));  #only prints age coloumn
print(df.nlargest(2,"age"));   #prints whole row
