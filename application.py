from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)

import json 
import random

def myFunc(pizzaId):
	r = requests.get('http://localhost:3000/api/Pizza') # create a new Pizza (random number)
	json_val = r.json()[0]['state']
	return(str(json_val).title())

def myChangeFunc(timestamp):
	return ("Hey",timestamp)

app.jinja_env.globals.update(myFunc=myFunc) 
app.jinja_env.globals.update(myChangeFunc=myChangeFunc) 


@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/factory")
def factory():
	r = requests.get('http://localhost:3000/api/ChangeOwner') 
	return render_template('factory.html', title="Factory", transactions=r.json())

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
	# return("The status code of the POST/PUT is: "+ str(rT.status_code) + " , " + str(rT.text))
	return redirect("/factory")

@app.route("/changeOwner/<owner>", methods=['POST','GET'])
def changeOwner(owner):
	# Create the new owner - wholesaler
	wholesaler_data = {
	  "$class": "org.acme.howto.Entity",
	  "entityId": str(owner)
	}
	r1 = requests.post('http://localhost:3000/api/Entity', data=wholesaler_data)
	# Change Ownership
	owner_data = {
		  "$class": "org.acme.howto.ChangeOwner",
		  "pizza": "p1zzA",
		  "newOwner": str(owner)
		}
	rT = requests.post('http://localhost:3000/api/ChangeOwner', data=owner_data)
	return redirect("/"+str(owner))

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
