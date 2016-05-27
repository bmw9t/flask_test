from flask import Flask, url_for, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/usr/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
                error = 'Invalid username/password'
        return render_template('login.html', error=error)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')


@app.route('/about')
def about():
    return 'The about page'


if __name__ == "__main__":
    with app.test_request_context('/hello', method='POST'):
        assert request.path == '/hello'
        assert request.method == 'POST'

    app.run(debug=True)
