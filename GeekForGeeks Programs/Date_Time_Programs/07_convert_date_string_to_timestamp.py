import time
import datetime

string = "20/02/2022"
print(time.mktime(datetime.datetime.strptime(string,"%d/%m/%Y").timetuple()))