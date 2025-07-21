import pandas as pd;
people = {
    "first_name" : ["corey","jane","John","Farrah"],
    "last_name" : ["smith","doe","doe","doe"],
    "age" : [24,43,12,22]
};

df = pd.DataFrame(people);

print(df[df["last_name"] == "doe"]);  #as the inner thing gives us a list of true,false and we use that to print the data ehich had true in the list

filt_last = df["last_name"] == "doe";
filt_age = df["age"] < 30;

print(df.loc[filt_last,"age"]);   #using loc to do the smae thing but now you can also select the colomns that u wanna see

print(df.loc[filt_last & filt_age]);  # & , | , ~ can be used as (and) , (or) , (not) to combine filters

