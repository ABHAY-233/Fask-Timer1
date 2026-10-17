from flask import Flask, render_template
import os

# This forces Flask to search relative to your current file location
app = Flask(__name__, template_folder=os.path.abspath('templates'))

@app.route('/')
def index():
    starting_seconds = 120
    return render_template('index.html', seconds=starting_seconds)

@app.route('/healthz', methods=['GET'])
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
