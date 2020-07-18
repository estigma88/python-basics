# import datetime
from datetime import date
import time
import camelcase

today = date.today()
timestamp=time.time()
print(today)
print(timestamp)

camel = camelcase.CamelCase()

text = 'hello world'

print(camel.hump(text))