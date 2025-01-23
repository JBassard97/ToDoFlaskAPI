from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app and set up the database URI
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:password123@localhost:5432/firstdatabase"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)


# Define the Todo model (representing a table in PostgreSQL)
class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    duedate = db.Column(db.String(30))
    todo = db.Column(db.String(100))

    def __init__(self, duedate, todo):
        self.duedate = duedate
        self.todo = todo

    def to_dict(self):
        return {"id": self.id, "duedate": self.duedate, "todo": self.todo}


# Route to get all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])


# Route to create a new todo
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    new_todo = Todo(duedate=data["dueDate"], todo=data["todo"])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201


if __name__ == "__main__":
    app.run(debug=True)
