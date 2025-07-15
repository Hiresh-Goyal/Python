import pandas as pd;
people = {
    "first_name" : ["corey","jane","John"],
    "last_name" : ["smith","doe","doe"],
    "email" : ["CoreySmith@gmail.com","JaneDoe@gmail.com","JohnDoe@gmail.com"]
};

df = pd.DataFrame(people);

df.set_index('email',inplace=True);
print(df);
print(df.index);

print(df.loc["CoreySmith@gmail.com"]);  #loc uses label/index as its argument to display that row

df.reset_index(inplace=True);  #resets the index to again be 0,1,2 