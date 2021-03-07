from flask import Flask,render_template,request

import FeatureExtraction
import pickle
import joblib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        data = FeatureExtraction.getAttributess(url)
        
        #data = [[float(x) for x in y] for y in data]
        print("Shape",data.shape)
        print(data)
        val=data.to_numpy()
        val=val.tolist()
        val[0].pop(1)
        val[0].pop(0)
        val[0].insert(0,0)
        val[0].insert(1,0)
        #val.drop(val.columns[[0]], axis=1, inplace= True)
        print(val)
        RFmodel = pickle.load(open(r'C:\Users\Ratnam\Desktop\SenTwit\DSA\BDA\ide\miniproject\Phishing-Website-Detection-master\Phishing website detection using UI\RandomForestModel.pkl', 'rb'))
        predicted_value = RFmodel.predict(val)
        #print(predicted_value)
        if predicted_value == 0:    
            value = "Legitimate"
            return render_template("home.html",error=value)
        else:
            value = "Phishing"
            return render_template("home.html",error=value)
        return render_template("home.html",error=0)
        
app.run(debug=True)