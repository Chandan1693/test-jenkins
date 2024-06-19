from flask import Flask, request, render_template_string
import pyfiglet

app = Flask(__name__)

# HTML template for the web form
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Figlet Web Form</title>
</head>
<body>
    <h1>Figlet Web Form</h1>
    <form method="POST">
        <label for="text">Enter your text:</label>
        <input type="text" id="text" name="text"><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if ascii_text %}
    <pre>{{ ascii_text }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    ascii_text = None

    if request.method == "POST":
        user_input = request.form["text"]
        ascii_text = pyfiglet.figlet_format(user_input)

    return render_template_string(form_template, ascii_text=ascii_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
