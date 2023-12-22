import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1>'
    # Added greeting line
    page += "</br>Greetings from YourName </br>"
    page += '</body></html>'
    return page

# Two blank lines after the function definition
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
