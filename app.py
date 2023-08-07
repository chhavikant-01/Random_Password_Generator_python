from flask import Flask, request
from flask import render_template
from flask import jsonify
import random, string

app=Flask(__name__)

TOOLS = [
{
  'Name': 'Strong Password Generator'
}
]

@app.route("/")
def hello_Logic():
  return render_template('index.html', tools= TOOLS)

# Function to generate a strong password
def generate_password(length=12):
    password = ''
    characters = string.printable
    for i in range(length):
      c = ''
      c = random.choice(characters)
      password = password + c
      return password
      

@app.route('/', methods=['GET', 'POST'])
def passwordgen():
    if request.method == 'POST':
        print("Received POST request:")
        password_length = int(request.form.get('password_length', 12))
        password = generate_password(password_length)
        return render_template('index.html', PASSWORD=password)
    else:
      print("NOT Received POST request:")
      return render_template('index.html', PASSWORD='',tools = TOOLS)
    

@app.route("/api/tools")  
def list_tools():
  return jsonify(TOOLS)
  
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)

