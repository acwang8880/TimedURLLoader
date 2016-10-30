from datetime import datetime
import webbrowser
import os
import time
#Let's also make a poem-generator! Anyway...

# fields
url = "www.google.com"
urls = [url, "www.yahoo.com", "www.youtube.com"]
path = ".\database.txt"


array = str(datetime.now()).split(" ")
currtime = array[1][:5]
print("Current Time: " + currtime)


#create file if does not exist
# if not os.path.isfile(path):
# 	file = open("database.txt", "w")
# 	file.close


data = {"22:06" : [url, "www.yahoo.com", "www.youtube.com"],
        "00:30:00" : ["www.twitter.com", "www.stackexchange.com"]}


#Things to do:
# 1) Data structure
# example of a tuple 
# Remove a time if it maps to nothing

# for s in urls:
#     webbrowser.open_new(s)


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

        
add("22:03", "https://calcentral.berkeley.edu/dashboard")

printData()

remove("00:31", "www.github.com")
print("--------------------------")

printData()

# 2) Input reader
# 3) webbrowser opens URL
# 4) Write to file
def updateFile():
	filename = open(path, "w+") # "w+" means overwrite all contents of the file
	for key in data:
		filename.write("\n")
		filename.write(key)
		for url in data[key]:
			filename.write("--" + url)
	filename.close()

updateFile()

# 5) Read in file

#Reads given file name and puts data in array
def readFile(filename):
	file = open(filename)
	times_and_urls = file.readlines()
	file.close()
	times_and_urls = [group.split("--") for group in times_and_urls[1:]]
	#removes "\n" at the end of the URLs
	for group in times_and_urls[:len(times_and_urls)-1]:
		group[len(group)-1] = group[len(group)-1][:len(group[len(group)-1]) - 1]
	return times_and_urls

#Updates the data dictionary given a correctly formatted file
def updateData(filename):
	for group in readFile(filename):
		time = group[0]
		for url in group[1:]:
			add(time, url)

#Opens URL at given time. Not sure if this is how it works...
# Yeah that's the general idea!
"""
def run():
	on = True
	while on:
	 	array = str(datetime.now()).split(" ")
	 	currtime = array[1][:5]
	 	for time in data:
	 		print("Currtime: " + currtime)
	 		print("Set time: " + time)
	 		if time == currtime:
	 			for url in data[time]:
	 				webbrowser.open_new(url)
	 			on = False #must find way to open URL once then continue running
	 	time.sleep(60)		#this will be the solution to your question. aka pauses for a minute and checks again
	 			"""