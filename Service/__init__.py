from flask import Flask, jsonify
from configparser import ConfigParser
import json

#: Get Configs
config = ConfigParser()
config.read("./config.ini")
app = Flask(__name__)


# method: index
# Testing for flask installation
# @completed
@app.route('/')
def index():
    data = dict()
    data['name'] = 'SUchedule'
    return jsonify(data)


# method: getVersion
# Get version of service
# @completed
@app.route('/version')
def getVersion():
    data = dict()
    data['name'] = 'SUchedule'
    data['term'] = '202202'
    data['version'] = 33
    data['start-date'] = '2023-02-20'
    data['end-date'] = '2023-05-26'
    return jsonify(data)


# method: getData
# Get the all lessons with their info.
# @completed
@app.route('/data')
def getData():
    data = json.load(open('./data.json'))
    data['term'] = '202202'
    data['version'] = 33
    data['infoLink'] = 'https://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=202202&crn_in='
    return jsonify(data)

if __name__ == "__main__":
    app.run(
        host=config["Service"]["host"],
        port=int(config["Service"]["port"])
    )
