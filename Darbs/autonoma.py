from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/js')
def js():
    return render_template('javaScript.html')


@app.route('/registration')
def jaunskonts():
    return render_template('registration')


@app.route('/users')
def user():
    return {
    "data":
        [
            {"id":"1", "vards":"Maris","uzvards":"Danne"},
            {"id":"2", "vards":"Valters","uzvards":"Ozols"}
            
        ]
    }

@app.route('/user/<id>')
def editUser(id):
    if id == "1":
        return {"id":"1", "vards":"Maris","uzvards":"Danne","status":"admin"}
    elif id == "2":
        return {"id":"2", "vards":"Valters","uzvards":"Ozols","status":"user"}
    else:
        return {"error":"User not found!"}
 

app.run(host='0.0.0.0', port=80, debug=True)