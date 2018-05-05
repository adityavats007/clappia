

from dbconnect import connection

from flask import Flask, render_template, flash, request, url_for, redirect, session,jsonify


from flask_wtf import FlaskForm
from functools import wraps
import gc
import datetime




app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/',methods=['GET','POST'])
def homepage():
       
       error=''
       z=datetime.datetime.now().strftime ("%Y-%m-%d")
       return render_template("page1.html",error=error,z=z)
       #

      # try:
       #     if request.method == "POST" and form.validate():
         #       username  = form.username.data
        #        email = form.email.data
         #       password = sha256_crypt.encrypt((str(form.password.data)))
         #       c, conn = connection()
           
@app.route('/page2/',methods=['GET','POST'])
def page2():
    cu, conn=connection()
    y1="UPDATE options set a0=1,a1=1,a2=1,a3=1,a4=1,a5=1 WHERE uid=1"
    y=cu.execute(y1,())
    y=cu.fetchall()
    conn.commit()
    cu.close()
    conn.close()
    return render_template("page2.html")
           
@app.route('/nextpage/',methods=['GET','POST'])
def nextpage():
    i=0
    var1=''
    var2=''
    var3=''
    var4=''
    var5=''
    var6=''
    x=[]
    if request.method == 'POST':
        cu, conn=connection()
        x1 = "SELECT * FROM options"
        x = cu.execute(x1,)
        x=cu.fetchall()
        jsonify(x)
        conn.commit()
        cu.close()
        conn.close()
        # flash(x)
        if x[0][1]==1:# name
             var1='checked' 
        if x[0][2]==1:# exp
             var2='checked'
        if x[0][3]==1:# loc
             var3='checked'
        if x[0][4]==1:# date
             var4='checked'
        if x[0][5]==1:# skill
             var5='checked'
        if x[0][6]==1:# gender
             var6='checked'
        
    return render_template("page3.html",var1=var1,var2=var2,var3=var3,var4=var4,var5=var5,var6=var6,x=x)
@app.route('/testpage1/',methods=['GET','POST'])
def testpage1():
    i=1
    A0=0
    A1=0
    A2=0
    A3=0
    A4=0
    A5=0
    l=request.form.getlist('java')
    if 'Name' in l:
                A0=1
    if 'Experience' in l:
                A1=1
    if 'location' in l:
                A2=1
    if 'Date' in l:
                A3=1
    if 'Skills' in l:
                A4=1
    if 'Gender' in l:
                A5=1
    cu, conn=connection()
    x1 = "SELECT * FROM test2"
    x = cu.execute(x1,)
    x=cu.fetchall()
    jsonify(x)
    conn.commit()
    cu.close()
    conn.close()
    cu, conn=connection()
    y1="UPDATE options set a0=%s,a1=%s,a2=%s,a3=%s,a4=%s,a5=%s WHERE uid=1"
    y=cu.execute(y1,(A0,A1,A2,A3,A4,A5))
    y=cu.fetchall()
    conn.commit()
    cu.close()
    conn.close()
    cu, conn=connection()
    variable='checked'
    #z1="SELECT * FROM options WHERE uid=1"
    #z=cu.execute(z1,)
   # z=cu.fetchall()
    #conn.commit()
    #cu.close()
    #conn.close()
    return render_template("page2.html",variable=variable,l=l,i=i,a0=A0,a1=A1,a2=A2,a3=A3,a4=A4,a5=A5,x=x)
@app.route('/dashboard/',methods=['GET','POST'])
def dashboard():
    return render_template("dashboard.html")
@app.route("/page1/")
def page1():
    c, conn=connection()
    return render_template("page1.html")
@app.route('/testpage/',methods=['GET','POST'])
def testpage():
    i=0
    j=""
    p=""
    h=""
    c=""
    a=""
    l=[""]
    try:
        
            
            if request.method == 'POST':
                #flash("You have been  out!")
                name=request.form['username']
                exp=request.form['exp']
                loc=request.form['City']
                date=request.form['date']
                l=request.form.getlist('java')
                length=len(l)
                if 'JAVA' in l:
                            j='JAVA'
                if 'PYTHON' in l:
                            p='PYTHON'
                if 'HTML' in l:
                            h='HTML'
                if 'CSS' in l:
                            c='CSS'
                if 'ANGULAR' in l:
                            a='ANGULAR'
                
                    
                gender=request.form['gender']
                cu, conn=connection()
            if loc=="None":
                flash("Please choose a valid location from the dropdown")
                return redirect(url_for('page1'))
            sql_insert_reg = "INSERT INTO test2 (name,exp,loc,date,j,p,h,c,a,gender) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cu.execute(sql_insert_reg, (name,exp,loc,date,j,p,h,c,a,gender))
            x1 = "SELECT * FROM test2"
            x = cu.execute(x1,)
            x=cu.fetchall()
            jsonify(x)
            conn.commit()
            cu.close()
            conn.close()
            #sql_insert_reg = "INSERT INTO test1 (user,exp,loc,date,j,p,h,c,a,gender) VALUES (%s, %d, %s,%s,%s,%s,%s,%s,%s,%s)"
            #c.execute(sql_insert_reg, (user,exp,loc,date,j,p,h,c,a,gender))
            #conn.commit()
            #c.close()
            #conn.close()
            #gc.collect()###
            i=0
            return render_template("page2.html",x=x,i=i)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('page1'))
        return(str(e))
        
            
            
            

@app.route('/profile/')
def profile():
    user=session['username']
    l=['user','email','password']
    return render_template("profile.html",user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#


if __name__ == "__main__":
    
    app.run()
   
