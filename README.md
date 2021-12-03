# Overview

Objectives:
- populate a DB with Pokemon.
- provide a front end to view these delightful creatures.

Design criteria:
- demonstrate some generic stuff
- get all the data without thinking about it too much
	- derive all referential information
	- currenly some grouping data is not properly extracted.  Information, not data.
- Provide a way to generically create queries
	- the data is in a format to do this
	- implemnetation timed out
	- sample 'intermediate' query provided
	- some comments in results.py
- a simple pair of templates to
	- run the crawl process
	- note this get 100 Pokemon by default - edit crawl.py to get more
		- future enhancement!
	- simple listing of ALL Pokemon, it would be nice to add filtering and sorting
	- and to add dynamic query generation.  Designed but not implemented.

## Install

Create a virtualenv and then from 'home':

```
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
set FLASK_APP=pokemon.py
```

## Launch

```
$ flask run
```

Then enter into your browser http://127.0.0.1:5000

## Test

None atm.  Another time out.

## Clean down DB

Comes fully populated, but if you wish to re-start:

Drop migrations folder and db file.
Then
```
flask db init
flask db migrate
flask db upgrade
```

And choose to the re-populate button on the home page.

Edit MAXIMUM_EXTRACT in crawl.py to change how many little critters come back.
The deployed DB was populated with this set effectively to infinity - somewhere a bit over a thousand. 