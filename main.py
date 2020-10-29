from flask import Flask,render_template,request
import pickle
with open("neet.pkl","rb") as file:
    logistic=pickle.load(file)
app = Flask(__name__)
@app.route("/demo")
def demo():
    return render_template('demo.html')
@app.route("/next")
def lamo():
    return render_template('next.html')
@app.route("/hello",methods=["GET","POST"])
def Back():
    if request.method=="POST":
        mydict=request.form
        user1=int(mydict['user1'])
        user2=int(mydict['user2'])
        user3=int(mydict['user3'])
        user4=int(mydict['user4'])
        user5=int(mydict['user5'])
        myvar=[user1,user4,user2,user3,user5]
        print([myvar])
        prob=logistic.predict_proba([myvar])[0][1]
        prob=prob*100
        if(user1<24 and user2<100):
            return render_template('next.html',inf=round(prob,2))
        else:
            return render_template('hello.html')
  
    else:
        return render_template('hello.html')
        
    

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        mydict=request.form
        user1=int(mydict['user1'])
        user2=int(mydict['user2'])
        user3=int(mydict['user3'])
        user4=int(mydict['user4'])
        user5=int(mydict['user5'])
        myvar=[user1,user4,user2,user3,user5]
        print([myvar])
        prob=logistic.predict_proba([myvar])[0][1]
        prob=prob*100
        if(user1<24 and user2<100):
            return render_template('next.html',inf=round(prob,2))
        else:
            return render_template('hello.html')
    else:
        return render_template('next.html')
    
   
if __name__ == "__main__":

    app.run(debug=True)






