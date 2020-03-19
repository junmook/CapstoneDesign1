import requests
import random
import time
for i in range(10):
    value = random.randint(1, 100)
    url = 'https://api.thingspeak.com/update?api_key=3B66Q0KW97BGHQR7&field1='+str(value)
    r = requests.get(url)
    r.encoding = 'utf8'
    time.sleep(20)
#print(r.text)
#hello
