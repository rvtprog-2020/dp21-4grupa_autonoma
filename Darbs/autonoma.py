from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/js')
def js():
    return render_template('javaScript.html')



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

@app.route('/')
def sakums():
    return render_template('sakums.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/administrators')
def admin():
    return render_template('admin.html')    

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results')
def search_result():
    return render_template('search_result.html')

@app.route('/klients')
def klients():
    return render_template('klients.html')

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/beigas')
def beigas():
    return render_template('beigas.html')

if __name__ == "__main__":
    app.run(debug=True)

app.run(host='0.0.0.0', port=80, debug=True)