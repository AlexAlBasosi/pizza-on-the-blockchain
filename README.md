# Pizza! on the Blockchain 

## Develop an end-to-end Blockchain application

## What is Hyperledger Fabric?
Hyperledger Fabric is a platform for distributed ledger solutions, underpinned by a modular architecture delivering high degrees of confidentiality, resiliency, flexibility and scalability. It is designed to support pluggable implementations of different components, and accommodate the complexity and intricacies that exist across the economic ecosystem.

<br/>
<img src="/images/hyperledger.png"></img>
<br/>

## What is Hyperledger Composer
Hyperledger Composer is a set of collaboration tools for building blockchain business networks that make it simple and fast for business owners and developers to create smart contracts and blockchain applications to solve business problems.

### The Business Network
Head over to the Composer Playground: [Composer Playground](http://composer-playground.mybluemix.net/)
<img src="/images/playground.png"></img>

Select "Deploy a Business Network"

Under the "Model Network Starter Template", select "browse", and choose the pizza-on-the-blockchain@0.0.1.bna file from this repository.

<img src="/images/result.png"></img>

## For Windows Users

## For Mac Users


### Purpose
This is a Python Flask web application built as an interface for the Blockchain network running on Hyperledger Fabric. The application utilises REST APIs (generated using the [Composer REST Server](https://hyperledger.github.io/composer/reference/rest-server.html)) to connect to the Blockchain network and perform GET, POST and PUT requests. 

### Technology 
This application was built with the [Flask Microframework](http://flask.pocoo.org/). The UI of the application was built with [MaterializeCSS](http://materializecss.com/), a front-end framework based on Material Design. 

### How to run
1. Ensure Python is installed on your local environment (Both Python 2 and Python 3 are supported).
2. Install the requirements using the command `pip install -r requirements.txt`.
3. Run the application as: `python application.py`. 
4. Point your web browser to the address `localhost:<port>`. 

### Help
Please feel free to [contact me](mailto:Arjun.Nedungadi1@ibm.com) with any questions/comments. 
