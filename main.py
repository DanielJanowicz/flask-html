from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/opsys')
def login():
    return render_template('opsys.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


