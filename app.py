# from app import Flask, render_template
# app = Flask(__name__)

# @app.route('/home')
# def home():
#     return "Hello from /home"

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
   return render_template('home.html')
if __name__ == '__main__':
   app.run(debug=True)
