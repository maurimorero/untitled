
import re
import datetime


def reformat_date(dates):

    output = []
    for date in dates:
        output.append(datetime.datetime.strptime(re.sub(r"(st|th|rd)", "", date), "%d %b %Y").strftime("%Y-%m-%d"))
    return output


print(reformat_date(["6th Oct 2019", "20th Sep 1985", "16th Sep 1985"]))
