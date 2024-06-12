from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

# HTML template for the web form with selected option retained
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
        <input type="text" id="name" name="name" value="{{ name }}"><br><br>
        <label for="figure">Choose a figure:</label>
        <select id="figure" name="figure">
            <option value="pig" {% if figure == 'pig' %}selected{% endif %}>Pig</option>
            <option value="tux" {% if figure == 'tux' %}selected{% endif %}>Tux</option>
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
    name = ''
    figure = 'pig'

    if request.method == "POST":
        name = request.form["name"]
        figure = request.form["figure"]

        # Construct the cowsay command
        cmd = f"cowsay -f \"{figure}\" Hello, {name}"

        # Run the command and capture the output
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        # Store the command output
        message = result.stdout

    # Render the form with the message
    return render_template_string(form_template, message=message, name=name, figure=figure)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

