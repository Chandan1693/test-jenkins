from flask import Flask, request, render_template_string, send_file
from gtts import gTTS
import os

app = Flask(__name__)

# HTML template for the web form
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Text to Speech</title>
</head>
<body>
    <h1>Text to Speech Web Form</h1>
    <form method="POST">
        <label for="text">Text to speak:</label>
        <input type="text" id="text" name="text" required><br><br>
        <input type="submit" value="Submit">
    </form>
    {% if audio %}
    <audio controls>
        <source src="{{ url_for('download_file', filename=audio) }}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    audio_file = None
    if request.method == "POST":
        text = request.form["text"]

        # Convert text to speech
        tts = gTTS(text, lang='en')
        audio_file = "output.mp3"
        tts.save(audio_file)

    return render_template_string(form_template, audio=audio_file)

@app.route("/audio/<filename>")
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005)

