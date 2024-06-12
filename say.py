from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

# HTML template for the web form
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Cowsay Web Form</title>
</head>
<body>
    <h1>Cowsay Web Form</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="figure">Choose a figure:</label>
        <select id="figure" name="figure">
            <option value="cow">Cow</option>
            <option value="pig">Pig</option>
            <option value="tux">Tux</option>
            <!-- Add more figures as needed -->
        </select><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if message %}
    <pre>{{ message }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        name = request.form["name"]
        figure = request.form["figure"]
        cmd = f"cowsay -f {figure} Hello, {name}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        message = result.stdout
    return render_template_string(form_template, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

