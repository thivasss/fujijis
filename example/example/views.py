"""
Routes and views for the flask application.
"""
from flask import Flask
from datetime import datetime
from flask import render_template
from example import app
from flask import request

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact Informations below',
        year=datetime.now().year,
        message='You can find us in any of the emails below or by calling any of the phones provided'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Applicatinon',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/dbapp', methods=['POST'])
def dbapp():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text

