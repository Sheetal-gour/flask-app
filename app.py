from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models import db,Employee

app = Flask(__name__)
print(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:sheetal@localhost:5432/emp1"

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()
    

@app.route('/')
@app.route('/employee')
def hello():
    return "Hello World!"

@app.route('/employee/add',methods=['POST'])
def new_emp():
    data = request.get_json()
    
    age = data['age']
    name = data['name']
    
    employee = Employee(name,age)
    db.session.add(employee)
    db.session.commit()
    
    return jsonify({
        "success":True,
        "message":"Employee Added successfully"
        })



if __name__ == '__main__':
    app.run(debug=True)
