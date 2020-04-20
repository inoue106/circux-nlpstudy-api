from flask import Flask, render_template, request, jsonify
from gensim.models import KeyedVectors
import spacy
import sqlite3
conn = sqlite3.connect("wnjpn.db")

app = Flask(__name__)
MODEL_FILENAME = "models/stanby-jobs-200d-word2vector.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)
nlp = spacy.load('ja_ginza')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=["POST"])
def recognize():
    data = []
    word = ''
    if ('w' in request.form):
        word = request.form["w"]
    if ('w' in request.args):
        word = request.args.get('w')
    app.logger.debug('word:' + word)
    doc = nlp(word)

    for sent in doc.sents:
        for token in sent:
            t = {
                'i':token.i,
                'orth':token.orth_,
                'lemma':token.lemma_,
                'pos':token.pos_,
                'tag':token.tag_, 
                'dep':token.dep_, 
                'head':token.head.i
            }
            data.append(t)

    return jsonify({
            'status': 'OK',
            'data': data
        })

@app.route('/similarity', methods=["POST"])
def similarity():
    data = []
    word1 = ''
    if ('w1' in request.form):
        word1 = request.form["w1"]
    word2 = ''
    if ('w2' in request.form):
        word2 = request.form["w2"]
    doc1 = nlp(word1)
    doc2 = nlp(word2)
    s = doc1.similarity(doc2)

    return jsonify({
            'status': 'OK',
            'similarity': s
        })

@app.route('/most-similar', methods=["POST"])
def top5():
    word = ''
    num = 5
    if ('w' in request.form):
        word = request.form["w"]
    if ('n' in request.form):
        num = request.form["n"]
    s = w2v.most_similar(word, topn=int(num))

    return jsonify({
            'status': 'OK',
            'similarity': s
        })

@app.route('/wnjpn', methods=["GET"])
def wnjpn():
    cur = conn.execute("select name from sqlite_master where type='table'")
    for row in cur:
        print(row)
    return jsonify({
            'status': 'OK'
        })

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['JSON_AS_ASCII'] = False
    app.run(debug = True, host='0.0.0.0', port=8888)
