from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Employee form page

if __name__ == '__main__':
    app.run(debug=True)
