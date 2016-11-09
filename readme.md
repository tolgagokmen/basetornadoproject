# Base Project
Basic RESTful web Application


### Project details

Each Project should contain the respective details:
* Title
* Release Date
* Production Company


## Built using :

	Tornado : Python web framework and asynchronous networking library
	MongoDB : Database Server
	Motor   : Database Connector ( For creating async connectiong between MongoDB and Tornado )


## Set up environment :

	Install Python ( If you don't have already )
		`sudo apt-get install python` or 'brew install pyhton'
    install mongodb http://docs.mongodb.org/manual/installation/

    Install virtualenv and run
        1) 'pip install virtualenv'
        2) 'virtualenv venv'
        3) '. venv/bin/activate'

## Direct Install from requirements.txt :
           'pip install -r requirements.txt'

## Step by step install :
	1) Install Tornado ( Web Framework )
		`pip install tornado`

	2) Install MongoDB
		`sudo brew install -y mongodb`

	3) Install Pymongo for database connector
		`pip install pymongo'

    4) Create or update requirements.txt
        'pip freeze --local > requirements.txt'

## Run :
	Run MongoDB
		1) Start MongoDB
			`sudo service mongod start`
		2) Stop MongoDB
			`sudo service mongod stop`

	Run the Project file(baseproject.py)
		`python baseproject.py`

	Browse with any Browser to the following link and DONE !
		`http://localhost:8000/recommended'

Tip: make sure to include a requirements.txt