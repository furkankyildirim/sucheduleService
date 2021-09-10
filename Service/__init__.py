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
    return jsonify(Home='SUchedule')


# method: getData
# Get the all lessons with their info.
# @completed
@app.route('/suchedule/data')
def getData():
    data = json.load(open('./data.json'))
    data['term'] = '202101'
    data['infoLink'] = 'https://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=202101&crn_in='
    return jsonify(data)


if __name__ == "__main__":
    app.run(
        host=config["Service"]["host"],
        port=int(config["Service"]["port"])
    )
