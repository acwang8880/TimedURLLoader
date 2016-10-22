from datetime import datetime
import webbrowser
#Let's also make a poem-generator! Anyway...

url = "www.google.com"
urls = [url, "www.yahoo.com", "www.youtube.com"]
array = str(datetime.now()).split(" ")
currtime = array[1][:5]
print(currtime)


data = {"00:29:00" : (url, "www.yahoo.com", "www.youtube.com"),
        "00:30:00" : ("www.twitter.com", "www.stackexchange.com")}


#Things to do:
# 1) Data structure
# example of a tuple 

# for s in urls:
#     webbrowser.open_new(s)



# 2) Input reader
# 3) webbrowser opens URL
# 4) Write to file
# 5) 