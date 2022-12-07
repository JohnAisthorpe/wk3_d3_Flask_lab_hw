from flask import render_template
from app import app
from models.book_list import books

@app.route('/books')
def index():
    return render_template('index.html', title="My orders!", books= books)

@app.route('/orders/<index>')
def show(index):
    return render_template('order.html', title="My orders!", book= books[int(index)])

