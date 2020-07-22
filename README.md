# FlaskSocketIO

This is a test Flask project to explore how to have dynamic Web pages.
By Dynamic, I mean ones that automatically update when some underlying data has changed. Not by just querying some data source and then displaying the data.

Just in case you need a static page there is one included also...

## Extras

There is a decent(ish) Makefile, plus this uses the very nice **bumpversion** semantic packaging.

## Routes

There are two active "routes" in this project

	/index - or the default hosting location (127.0.0.1:5000) 
	/hello

### Index

This generatesa rather dull Web page, which has a piece of JS embedded in it.
This JS listens for data being sent to the endpoint /test, and then extracts from *newnumber* event, and then displays the number value of the object to the screen.

### Hello

This is an even more stupid piece of HTML, which just says "Hi", but it here so that there are both Static and Dynamic routes.

# Project Layout

This is a better layed out project than most - I have split the functionality into clear areas (well I hope it is clear). Flask is nice to work with until you try and clean things up, and then it seems to get overly unpleasant. You have been warned.


```text
/setup.py
  /__main__.py
  /__init__.py
  /README.md
    /templates/index.html
    /templates/Hello.html
    /model/rnd_num.py
    /model/hello.py
    /model/__init__.py
    /controllers/socketioapp.py
    /controllers/app.py
    /controllers/__init__.py
      /static/js/application.js

```

## Installing

Please check out **setup.py** which maintains a list of requirements.

## Running

Assuming everything is installed, it should be.

    python __main__.py 

# Omissions

There are no tests written for this. 
Logging has not been implemented, rather I used cheap quick print statements (I hang my head in shame).

