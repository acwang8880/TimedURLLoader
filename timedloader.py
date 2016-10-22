from datetime import datetime
import webbrowser
#Let's also make a poem-generator! Anyway...

url = "www.google.com"
# webbrowser.open_new(url)

array = str(datetime.now()).split(" ")
date = array[0]
time = array[1]

print(date)
print(time)