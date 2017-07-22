from flask import Flask , render_template , request
import random
import dataset
db = dataset.connect("postgres://xcxxntyuoeqjlg:19cf8cf68bccacb6b5d8b6c7a0d0ba268bca3ec870485ca47b995704f360bbe3@ec2-23-21-96-159.compute-1.amazonaws.com:5432/d5h12c5nd4jmvn")
app= Flask(__name__)

@app.route('/')
def contact():
		return render_template("index.html")
@app.route("/ShowContact" , methods=["POST"])
def showcontact():
	form = request.form
	Name = form["Name"]
	Subject=form["Subject"]
	Message = form["Message"]
	Email = form["Email"]
	Phone = form["Phone"]
	contactsTable = db["contacts"]
	entry = {"Name":Name , "Subject":Subject , "Message":Message , "Email":Email , "Phone":Phone}
	contactsTable.insert(entry)
	print list(contactsTable.all())
	return render_template("contactshow.html" , Name=Name  , Subject=Subject , Email=Email , Phone=Phone , Message=Message)
@app.route("/05980172022001")
def showAll():
	contacts= db["contacts"]
	allContacts= list(contacts.all())
	return render_template("showall.html" , contacts=allContacts)

if __name__== '__main__':
	app.run()
