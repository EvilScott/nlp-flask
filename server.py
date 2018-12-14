from dragnet import extract_content, extract_content_and_comments
from flask import Flask, jsonify, request
from gensim.summarization import keywords as textrank_keywords
from nlp.rake import rake_keywords

# silence deprecation warnings
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

app = Flask(__name__)


@app.route('/dragnet/content', methods=['POST'])
def dragnet_extract_content():
    return extract_content(request.data)


@app.route('/dragnet/content-comments', methods=['POST'])
def dragnet_extract_content_and_comments():
    return extract_content_and_comments(request.data)


@app.route('/gensim/textrank-keywords', methods=['POST'])
def gensim_textrank_keywords():
    return jsonify(textrank_keywords(request.data, split=True, lemmatize=True))


@app.route('/nlp/rake-keywords', methods=['POST'])
def nlp_rake_keywords():
    return jsonify(rake_keywords(request.data))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
