from flask import Flask
# requirement: flask($ pip install flask)

# define app using Flask
app = Flask(__name__)

# route(ex> https://www.naver.com"/news" )
@app.route('/')
def index():
    return "hello"

# route for api server
@app.route('/api/v1/naver')
def get_keyword():
    return "keyword will shows here"

# flask run with shell
if __name__ == '__main__':
    app.run('0.0.0.0', port=8088)
