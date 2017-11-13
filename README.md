# RestAPIBackend
A simple REST API demo in Python using Flask

This project was done in Python 2.7 on kali linux

You should be able to run without having to download any of the required libraries. once you've downloaded the project navigate to the folder containing app.py in the command line and then call 

`flask/bin/python app.py`

This should start the application. then in a separate command window you can begin calling curl commands on it. 

Please be aware that flask will run by default on port 5000 so the data is located at `localhost:5000/api/notes`

calling:
```curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/notes/```
should get you one initial entry.

once done simply hit `ctrl+c` on the command window you used to initially run app.py and it will kill the server

If it doesn't work out of the box you'll have to grab the flask library files which can be done using the pip command

`pip install flask flask-jsonpify flask-restful` 

which will install it to your default python install directory. if you would like it to be selfcontained to just the project you can install it through virutalenv

navigate in the command line to where app.js is located then enter the following commands:

```
virtualenv flask
source flask/bin/activate
pip install flask flask-jsonpify flask-restful
pip freeze
```

once done you should be able to run the app by calling `flask/bin/python app.py`
