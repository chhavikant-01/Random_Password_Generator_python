from flask import Flask 
from flask import render_template
from flask import jsonify

app=Flask(__name__)
TOOLS = [
{
  'Name': 'Strong Password Generator'
}
]

@app.route("/")
def hello_Logic():
  return render_template('index.html', tools= TOOLS)

@app.route("/api/tools")  
def list_tools():
  return jsonify(TOOLS)
  
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)

