print("\n\n")
# 1

from datetime import datetime
  
  
timestamp = 1545730073
dt_obj = datetime.fromtimestamp(1140825600)
  
print("date_time:",dt_obj)
print("type of dt:",type(dt_obj))



#spacing
print("\n")
#spacing

# 2

from datetime import datetime
  
  
timestamp = 1553367060
dt_obj = datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')
  
print("date:",dt_obj)