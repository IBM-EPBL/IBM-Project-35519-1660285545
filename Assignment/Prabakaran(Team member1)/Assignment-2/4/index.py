from flask import Flask, render_template, request, redirect, url_for, abort
import ibm_db
app = Flask(__name__)
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=31249;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=txz44264;PWD=0e7ZwhLpS1dJFh9f","","")
data = ibm_db.exec_immediate(conn, "SELECT \"USER\", \"PASSWORD\" FROM \"TXZ44264\".\"User Details\";")
user_lst = []
pass_lst = []
while ibm_db.fetch_row(data) != False:
    user_lst.append(ibm_db.result(data, 0).replace(" ", ""))
    pass_lst.append(ibm_db.result(data, 1).replace(" ", ""))
print(user_lst, pass_lst)
@app.route("/")
def welcome():
    return render_template("/index.html")
@app.route("/index", methods=["POST","GET"])
def index():
    if (request.method == "POST"):
        user = request.form.get("user")
        passw = request.form.get("pass")
        if (user in user_lst and passw in pass_lst):
            return render_template("/welcome.html", user=user)
        else:
            return redirect(url_for("error"))   
@app.route("/error")
def error():
    return render_template("/error.html")
if __name__ == "__main__":
    app.run(debug = True)