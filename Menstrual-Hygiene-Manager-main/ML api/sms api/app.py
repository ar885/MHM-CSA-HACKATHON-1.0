import requests


import flask
from flask import Flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
  url = "https://api.twilio.com/2010-04-01/Accounts/AC05df9f050ac6ff3b2f9140c6c8d4a47e/Messages.json"
  payload='From=%2B12054984775&To=%2B918435479544&Body=Hello%2C%20your%20favourite%20person%20needs%20you.%20Dear%20Friend%2C%20We%20would%20like%20to%20let%20you%20know%20your%20dear%20one%20is%20suffering%20from%20horrible%20period%20cramps.%20Pro%20tip%3A%20Don\'t%20go%20near%20her%20or%20else%20you%20will%20awake%20a%20deadly%20monster%20and%20regret%20the%20decision%20for%20your%20entire%20life.%20%20But%20she%20needs%20you%20right%20now.%20No%20worries%2C%20Team%20Glovia%20is%20here%20with%20suggestions%20specially%20for%20you%20to%20make%20her%20feel%20better%2C%20amazing%20and%20beautiful%20like%20she%20is.%20%20Here%20are%20some%20things%20you%20can%20do%20for%20her%20right%20now%3A%20%201.%20Get%20some%20chocolates%20for%20her.%20Trust%20us%2C%20that%20works.%20%202.%20Hot%20water%20bags.%20They%20are%20literally%20God\'s%20own%20creation.%20%203.%20Her%20favorite%20games.%20She%20is%20overloading%20with%20emotions%2C%20let%20her%20win%20this%20time%20soldier%20Oh%2C%20and%2C%20most%20importantly%2C%20tell%20her%20how%20much%20you%20love%20her.%20%20You%20are%20amazing.%20Cheers!%20Team%20Glovia'
  headers = {
  'Authorization': 'Basic QUMwNWRmOWYwNTBhYzZmZjNiMmY5MTQwYzZjOGQ0YTQ3ZTpkZTVmNmIyZDQ2ZGUxOTJmZGRiZmI1NDZkNTI1ZTBhNQ==',
  'Content-Type': 'application/x-www-form-urlencoded'}
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text.encode('utf8'))

  return '''<h1>SMS API</h1></p>'''


if __name__ == "__main__":
    app.run(debug = True, use_reloader=False)