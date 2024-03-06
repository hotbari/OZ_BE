from flask import Flask,request


app = Flask(__name__)

@app.route('/')
def home():
    return "hello"

@app.route('/about')
def about():
    return "about page"

@app.route('/project')
def project():
    return 'The project page'

# 동적으로 파라미터 받아옴
# http://127.0.0.1:5000/user/sungchan
@app.route('/user/<username>')
def user_profile(username):
    return f'Username : {username}'

@app.route('/submit',methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)



if __name__ == "__main__":
    app.run()