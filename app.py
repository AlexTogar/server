from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

def prepare(param):
    if param in request.args:
        return request.args[param]
    else:
        return ""
key = "a4ef86bd-705f-47dc-bcbd-551dab0ff43c"

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


# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=True)

