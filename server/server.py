#!flask/bin/python
import re
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from algorithm import *
from random import randint

app = Flask(__name__)

# CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

STOPWORDS = ['teh', 'mah', 'atuh', 'da', 'weh']
ADDITIONWORDS = ['kami', 'mereka', 'apa', 'aku', 'saya', 'kamu', 'kita']


@app.route('/', methods=['GET'])
def welcome():
    return 'It\'s Works!', 200

@app.route('/', methods=['POST'])
def searchPattern():
    # Validate request
    if (not request.json 
        or not 'algorithm' in request.json
        or not 'words' in request.json
        or not 'default' in request.json
        ):
        abort(400)

    res = ''
    dicts = {}
    isStopWords = False
    isIndo = True
    if request.json['selected'] == 'sunda':
        isIndo = False
        removeStopWords(request.json['words'])

    if request.json['default'] or request.json['dicts']:
        if isIndo:
            dicts = loaderFile('vocab/indonesia.txt')
        else:
            dicts = loaderFile('vocab/sunda.txt')
    else:
        dicts = request.json['dicts']

    newSortedList = sorted(dicts.keys(), key=len, reverse=True)
    for i in request.json['words']:
        for j in newSortedList:
            if patternCase(request.json['algorithm'], j, i):
                temp = dicts[j]
                if isIndo:
                    if (i in ADDITIONWORDS) and not isStopWords:
                        temp += ' ' + addStopWords()
                        isStopWords = True
                res += temp + ' '
                break
        else:
            res += i + ' '
    return jsonify({'data': res}), 200


def removeStopWords(text):
    for i in STOPWORDS:
        if i in text:
            text.remove(i)
    return text

def addStopWords():
    idx = randint(0, len(STOPWORDS) - 2)
    return STOPWORDS[idx]

def loaderFile(path) :
    dicts = {}
    with open(path, 'r') as f:
        text = f.read()
        f.close()
    raw = text.split('\n')
    for key in raw:
        temp = key.split(' = ')
        if (len(temp) >= 2):
            dicts[temp[0]] = temp[1]
    return dicts


def patternCase(algorithm, pattern, text):
    if algorithm == 'Regex':
        return searchRegex(pattern.lower(), text.lower())
    if algorithm == 'Boyer':
        return searchBM(pattern.lower(), text.lower()) != -1
    if algorithm == 'KMP':
        return searchKMP(pattern.lower(), text.lower()) != -1

if __name__ == '__main__':
    app.run(debug=True)
