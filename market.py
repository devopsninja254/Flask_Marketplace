from flask import Flask, render_template,jsonify


app = Flask(__name__)  # this is the local python file I'm working with

'''
remember to create a templates dir in root folder of project 
'''


@app.route('/')
@app.route('/home')
@app.route('/nyumbani')      # how to add multiple routes with flask python
def homepage():
    return render_template("home.html")


@app.route('/purpose')
def purpose():
    return '<h1> I am going to build a nice UI for prod support</h1>'


@app.route('/health')
def health():
    return jsonify(status="Virtuoso is up and running!")


@app.route('/market')
def market_page():
    # a list of dictionaries
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)    # how to fetch data and display on html using Jinja


@app.route('/about/<username>')  # allow this string to receive a username variable. Dynamic routes in flask python
def about(username):
    return f'<h1> Welcome to the marketplace, {username}</h1'


# handle flask exceptions gracefully please!
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == "__main__":
    app.run()
