from flask import Flask, request, Response
import json

app = Flask(__name__)

todo_db = {
    "1": {"task": "build crud app", "description": "Building a CRUD app for talent academy classs"},
    "2": {"task": "Get some food", "description": "Leave work and get some food!"},
    "3": {"task": "Get some food", "description": "Leave work and get some food!"}
}



@app.route('/')
def read():
    return todo_db

@app.route('/create')
def create():
    create_todo = {"4": {"task": "Go to the grocery store", "description": "Grocery shop for the week"}} 
    todo_db.update(create_todo)
    return todo_db

@app.route('/update')
def update():
    todo_db["4"]["task"] =  "Go to Publix and Walmart"
    return todo_db

@app.route('/delete')
def delete():
    del todo_db["4"]
    return todo_db



if __name__ == "__main__":
    app.run(host="127.0.0.1")