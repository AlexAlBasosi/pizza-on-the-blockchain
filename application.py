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

@app.route("/submitPizza", methods=['POST', 'GET'])
def submitPizza():
	json_val = {
	  "$class": "org.acme.howto.Pizza",
	  "pizzaId": "pizza",
	  "timestamp": request.form['firstname'],
	  "date": request.form['date'],
	  "state": request.form['state'],
	  "owner": {
	    "$class": "org.acme.howto.Entity",
	    "entityId": "factory",
	    "entityType": "factory",
	    "firstName": request.form['firstname'],
	    "lastName": request.form['lastname']
	  }
	}
	requests.post('http://localhost:3000/api/Pizza/pizza', data = json_val)
	return(str(json_val))

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