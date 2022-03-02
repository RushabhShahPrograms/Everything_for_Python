# 1) Current Time Zone

from datetime import *
import pytz

IN=pytz.timezone('Asia/Kolkata')
datetime_IN=datetime.now(IN)
print("INDIA time: ",datetime_IN.strftime("%H:%M:%S"))


# 2) Current Time

from datetime import datetime
now_method = datetime.now()
currenttime=now_method.strftime("%H:%M:%S")
print("Current Time: ",currenttime)