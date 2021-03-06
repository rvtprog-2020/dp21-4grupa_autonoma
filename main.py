from flask import Flask, flash, render_template, url_for, request, redirect, session
from pymongo import MongoClient
from bson.json_util import dumps
from random import randint

app = Flask(__name__)
app.secret_key = "rTf45as(rw2Ew_"

# login
# TkD0nfEVDOyNk3Bp

# Mongo klienta pievienošana. 

client = MongoClient("mongodb+srv://login:TkD0nfEVDOyNk3Bp@cluster0.qd271.mongodb.net/database?retryWrites=true&w=majority")

# Informācija par divām datubāzēm
db = client.users
users_database = db.users_info

db = client.cars
cars_database = db.cars_info

# Panels, kura lietotājs var izveleties sev transportu.

@app.route('/cars', methods=["GET","POST"])
def cars():
    if 'user' in session:
        user_text = session['user']
    elif 'admin' in session:
        user_text = session['admin']
    else:
        user_text = "user"
    if 'admin' in session or 'user' in session:
        return render_template('cars.html', user_text=user_text)
    else:
        flash("Lūdzu, ieiet")
        return redirect(url_for("index"))

@app.route('/data')
def data():
    cars = cars_database.find()
    data = list(cars)
    return dumps(data)

# Ielogošana saitē. Ir divi lietotāju veidi, kuri var darboties saitē, vai nu parasts users, vai nu admins. Ir arī iespēja reģistreties saitē. 

@app.route('/', methods=["GET","POST"])
def index():
    if 'user' in session:
        user_text = session['user']
    elif 'admin' in session:
        user_text = session['admin']
    else:
        user_text = "user"
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        if "admin" in session or "user" in session:
            flash("Jūs jau esat iegājuši")
            return render_template('index.html', user_text=user_text)
        if login == "admin" and password == "admin":
            session['admin'] = "admin"
            return redirect(url_for("panel"))
        user_database = users_database.find_one({"login":login})
        if user_database == None:
            flash("Parole vai e-pasts nav pareizs!")
            return render_template('index.html', user_text=user_text)
        if login == user_database['login'] and password == user_database['password']:
            session['user'] = login
            flash("Jūs esat iegājuši")
            return render_template('index.html', user_text=login)
        else:
            flash("Parole vai e-pasts nav pareizs!")
            return render_template('index.html', user_text=user_text)
    else:
        return render_template('index.html', user_text=user_text)

# Panelis paredzēts adminam. Šeit viņš var pievienot jaunu automobili vai noņemt.

@app.route('/panel', methods=["GET","POST"])
def panel():
    if 'user' in session:
        user_text = session['user']
    elif 'admin' in session:
        user_text = session['admin']
    else:
        user_text = "user"
    if "admin" in session:
        if request.method == 'POST':
            place = request.form['place']
            marka = request.form['marka']
            model = request.form['model']
            year = request.form['year']
            img = request.form['img']
            if place == "" or marka == "" or model == "" or year == "" or img == "":
                flash("Ievadiet visu informāciju")
                return render_template('panel.html', user_text=user_text)
            else:
                random_int = randint(999,999999)
                data = {"id":random_int,"place":place,"marka":marka,"model":model,"year":year,"img":img,"buy":True}
                cars_database.insert_one(data)
                flash("Gatavs!")
                return render_template('panel.html', user_text=user_text)

        else:
            return render_template('panel.html', user_text=user_text)
    else:
        flash("Jūs neesat admins!")
        return redirect(url_for("index"))

# Šeit admins var apskatīt klientus (pircējus). Tā informacija tiek aizsargāta no parastiem useriem, tie nevar to apskaitīt, jo nav pieejams.

@app.route("/panel/buy/<int:id>", methods=["GET","POST"])
def customer(id):
    if 'user' in session:
        user_text = session['user']
    elif 'admin' in session:
        user_text = session['admin']
    else:
        user_text = "user"
    if 'admin' in session:
        user_who_buy = users_database.find_one({"buy":id})
        if user_who_buy == None:
            name = "None"
            email = "None"
        else:
            name = user_who_buy['name']
            email = user_who_buy['login']
        car_who_buy = cars_database.find_one({"id":id})
        car = car_who_buy['marka']
        return render_template("who-customer.html", user_text=user_text, name=name, email=email, car=car)
    else:
        return redirect(url_for("index"))

# Šeit userim parādās visa informācija par nopirkto transportu. 

@app.route("/cars/buy/<int:id>", methods=["GET","POST"])
def buy(id):
    if 'user' in session:
        user_text = session['user']
    elif 'admin' in session:
        user_text = session['admin']
    else:
        user_text = "user"
    car_database = cars_database.find_one({"id":id})
    if car_database['buy'] == False:
        return redirect(url_for("index"))
    if 'user' in session:
        user = session['user']
        users_database.update_one({"login":user}, {"$set": {"buy":id}})
        car = car_database['marka']
        cars_database.update_one({"id":id}, {"$set": {"buy":False}})
        return render_template('check.html', user_text=user_text, id=id, car=car)
    else:
        return redirect(url_for("index"))

# Šeit admins var nodzēst automobiļi no saraksta. 

@app.route("/panel/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    if 'user' in session:
        user_text = session['user']
    elif 'admin' in session:
        user_text = session['admin']
    else:
        user_text = "user"
    if 'admin' in session:
        cars_database.delete_one({"id":id})
        return redirect(url_for("panel"))
    else:
        return redirect(url_for("index"))

# Reģistracija

@app.route('/register', methods=["GET","POST"])
def register():
    if 'user' in session:
        user_text = session['user']
    elif 'admin' in session:
        user_text = session['admin']
    else:
        user_text = "user"
    if request.method == "POST":
        if 'user' in session or 'admin' in session:
            flash("Jūs jau esat iegājuši")
            return render_template('register.html', user_text=user_text)
        login = request.form['login']
        name = request.form['name']
        password = request.form['password']
        if login == "" or name == "" or password == "":
            flash("Lūdzu, ievadiet visu informāciju")
            return render_template('register.html', user_text=user_text)
        data = {"login":login,"name":name,"password":password,"buy":0}
        users_database.insert_one(data)
        flash("Reģistrācija ir veiksmīga!")
        return redirect(url_for("index"))
    else:
        return render_template('register.html', user_text=user_text)

# Izeja no saites

@app.route('/logout', methods=["GET","POST"])
def logout():
    session.pop("admin", None)
    session.pop("user", None)
    flash("Jūs veiksmīgi izgājāt no sava konta")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)