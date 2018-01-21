from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/factory")
def factory():
	transactions = {
		"pizza": {"name": "pizza123", "date": "29/06/1996"}
	}
	return render_template('factory.html', title="Factory", transactions=transactions)

import json 
import random

@app.route("/submitPizza", methods=['POST', 'GET'])
def submitPizza():
	state_info = request.form['state'].encode('utf-8').lower()
	if(state_info=="production"):
		json_val = {
			  "$class": "org.acme.howto.Pizza",
			  "pizzaId": "p1zzA",
			  "timestamp": request.form['timestamp'].encode('utf-8'),
			  "date": request.form['date'].encode('utf-8'),
			  "state": request.form['state'].encode('utf-8').lower(),
			  "owner": "factory"
			}	
		transactions_val = {
			  "$class": "org.acme.howto.ChangeStateTo"+state_info.title(),
			  "pizza": "p1zzA"
			}
		r = requests.post('http://localhost:3000/api/Pizza', data=json_val) # create a new Pizza (random number)
		rT = requests.post('http://localhost:3000/api/ChangeStateTo'+state_info.title(), data=transactions_val)
	else:
		json_val = {
			  "$class": "org.acme.howto.Pizza",
			  "pizzaId": "p1zzA",
			  "timestamp": request.form['timestamp'].encode('utf-8'),
			  "date": request.form['date'].encode('utf-8'),
			  "state": request.form['state'].encode('utf-8').lower(),
			  "owner": "factory"
			}	
		transactions_val = {
			  "$class": "org.acme.howto.ChangeStateTo"+state_info.title(),
			  "pizza": "p1zzA"
			}
		rT = requests.post('http://localhost:3000/api/ChangeStateTo'+state_info.title(), data=transactions_val)
	return("The status code of the POST/PUT is: "+ str(rT.status_code) + " , " + str(rT.text))

@app.route("/changeOwner<owner>", methods=['POST','GET'])
def changeOwner(owner):
	return owner

@app.route("/wholesaler")
def wholesaler():
	return render_template('wholesaler.html', title="Wholesaler")

@app.route("/retailer")
def retailer():
	return render_template('retailer.html', title="Retailer")

@app.route("/customer")
def customer():
	return render_template('customer.html', title="Customer")

if __name__ == "__main__":
	app.run(debug=True)
