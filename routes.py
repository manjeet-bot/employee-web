from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Dummy login check
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Dummy database (for simplicity, use a dictionary or file for storing data)
employees = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    number = request.form['number']
    address = request.form['address']
    department = request.form['department']
    feedback = request.form['feedback']
    photo = request.files['photo']
    
    photo_path = os.path.join('static/photos', photo.filename)
    photo.save(photo_path)

    # Save employee details (in real cases, save in database)
    employees.append({
        'name': name,
        'number': number,
        'address': address,
        'department': department,
        'photo': photo_path,
        'feedback': feedback
    })

    return redirect(url_for('home'))

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for('admin_dashboard'))
        else:
            return "Invalid credentials!", 403
    
    return render_template('admin_login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', employees=employees)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('search_query')
    filtered_employees = [e for e in employees if query.lower() in e['name'].lower() or query.lower() in e['department'].lower()]
    return render_template('admin_dashboard.html', employees=filtered_employees)

if __name__ == '__main__':
    app.run(debug=True)
