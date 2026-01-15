import pandas as pd;
from datetime import datetime;

df = pd.read_csv("D:/Codes/data for pandas python/ETH_1h.csv");

#2methods of ocnverting string date to actual date

#1)
df["Date"] = pd.to_datetime(df["Date"],format = "%Y-%m-%d %I-%p");
# print(df.loc[0,"Date"].day_name());

#2) Doing it while importing file

d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p');
df = pd.read_csv("D:/Codes/data for pandas python/ETH_1h.csv", parse_dates=['Date'], date_parser=d_parser);

df["Day"] = df["Date"].dt.day_name();


# print(df["Date"].min());
# print(df["Date"].max());
# print(df["Date"].max() - df["Date"].min());

        #Filtering using date-time

# filt = (df["Date"] >= "2019") & (df["Date"] < "2020");
# print(df.loc[filt]);

# filt2 = (df["Date"] > pd.to_datetime("2019-01-01")) & (df["Date"] > pd.to_datetime("2019-06-01"));
# print(df.loc[filt2]);

                        #Setting Date as Index

df.set_index("Date",inplace = True);
df = df.sort_index();

# print(df.loc["2019"]);
# print(df.loc["2020-01" : "2020-02"]);

highs = df["High"].resample("D").max();
highs.plot(); #run in interactive window to see the graph

df2 = df.resample('W').agg({"Close" : "mean",
                            "High" : "max",
                            "Low" : "min",
                            "Volume" : "sum"});

print(df2); 
