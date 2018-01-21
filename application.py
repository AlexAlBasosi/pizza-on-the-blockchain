from flask import Flask, render_template
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