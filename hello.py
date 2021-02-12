from flask import Flask
from flask import request
import pandas as pd
from zipfile import ZipFile

from main import *

app = Flask(__name__)

def handle_request(sampleType, whichState, sampleTechnique, sampleSize,
                  informationType, outputType):
    result = main(sampleType, whichState, sampleTechnique, sampleSize,
                  informationType, outputType)
    return result

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/getfile', methods=['GET', 'POST'])
def getfile():
    if request.method == 'POST':
        json = request.get_json()
        sampleType = json['data']['sampleType']
        whichState = json['data']['whichState']
        sampleTechnique = json['data']['sampleTechnique']
        sampleSize = json['data']['sampleSize']
        informationType = json['data']['informationType']
        outputType = json['data']['outputType']

        result = [sampleType, whichState, sampleTechnique, sampleSize,
                  informationType, outputType]
        print(result)
        output = handle_request(sampleType, whichState, sampleTechnique, sampleSize,
                  informationType, outputType)
        print(output)
        return "hello"
    else:
        return "response"
        