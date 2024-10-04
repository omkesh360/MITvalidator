from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate_email():
    name = request.form['name']
    email = request.form['email']

    if validate_email_address(email):
        result = f"Hello, {name}! Your email is valid."
        color = "green"
    else:
        result = f"Sorry, {name}. Your email is not valid."
        color = "red"

    return render_template('index.html', result=result, color=color)

def validate_email_address(email):
    import re
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None

if __name__ == '__main__':
    app.run(debug=True)