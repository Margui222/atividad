

from flask import Flask,render_template, request,url_for, redirect
from flaskext.mysql import MySQL
app = Flask(__name__, static_url_path="/static")
mysql = MySQL(app)
app.config["MYSQL_DATABASE_HOST"] = "127.0.0.1"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "Nuevo"
app.config["MYSQL_DATABASE_PORT"] = 3306
mysql.init_app(app)
@app.route("/")

def index():

  return render_template("index.html")

@app.route("/rejilla")
def rejilla_html():
     return render_template('html_rejilla.html')

@app.route("/senderismo")
def senderismo_html():
     return render_template('senderismo.html')

@app.route("/index")
def index_html():

    return render_template("/index.html")

@app.route("/fisica")
def fisica_html():
        return render_template("/fisica.html")
@app.route("/Material")
def Material_html():
        return render_template("/Material.html")
@app.route("/Formacion")
def Formacion_html():
        return render_template("/Formacion.html")



if __name__ == '__main__':
 app.run(port=8000,debug=True)