import datetime
import hashlib
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, session
from config import MyClass
import secrets

# Generate a secure random secret key
secret_key = secrets.token_hex(16)

# Set the secret key in your Flask application


app = Flask(__name__)
app.secret_key = secret_key

cred = MyClass()
username = MyClass.username
password = MyClass.password

data = {}
name = ''
passw = ''


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/get_data_overview', methods=["GET", "POST"])
def get_data_overview():
    if request.method == 'POST':
        get_data("overview")
    return render_template('thanks.html')


@app.route('/get_data_enquire', methods=["GET", "POST"])
def get_data_enquire():
    if request.method == 'POST':
        get_data("enquire")
    return render_template('thanks.html')


@app.route('/get_data_config', methods=["GET", "POST"])
def get_data_price():
    if request.method == 'POST':
        get_data("config")
    return render_template('thanks.html')


@app.route('/get_data_contact', methods=["GET", "POST"])
def get_data_contact():
    if request.method == 'POST':
        get_data("contact")
    return render_template('thanks.html')


@app.route('/get_data_ameni', methods=["GET", "POST"])
def get_data_ameni():
    if request.method == 'POST':
        get_data("ameni")
    return render_template('thanks.html')


def get_data(name_type):
    name = request.form[f"{name_type}-name"]
    phone = request.form.get(f"{name_type}-phone")
    email = request.form.get(f"{name_type}-email")
    time = datetime.datetime.now().strftime("%b %d, %Y")
    print(time)
    data = pd.DataFrame({"Name": [name], "Phone": [phone], "Email": [email], "Time": [time]})
    reader = pd.read_excel("Customer Data.xlsx")
    writer = pd.ExcelWriter('Customer Data.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")
    data.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)
    writer.close()


@app.route('/admin', methods=["GET", "POST"])
def admin():
    global data
    if 'name' in session:
        if request.method == 'POST':
            start_date = datetime.datetime.strptime(request.form['start'], "%b %d, %Y")
            end_date = datetime.datetime.strptime(request.form['end'], "%b %d, %Y")
            print(start_date)
            print(end_date)
            file = pd.read_excel("Customer Data.xlsx")
            print(len(file.values))
            table_data = []
            for i in range(0, len(file.values)):
                c_date = datetime.datetime.strptime(file.values[i][3], "%b %d, %Y")
                if start_date <= c_date <= end_date:
                    print(file.values[i][3])
                    table_data.append(file.values[i])
            data = {
                'table_data': table_data
            }
            return render_template('admin.html', data=data)
        return render_template('admin.html', data=data)
    else:
        return redirect(url_for('admin_login'))


@app.route('/admin_login', methods=["GET", "POST"])
def admin_login():
    global name, passw, username, password
    if request.method == 'POST':
        name = str(hashlib.sha256(request.form['name'].encode()).hexdigest())
        passw = str(hashlib.sha256(request.form['password'].encode()).hexdigest())

        if name == username and passw == password:
            session['name'] = name
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('admin_login'))
    return render_template('admin-login.html')


@app.route('/logout', methods=['POST'])
def logout():
    del session['name']
    return redirect(url_for('admin_login'))


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
