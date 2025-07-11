months = {
    "Jan" : "January",   #Key : Value pairs
    "Feb" : "February",  #Duplicate keys are not allowed
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(months["Nov"])
print(months.get("Nov"))
print(months.get("abc","Invalid Key"))  #default string can be given which will be printed if key is not present in our dictionaries