from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/history')
def history():
    return render_template('pages/history.html')

if __name__ == '__main__':
    app.run(debug=True)
