from datetime import datetime
import webbrowser
import os
import time
import copy 	
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


data = {}


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
            
def add(t, url, destination):
    if t not in destination:
        destination[t] = [url]
    else:
        destination[t].append(url)
        
def remove(t, url):
    #what if time does not exist?
    #what if url does not exist? (question of existence)
    assert t in data
    assert url in data[t]
    data[t].remove(url)

def removeTime(t):
	assert t in data
	del data[t]
	print("Removed URLs associated with: " + t)   

def removeURL(url):
	for keys in data:
		for urls in data[keys]:
			 if urls == url:
			 	remove(keys, url)
			 	print("Removed url: " + url)
	print("No instance of " + url)
	


#Things to do:
# 1)     Data structure
# 1a)        Modify the data structure

# 2) Input reader
# 3) webbrowser opens URL
# 4) Write to file
def cleanData():
	newData = copy.deepcopy(data)
	for key in data:
		if not data[key]:
			del newData[key]
	return newData

def updateFile():

	data = cleanData()
	filename = open(path, "w+") # "w+" means overwrite all contents of the file
	for key in data:
		filename.write("\n")
		filename.write(key)
		for url in data[key]:
			filename.write("--" + url)
	filename.close()

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

def run():
	while True:
	 	array = str(datetime.now()).split(" ")
	 	currtime = array[1][:5]
	 	for t in data:
	 		# print("Currtime: " + currtime)
	 		# print("Set time: " + t)
	 		if t == currtime:
	 			for url in data[t]:
	 				webbrowser.open_new(url)
	 			#on = False #must find way to open URL once then continue running
	 			time.sleep(60)		#this will be the solution to your question. aka pauses for a minute and checks again
	 			
# option to change data before running
def main():
	in = input("View Data (V) | Add Entry (A) | Delete Entry (D) [time/url] | Cancel (X): ")
	switcher = {
		"V": lambda: printData,
		"A": lambda: add() #fill in
		"D": lambda: #parse data and find whether is time or url
		"X": lambda: run()
	} func = switcher.get(in, lambda: "nothing")
	return func()

# Begin testing
add("18:58", "www.google.com", data)
removeURL("www.google.com")
updateFile()

run()