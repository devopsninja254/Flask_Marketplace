from flask import Flask

app = Flask(__name__)  # this is the local python file I'm working with


@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/purpose')
def purpose():
    return '<h1> I am going to build a nice UI for prod support</h1>'


@app.route('/about/<username>')    # allow this string to receive a username variable. Dynamic routes in flask python
def about():
    return f'<h1> Welcome to the marketplace, {username}</h1'




if __name__ == "__main__":
    app.run()


