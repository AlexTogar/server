from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    #prepare parameters
    lat = prepare("lat")
    lon = prepare("lon")
    if lat == "":
        lat = "55.675813"
    if lon == "":
        lon = "37.532349"
    #creating query
    url = 'https://api.weather.yandex.ru/v1/forecast?lat=%s&lon=%s' %(lat, lon)
    header = {'X-Yandex-API-Key': key}
    #getting response
    response = requests.get(url, headers=header).json()
    #parse response
    fact = response["fact"]
    temperature = fact["temp"]
    wind_speed = fact["wind_speed"] #speed of find
    humidity = fact["humidity"]
    #return result as json

    return jsonify({"temperature": temperature,
    "wind_speed": wind_speed,
    "humidity": humidity})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
