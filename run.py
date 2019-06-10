import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  data = []
  with open("data/company.json", "r")  as json_data:
    data = json.load(json_data)
  return render_template("about.html", page_title="About", company=data) 
  # The "list_of_numbers=[1, 2, 3]"" was used initially after page_title="About" to see a for loop working. Just a test that it works, no other meaning
  #list_of_numbers=[1, 2, 3])

@app.route("/about/<member_name>")
def about_member(member_name):
  member = {}

  with open("data/company.json", "r") as json_data:
    data = json.load(json_data)
    for obj in data:
      if obj["url"] == member_name:
        member = obj

  return render_template("member.html", member=member)


@app.route("/contact")
def contact():
  return render_template("contact.html", page_title="Contact")

@app.route("/careers")
def careers():
  return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":

  # in cloud 9 i would add the following for the flask app to work:
  # app.run(host=os.environ.get("IP"),port-int(os.environ.get("PORT")),debug=True)
  app.run(debug=True)