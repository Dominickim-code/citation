from scholarly import scholarly
from flask import Flask, render_template, jsonify, request

# import socketserver
# import threading
#
# HOST = 'localhost'
# PORT = 5000
# lock = threading.Lock()

app = Flask(__name__)


# 'Perception of physical stability and center of mass of 3D objects'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/book', methods=['GET'])
def get_citation():
    keyword_receive = request.args.get('search')
    print(keyword_receive)

    raw_citation_info = scholarly.search_pubs(keyword_receive.replace("'", ""))
    citation_info = next(raw_citation_info)

    author = citation_info['bib']['author']
    pub_year = citation_info['bib']['pub_year']
    title = citation_info['bib']['title']
    pub_url = citation_info['pub_url']
    venue = citation_info['bib']['venue']
    abstract = citation_info['bib']['abstract']

    bib = {
        'author': author,
        'pub_year': pub_year,
        'title': title,
        'venue': venue,
        'abstract': abstract
    }

    print(bib)

    # return jsonify({'result': 'success', 'citation': bib, 'author':author,'title': title, 'venue': venue,'pub_year': pub_year,
    #                 pub_url: pub_url})
    return jsonify({'result': 'success'})


@app.route('/book2', methods=['GET'])
def get_citation2():
    keyword_receive = request.args.get('search')
    print(keyword_receive)

    raw_citation_info = scholarly.search_pubs(keyword_receive.replace("'", ""))
    citation_info = next(raw_citation_info)

    author = citation_info['bib']['author']
    pub_year = citation_info['bib']['pub_year']
    title = citation_info['bib']['title']
    pub_url = citation_info['pub_url']
    venue = citation_info['bib']['venue']
    abstract = citation_info['bib']['abstract']

    bib = {
        'author': author,
        'pub_year': pub_year,
        'title': title,
        'venue': venue,
        'abstract': abstract
    }

    print(bib)

    # return jsonify({'result': 'success', 'citation': bib, 'author':author,'title': title, 'venue': venue,'pub_year': pub_year,
    #                 pub_url: pub_url})
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
