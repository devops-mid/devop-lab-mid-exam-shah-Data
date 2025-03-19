import re
from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'].strip()
    email = request.form['email'].strip()
    phone = request.form.get('phone', '').strip()
    address = request.form.get('address', '').strip()

    # Validate email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        flash("Invalid email format!", "danger")
        return redirect(url_for('index'))

    # Validate phone number (must be 10 digits)
    if phone and not re.match(r'^\d{10}$', phone):
        flash("Invalid phone number! Please enter exactly 10 digits.", "danger")
        return redirect(url_for('index'))

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        flash("Email already registered!", "warning")
        return redirect(url_for('index'))

    # Check if phone number already exists
    if User.query.filter_by(phone=phone).first():
        flash("Phone number already registered!", "warning")
        return redirect(url_for('index'))

    # Insert into DB
    user = User(name=name, email=email, phone=phone, address=address)
    db.session.add(user)
    db.session.commit()

    flash("User registered successfully!", "success")
    return redirect(url_for('index'))
