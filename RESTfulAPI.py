from flask import Flask, render_template, request

app = Flask(__name__)

# Define the routes for the web application
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send the email to the appropriate recipient using a third-party email service
        return render_template('contact_success.html', name=name)
    else:
        return render_template('contact.html')

# Run the web application
if __name__ == '__main__':
    app.run(debug=True)
