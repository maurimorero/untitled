
def reformatDate(dates):

    output=[]
    for date in dates:
        year= date[-4:]
        month= date[-8:-5]
        day=date[:-11]

        if (month=="Jan"):
            date = str(year) + "-01-" + str(day)
        elif (month =="Feb"):
            date = str(year) + "-02-" + str(day)
        elif (month == "Mar"):
            date = str(year) + "-03-" + str(day)
        elif (month == "Apr"):
            date = str(year) + "-04-" + str(day)
        elif (month == "May"):
            date = str(year) + "-05-" + str(day)
        elif (month == "Jun"):
            date = str(year) + "-06-" + str(day)
        elif (month == "Jul"):
            date = str(year) + "-07-" + str(day)
        elif (month == "Aug"):
            date = str(year) + "-08-" + str(day)
        elif (month == "Sep"):
            date = str(year) + "-09-" + str(day)
        elif (month == "Oct"):
            date = str(year) + "-10-" + str(day)
        elif (month == "Nov"):
            date = str(year) + "-11-" + str(day)
        elif (month == "Dec"):
            date = str(year) + "-12-" + str(day)
        if (len(date)==9):
            date= date[:8]+"0"+date[8:]
        output.append(date)

    return output

print (reformatDate(["6th Oct 2019","20th Sep 1985","16th Sep 1985"]))