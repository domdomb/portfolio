from flask import Flask,render_template
from livereload import Server, shell
app = Flask(__name__,template_folder='.')

@app.route("/")
def hello():
    return render_template('index.html')
app.debug = True
server = Server(app.wsgi_app)
# server.watch
server.serve()
