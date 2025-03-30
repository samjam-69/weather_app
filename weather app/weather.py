from flask import Flask,render_template,request
import requests
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
@app.route("/calculate",methods=["POST"])
def calc():
    if request.method == 'POST':
        url = "http://api.weatherapi.com/v1/forecast.json"
        api_key = "a986235e67d446fdaa1190241252903"
        query = request.form.get("city")
        params = {
            "key": api_key,
            "q": query,
            "aqi": "no",
            "days":7
            
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return render_template("sec.html",weather_data=data)
    

        else:
            return render_template("sec.html", error="Error: Could not retrieve weather data")
if __name__=="__main__":
    app.run(debug=True)

    
