var url, urls, path, data;
url = "www.google.com";
urls = [ url, "www.yahoo.com", "www.youtube.com" ];
filepath = "./database.txt";

data = [];

function contains(element, list) {
    for (i = 0; i<list.length; i++) {
		if (list[i] === element) {
			return true;
		}
	}
	return false;
}

function add(t, url, destination) {
	if (!(t in data)) {
		destination[t] = [url];
	} else {
		destination[t].push(url);
	}
}

//check existence of recovery file. If not, makes a new recovery file
function readSingleFile(e) {
	var file = e.target.files[0];
	if (!file) {
	  return;
	}
	var reader = new FileReader();
	reader.onload = function(e) {
	  var contents = e.target.result;
	  displayContents(contents);
	};
	reader.readAsText(file);
}

function displayContents(contents) {
	var element = document.getElementById('file-content');
	element.innerHTML = contents;
}

document.getElementById('file-input')
  .addEventListener('change', readSingleFile, false);


function remove(t, url, data) {
    if (!(t in data) || !contains(url, data[t])) {
		throw "No URL opening at that time";
	} else {
		var i = data.indexOf(url);
		data[t].splice(i);
	}
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function run() {
	while (true) {
		var d, currtime, hour, minute;
		d = new Date();
		hour = d.getHours();
		minute = d.getMinutes();
		currtime = hour.toString() + ":" + minute.toString();
		for (t in data) {
			if (t === currtime) {
				for (i = 0; i<data[t].length; i++) {
					window.open(data[t][i]);
				}
				sleep(60000);
			}
		}
	}
}