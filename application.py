from flask import Flask, render_template, request
import requests
app = Flask(__name__)

get_pizza_url = "http://localhost:3000/api/Pizza/pizza"
post_pizza_url = "http://localhost:3000/api/Pizza/pizza"
post_entity_url = "http://localhost:3000/api/Entity"
post_pizza_json = {
  "$class": "org.acme.howto.Pizza",
  "pizzaId": "3901",
  "timestamp": "",
  "date": "",
  "state": "production",
  "owner": {
    "$class": "org.acme.howto.Entity",
    "entityId": "3592",
    "entityType": "",
    "firstName": "",
    "lastName": ""
  }
}
'''
To create Pizza: 
- timestamp (now)
- date (now)
- state (dropdown)
- owner (factory)
TO JSON AND THEN POST TO API 
pizzaId: "pizza"
entityId: "factory"
entityType: "factory"
'''

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
	random_val = str(random.randint(1, 9999))
	state_info = request.form['state'].encode('utf-8').lower()
	json_val = {
		  "$class": "org.acme.howto.Pizza",
		  "pizzaId": random_val,
		  "timestamp": request.form['timestamp'].encode('utf-8'),
		  "date": request.form['date'].encode('utf-8'),
		  "state": request.form['state'].encode('utf-8').lower(),
		  "owner": "factory"
		}	
	transactions_val = {
		  "$class": "org.acme.howto.ChangeStateTo"+state_info.title(),
  		  "pizza": random_val
		}
	r = requests.post('http://localhost:3000/api/Pizza', data=json_val) # create a new Pizza (random number)
	rT = requests.post('http://localhost:3000/api/ChangeStateTo'+state_info.title(), data=transactions_val)
	return("The status code of the POST is: "+ str(r.status_code) + " , " + str(rT.status_code) + " , " + str(rT.text))

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
