from flask import Flask, render_template
import random 

app = Flask(__name__)

@app.route('/')
def Site():
	return render_template("fares.html")




if __name__ == "__main__":
	app.run()



