from flask import Flask    # From the flask import the flask class

app = Flask(__name__)      # Create an instance of the flask class into app.
                           # app is now an "object"

@app.get("/")               # Flask decorator that allows us to map a route to a view function
def index():                # Our view function.
    return "<h1>Hello, world!</h1>"  # Return statement.





@app.get("/about")
def get_about():
    me = {
        "first_name": "Kim",
        "last_name": "Morgan",
        "hobbies": "Hiking, jogging",
        "active": True
    }
    return me
