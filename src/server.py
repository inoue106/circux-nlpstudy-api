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

@app.route('/wnjpn/<word>', methods=["GET"])
def wnjpn(word):
    # 問い合わせしたい単語がWordnetに存在するか確認する
    cur = conn.execute("select wordid from word where lemma='%s'" % word)
    word_id = 99999999  #temp 
    for row in cur:
        word_id = row[0]

    # Wordnetに存在する語であるかの判定
    if word_id==99999999:
        print("「%s」は、Wordnetに存在しない単語です。" % word)
        return jsonify({
                'status': 'NG',
                'message': ("「%s」は、Wordnetに存在しない単語です。" % word)
            })
    else:
        print("【「%s」の類似語を出力します】\n" % word)

    # 入力された単語を含む概念を検索する
    cur = conn.execute("select synset from sense where wordid='%s'" % word_id)
    synsets = []
    for row in cur:
        synsets.append(row[0])

    # 概念に含まれる単語を検索して画面出力する
    results = []
    no = 1
    for synset in synsets:
        cur1 = conn.execute("select name from synset where synset='%s'" % synset)
        for row1 in cur1:
            print("%sつめの概念 : %s" %(no, row1[0]))
        cur2 = conn.execute("select def from synset_def where (synset='%s' and lang='jpn')" % synset)
        sub_no = 1
        for row2 in cur2:
            print("意味%s : %s" %(sub_no, row2[0]))
            sub_no += 1
        cur3 = conn.execute("select wordid from sense where (synset='%s' and wordid!=%s)" % (synset,word_id))
        sub_no = 1
        for row3 in cur3:
            target_word_id = row3[0]
            cur3_1 = conn.execute("select lemma from word where wordid=%s" % target_word_id)
            for row3_1 in cur3_1:
                results.append(row3_1[0])
                print("類義語%s : %s" % (sub_no, row3_1[0]))
                sub_no += 1
        print("\n")
        no += 1

    return jsonify({
            'status': 'OK',
            'result': results
        })

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['JSON_AS_ASCII'] = False
    app.run(debug = True, host='0.0.0.0', port=8888)
