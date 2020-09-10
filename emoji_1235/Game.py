from flask import Flask


app=Flask (__name__,static_url_path="/static")
@app.route("/")
def Game():
    return open('index.html','r').read()

if __name__== '__main__':
    #app.send_static_file("index.html")
    app.run(debug=True, port=1235)
