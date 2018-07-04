from flask import Flask

app=Flask(__name__) 

@app.route('/helloworld:9000')

def home():
    return "Hello World"

if __name__ =="__main__":
    app.run(debug=True)
