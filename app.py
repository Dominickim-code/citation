from scholarly import scholarly
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET'])
def get_citation():

    keyword_receive = request.args.get('search')
    print(keyword_receive)

    raw_citation_info = scholarly.search_pubs(keyword_receive.replace("'", ""))

    citation_info = next(raw_citation_info)
    scholarly.bibtex(citation_info)

    author = citation_info['bib']['author']
    title = citation_info['bib']['title']
    pub_year = citation_info['bib']['pub_year']
    venue = citation_info['bib']['venue']
    location =citation_info['bib']['publisher']

    return jsonify({'result': 'success', 'author':author,'title': title, 'venue': venue,'pub_year': pub_year,
                    'location':location})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
