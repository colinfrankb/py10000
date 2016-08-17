from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def index():
    # response = make_response('Hello World!\n\r')
    # response.headers['Cache-Control'] = 'public'
    # response.headers['Last-Modified'] = 'Sun, 31 Jul 2016 19:50:16 GMT'
    # response.headers['Expires'] = 'Mon, 1 Aug 2016 19:50:16 GMT'
    return 'test'

if __name__ == "__main__":
    app.run()
