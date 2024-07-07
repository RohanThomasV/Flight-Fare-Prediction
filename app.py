 
from flask import Flask,render_template,request
import pickle

model=pickle.load(open('flight_price_prediction.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("data.html")
@app.route("/predict", methods=["POST"])
def predict():
    if request.method=="POST":
        airline = int(request.form["airlines"])
        source = int(request.form["source"])
        destination	 = int(request.form["destination"])
        stops = int(request.form["stops"])
        dhours= int(request.form["dtime"].split(':')[0])
        dmins = int(request.form["dtime"].split(':')[1])
        jday = int(request.form["jdate"].split('-')[0])
        jmonth = int(request.form["jdate"].split('-')[1])
        
        durahours = int(request.form["duratime"].split(':')[0])
        duramins = int(request.form["duratime"].split(':')[1])
        arrhours = int(request.form["arrtime"].split(':')[0])
        arrmins = int(request.form["arrtime"].split(':')[1])
        pred =model.predict([[airline,source,destination,stops,dhours,dmins,jday,jmonth,durahours,duramins,arrhours,arrmins]])
        print(pred)
        return render_template('data.html',result=pred)
     
if __name__=='__main__':
    app.run(debug=True,port=5002)