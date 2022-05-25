from flask import Flask, render_template,request, redirect,session

app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'

@app.route('/')
def index():
    print(session)
    if session=={}:
        session['count']=1
        session['visited']=1
    else:
        session['count']+=1
        session['visited']+=1
            
    return render_template("index.html")

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    # print(session)
    session.clear()
    return redirect('/')

@app.route('/2button', methods=['POST'])
def add_2():
    session['count']=session['count']+1
    session['visited']-=1
    return redirect('/')

@app.route('/set_incrementer', methods=['POST'])
def set_increment():
    
    session['count']=session['count']+int(request.form['increment'])-1
    session['visited']-=1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)