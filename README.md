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
* Head over to the Composer Playground: [Composer Playground](http://composer-playground.mybluemix.net/)
<img src="/images/playground.png"></img>

* Select "Deploy a Business Network"

* Under the "Model Network Starter Template", select "browse", and choose the pizza-on-the-blockchain@0.0.1.bna file from this repository.

<img src="/images/result.png"></img>
* Select "Deploy"

<img src="/images/connect.png"></img>
* Select "Connect Now"

You should be presented with the following screen:
<img src="/images/screen.png"></img>

* Click on the "Model File" in the left pane. From this section you can model your business network. In our example, we are tracking the shipment of Frozen Pizzas from the Factory, to the Wholesaler, to the Retailer, down to the Customer. We're assuming each Entity (i.e. Factory), will make use of RFID tags to store information on the pizza, and will scan that tag as it's received. This information, such as timestamp, the date, and state (production, freezing, packaging, distribution) is stored on the Blockchain.

<img src="/images/pizza.png"></img>

We will create multiple instances of type Entity (i.e. Factory).

<img src="/images/participant.png"></img>

Here we define the transactions that will take place on the Blockchain, such as changing the state of the pizza and which entity owns the pizza.
<img src="/images/transactions.png"></img>

* Select "Script File" in the left pane. From here, you will define the transaction processor functions, these are the functions that will execute when the transactions are invoked.

The ChangeStateToProduction function will change the state of the current pizza to Production.
<img src="/images/state.png"></img>

The same applies with the other three states. <br/>
The ChangeOwner function will change the owner of the pizza to a new owner.
<img src="/images/owner.png"></img>

* Select "Access Control" from the left pane. From here, you can determine which participants of the business network have access to which assets and transactions.
<img src="/images/access.png"></img>

* On the Top Pane, select "Test". 
<img src="/images/test.png"></img>

* From here, you can test out the transactions that you defined in the model file. On the top left, select "+ Create New Participant, and enter a unique identifier for the entity.
<img src="/images/entity.png"></img>

* Select "Create New". You should see a new entity being created. In the left Pane, under Assets, select Pizza. Select "+ Create New Asset." Fill in the details for the Pizza, and select "Create New". (For the state, select from "production", "freezing", "packaging", and "distribution). For the Owner field, select the ID of the entity you just created.
<br/><img src="/images/pizzaasset.png"></img>

You should see a new Pizza asset being created.

* Select "Submit Transaction" on the bottom left. For the Transaction Type, select the "ChangeStateToFreezing" transaction, and for the "pizza" field, pass in the ID you just created when creating your pizza asset.
<img src="/images/submittransaction.png"></img>

* Select "Submit"

You should see a notification pop up saying "Submit Transaction Successful". You can double-check by selecting "All Transactions" in the left pane, under Transactions. 
<img src="/images/alltransactions.png"></img>

* In the ChangeStateToFreezing transactions, select "view record", and you can see all the transaction related information.

That's it! You're ready to deploy your business network to the Hypelerledger Fabric.

## Setting up the Environment

### For Windows/Linux Users
The Hyperledger Fabric environment can only be set up on Unix environments, so for windows users, you have to install a virtual machine and set up the environment as such. For the purposes of this demo, we're going to be setting up a Ubuntu OS on VirtualBox.

Download Ubuntu: [Install Ubuntu](https://www.ubuntu.com/download/desktop) <br/>
Download VirtualBox [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)<br/>
Instructions for setting up Ubuntu on VirtualBox [Set Up Ubuntu on VirtualBox](https://askubuntu.com/questions/142549/how-to-install-ubuntu-on-virtualbox) <br/>

#### Installing Pre-Requisites
To run Hyperledger Composer and Hyperledger Fabric, we recommend you have at least 4Gb of memory.

The following are prerequisites for installing the required development tools:

    Operating Systems: Ubuntu Linux 14.04 / 16.04 LTS (both 64-bit), or Mac OS 10.12
     Docker Engine: Version 17.03 or higher
     Docker-Compose: Version 1.8 or higher
     Node: 8.9 or higher (note version 9 is not supported)
     npm: v5.x
     git: 2.9.x or higher
     Python: 2.7.x
     A code editor of your choice, we recommend VSCode.

If installing Hyperledger Composer using Linux, be aware of the following advice:

    Login as a normal user, rather than root.
    Do not su to root.
    When installing prerequisites, use curl, then unzip using sudo.
    Run prereqs-ubuntu.sh as a normal user. It may prompt for root password as some of it's actions are required to be run as root.
    Do not use npm with sudo or su to root to use it.
    Avoid installing node globally as root.**

If you're running on Ubuntu, you can download the prerequisites using the following commands:

``` curl -O https://hyperledger.github.io/composer/prereqs-ubuntu.sh ```
``` chmod u+x prereqs-ubuntu.sh ```

Next run the script - as this briefly uses sudo during its execution, you will be prompted for your password.

``` ./prereqs-ubuntu.sh ```

## For Mac Users

Follow these instructions to install the pre-requsities for installing Hyperledger Composer on a local Mac OS X machine. You need to install these tools before you attempt to install Hyperledger Composer.

### Install nvm and Apple Xcode

First install nvm (the Node version manager). nvm is a tool that allows you to easily install, update and switch between versions of Node.js.

Open the terminal (command line) by clicking on the magnifier in the menu bar at the top right of your screen. Type terminal and press enter.

In the terminal window paste the text below and press enter:

``` curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash ```

When you hit enter you should see the pop-up below, prompting you to install git. Press the Get Xcode button to install the full Apple Xcode IDE, including a C++ compiler, used to install native Node.js modules.

The download and install process for Xcode may take 20 minutes or more. Be patient!

After the installation of Xcode has completed launch Xcode. Accept the license agreement. It will prompt you for your username and password and will install additional components.

After Xcode finishes installing additional components and launches, simply quit Xcode.

Switch back to the terminal and create your bash profile (stores user preferences for bash):

``` touch .bash_profile ```

Then rerun the original curl command:

``` curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash ```

Close the terminal and reopen it.

Check that nvm is installed and is accessible:

``` nvm —-version ```

### Install Node

Install the latest (long term support) version of Node:

``` nvm install --lts ```

Switch to the LTS version of Node:

``` nvm use --lts ```

Check that Node is installed:

``` node --version ```

## Intall Docker

Follow the instructions here to install Docker for Max (stable): [Install Docker](https://docs.docker.com/docker-for-mac/install/)

After running the installed Docker application you should have the whale icon in your menu bar, with a green “Docker is running” status.

### Install VSCode

Install VSCode by visiting: [Install VSCode](https://code.visualstudio.com/)

Press the “Download for Mac” button and copy the downloaded application into your Applications folder.

### Install the Hyperledger Composer Extension for VSCode
Type ```composer``` into the search bar and then press the ```Install``` button next to the Hyperleger Composer extension. Once the install completes you need to press the ```Reload``` button to activate the extension.


## Installing the Development Environment

Follow these instructions to obtain the Hyperledger Composer development tools (primarily used to create Business Networks) and stand up a Hyperledger Fabric (primarily used to run/deploy your Business Networks locally). Note that the Business Networks you create can also be deployed to Hyperledger Fabric runtimes in other environments e.g. on a cloud platform.

### Installing Components

#### Step 1: Install the CLI Tools

There are a few useful CLI tools for Composer developers. The most important one is ```composer-cli```, which contains all the essential operations, so we'll install that first. Next, we'll also pick up ```generator-hyperledger-composer```, ```composer-rest-server``` and ```Yeoman``` plus the ```generator-hyperledger-composer```. Those last 3 are not core parts of the development environment, but they'll be useful if you're following the tutorials or developing applications that interact with your Business Network, so we'll get them installed now.

1. Essential CLI tools:

```npm install -g composer-cli```

2. Utility for running a REST Server on your machine to expose your business networks as RESTful APIs:

```npm install -g composer-rest-server```

3. Useful utility for generating application assets:

```npm install -g generator-hyperledger-composer```

4. Yeoman is a tool for generating applications, which utilises generator-hyperledger-composer:

```npm install -g yo```

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
