from flask import Flask,render_template,request
app = Flask(__name__ , template_folder='templates')
@app.route('/')
def main():
  return render_template('main.html')
    
@app.route('/submit',methods=['POST'] )
def show():
  name=request.form['name']
  age=request.form['age']
  email=request.form['email']
  password=request.form['password']
  return render_template('display.html',name=name , age =age , email = email , password= password)
if __name__ == '__main__':
    app.run(debug=True)
  