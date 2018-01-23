import csv
import os
from datetime import datetime

def start():
    start = raw_input("""\nHello, what would you like to do?
        \nto create a new file, type "new".
        \nto add to your file, hit Enter. """)
    if start != "new":
        overtimer()
    elif start == "new":
        create_overtimer_file()


# file starter
def create_overtimer_file():
    file = open('overtimer.csv', "wb")
    writing = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    writing.writerow(('Date', 'Hours', 'Overtime'))
    file.close()
    print "\nYour csv file has been created"



def overtimer():
    overtime = 0
    os.system('clear')
    date = raw_input("\nWhich day are you recording? Please use format MMM DD YYYY \n")

    date_sorted = datetime.strptime(date, '%b %d %Y' ).date()  
    hours = float(raw_input("""\nHow many hours did you work? If it was a weekend, simply type '0'.
If you worked on the weekend, be ashamed of yourself, then log your hours normally. \n"""))

    if hours > 8.5:
        overtime = hours - 8.5
    elif hours == 0:
        overtime = "weekend"
    else:
        overtime = 0

    file = open('overtimer.csv', "a")
    writing = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    # file writer
    work_data = (date_sorted, hours, overtime)

    print "Thanks for logging!"

    # writing & closing
    writing.writerow(work_data)
    redo = raw_input("\nIf you'd like to log some new data, hit any key. Otherwise, type 'x'. \n")
    if redo != "x":
        overtimer()


start()



# ISSUES:
# Dates not in order
# you can update only the latest csv you created
