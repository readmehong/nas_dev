from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   # return render_template('index.html')
    return 'hello'
    
@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
