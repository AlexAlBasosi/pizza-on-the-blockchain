from flask import Flask, render_template, request
import requests
app = Flask(__name__)

get_pizza_url = "http://localhost:3000/api/Pizza/pizza"
post_pizza_url = "http://localhost:3000/api/Pizza/pizza"
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

@app.route("/submitPizza", methods=['POST', 'GET'])
def submitPizza():
	json_val = {
	  "$class": "org.acme.howto.Pizza",
	  "pizzaId": "random",
	  "timestamp": request.form['timestamp'].lower().encode("utf-8"),
	  "date": request.form['date'].lower().encode("utf-8"),
	  "state": request.form['state'].lower().encode("utf-8"),
	  "owner": {
	    "$class": "org.acme.howto.Entity",
	    "entityId": "factory",
	    "entityType": "factory",
	    "firstName": request.form['firstname'].encode("utf-8"),
	    "lastName": request.form['lastname'].encode("utf-8")
	  }
	}
	#json_new_val = str(json_val).replace("'", '"')
	#r = requests.post('http://localhost:3000/api/Pizza/random', data=json.loads(json_new_val))
	payload = {
		  "$class": "org.acme.howto.Entity",
		  "entityId": "factory",
		  "entityType": "factory",
		  "firstName": "Cool",
		  "lastName": "Man"
		}
	r = requests.post('http://localhost:3000/api/Entity', data=payload)
	return("The status code of the POST is: "+ str(r.status_code) + " , " + str(r.text))

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
