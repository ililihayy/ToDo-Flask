from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"task": "First Task", "done": False}, {"task": "Second Task", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo_add']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))

@app.route("/delete/<int:index>", methods=['POST'])
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

@app.route("/check/<int:index>", methods=['POST'])
def check(index):
    todos[index]["done"] = not todos[index]["done"]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
    