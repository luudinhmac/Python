def week(i):
    switcher = {
        2: "Monday",
        3: "Tueday",
        4: "Webnesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
        8: "Sunday"
    }
    return switcher.get(i, "Invalid days")
print(week(0))