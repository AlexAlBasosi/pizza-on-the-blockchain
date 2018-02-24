from flask import Flask, render_template, request, redirect
import requests
import json 
import random
import os
import dateutil.parser

app = Flask(__name__)

# Helper function to parse the raw string from the Blockchain
def myOwnerFunc(newOwner):
	return newOwner.split("#")[1].title()

# Helper function to get the current state of the Pizza asset
def myFunc(pizzaId):
	r = requests.get('http://localhost:3000/api/Pizza')
	try:
		json_val = r.json()[0]['state']
	except:
		json_val = " "
	return(str(json_val).title())

# Helper function to parse a raw timestamp to a desired format of "H:M:S dd/mm/yyy"
def myChangeFunc(timestamp):
	t = dateutil.parser.parse(timestamp)
	finalT = t.strftime("%H:%M:%S %d/%m/%Y")
	return finalT

# This allows using the above 3 functions in-line from the HTML templates 
app.jinja_env.globals.update(myFunc=myFunc) 
app.jinja_env.globals.update(myChangeFunc=myChangeFunc) 
app.jinja_env.globals.update(myOwnerFunc=myOwnerFunc) 

# Route: index page
@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

# Route: factory page
@app.route("/factory")
def factory():
	print("Hello!")
	r = requests.get('http://localhost:3000/api/ChangeOwner') 
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('factory.html', title="Factory", transactions=transactions)

# Route: submitPizza transaction
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
		# Making 2 POST requests with JSON data as a parameter 
		# POST Request 1: Create a new Pizza element with its respective fields 
		r = requests.post('http://localhost:3000/api/Pizza', data=json_val)
		# POST Request 2: Issue a ChangeStateToProduction transaction
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
		# Making 1 POST request with JSON data as a parameter
		# POST Request: Issue a ChangeStateTo<state>; where <state> is the state selected from the dropdown
		rT = requests.post('http://localhost:3000/api/ChangeStateTo'+state_info.title(), data=transactions_val)
	# return("The status code of the POST/PUT is: "+ str(rT.status_code) + " , " + str(rT.text))
	return redirect("/factory")

# Route: changeOwner transaction (owner's name is passed as a parameter) 
@app.route("/changeOwner/<owner>", methods=['POST','GET'])
def changeOwner(owner):
	owner_data = {
	  "$class": "org.acme.howto.Entity",
	  "entityId": str(owner)
	}
	# POST Request 1: Create a new Entity element with its respective fields
	r1 = requests.post('http://localhost:3000/api/Entity', data=owner_data)
	# Change Ownership
	owner_data = {
		  "$class": "org.acme.howto.ChangeOwner",
		  "pizza": "p1zzA",
		  "newOwner": str(owner)
		}
	# POST Request 2: Issue a ChangeOwner transaction
	rT = requests.post('http://localhost:3000/api/ChangeOwner', data=owner_data)
	return redirect("/"+str(owner))

# Route: wholesaler page
@app.route("/wholesaler")
def wholesaler():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner') 
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('wholesaler.html', title="Wholesaler", transactions=transactions)

# Route: retailer page
@app.route("/retailer")
def retailer():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner')
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()	
	return render_template('retailer.html', title="Retailer", transactions=transactions)

# Route: customer page
@app.route("/customer")
def customer():
	# GET Request 1: Get ChangeOwner transaction data
	r = requests.get('http://localhost:3000/api/ChangeOwner')
	if r.json()==None or r.json()=={}:
		transactions = {}
	else:
		transactions = r.json()
	return render_template('customer.html', title="Customer", transactions=transactions)

# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 5000))

# Entry point to the program
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
