from flask import *
import pymysql

mydb=pymysql.connect(host="localhost", user="root", password="admin", database="zoho")

mycursor=mydb.cursor()
mycursor.execute("create table if not exists user(name varchar(25), email varchar(50) unique, password varchar(20));")
mydb.commit()
mycursor.close()

app=Flask(__name__)
app.secret_key=b'abcdefghijklmnopqrstuvwxyz'
@app.route("/",methods=["GET",'POST'])
def index():
    if request.method=='POST':
        mail=request.form.get('Mail')
        password=request.form.get('Password')
        conn=mydb.cursor()
        conn.execute(f"""
                     select * from user where email ="{mail}";
                     """)
        result=conn.fetchone()
        
        if not result:
            message="You are not registered"
            return render_template("login.html", message=message)
        if result[2]==password:
            session['user']=result[0]
            return render_template('home.html', user=session['user'])
        else:
            message="mail and password mismatch"
            return render_template("login.html",message=message)
        
    return render_template("login.html")

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form.get('Name')
        mail=request.form.get("Mail")
        password1=request.form.get("Password1")
        password2=request.form.get("Password2")
        if password1==password2 and len(password1)>=8:
            conn=mydb.cursor()
            try:
                conn.execute(f"""
                         insert into user (name,email,password) values ("{name}","{mail}","{password1}")
                         """)
                mydb.commit()
                conn.close()
                return redirect("/")
            except pymysql.err.IntegrityError:
                message="You are already Registered"
                return render_template('register.html', error=message)
            
        else:
            message="Check your password Either The password is mismatch or Minimum 8 characters in password"
            print(message)
            return render_template("register.html", message=message)

    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop('user',None)
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)