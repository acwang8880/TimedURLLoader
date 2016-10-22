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


data = {"00:29" : [url, "www.yahoo.com", "www.youtube.com"],
        "00:30" : ["www.twitter.com", "www.stackexchange.com"]}

def printData():
    for time in data:
        print(time)
        for thing in data[time]:
            print("   " + thing)
            
def add(time, url):
    if time not in data:
        data[time] = [url]
    else:
        data[time].append(url)
        
def remove(time, url):
    #what if time does not exist?
    #what if url does not exist? (question of existence)
    assert time in data
    assert url in data[time]
    data[time].remove(url)

    
add("00:31", "www.github.com")


#Things to do:
# 1)     Data structure
# 1a)        Modify the data structure

        
add("00:31", "www.calcentral.berkeley.edu")

printData()

remove("00:31", "www.github.com")
print("--------------------------")

printData()
# for s in urls:
#     webbrowser.open_new(s)


# 2) Input reader
# 3) webbrowser opens URL
# 4) Write to file
# 5) 