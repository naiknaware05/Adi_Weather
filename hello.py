from flask import Flask,render_template,request
import requests
from pprint import pprint
import json 

app = Flask(__name__)

@app.route("/", methods =['POST','GET'])
def home_page():
	city='pune'
	if request.method == 'POST': 
		city = request.form['city'] 
	else: 
		city = 'pune'
	#city='pune'
	r =requests.post('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=94c63b9f329db27aa9faaefe532bfabe')
	
	
	# converting JSON data to a dictionary 
	recieved_obj = r.json() 

	#print(recieved_obj)

	##print('Main temp = ', recieved_obj['main']['temp'])

	data = {
	'temp' : recieved_obj['main']['temp'],
	'name' : recieved_obj['name'],
	'pressure' : recieved_obj['main']['pressure'],
	'humidity' : recieved_obj['main']['humidity'],
	'speed' : recieved_obj['wind']['speed'],
	'temp_min' : recieved_obj['main'][ 'temp_min'],
	'temp_max' : recieved_obj['main'][ 'temp_max'],
	'sunrise' : recieved_obj['sys']['sunrise'],
	'sunset' : recieved_obj['sys']['sunset']

	}

	#pprint(data)

	return render_template('insert.html', data=data)
	

	
if (__name__ == "__main__"):
	app.run()
	
	


