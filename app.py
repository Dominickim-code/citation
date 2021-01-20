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
    # scholarly.pprint(citation_info)
    # print(citation_info)
    # print(citation_info['bib']['author'])
    # print(citation_info['bib']['pub_year'])
    # print(citation_info['bib']['title'])
    # print(citation_info['pub_url'])

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

    """
    'author' => ['bib']['author']
    'pub_year' -> ['bib']['pub_year']
    'title' ['bib']['title']
    'pub_url' ['pub_url']


    {'container_type': 'Publication', 
    'source': <PublicationSource.PUBLICATION_SEARCH_SNIPPET: 1>, 
    'bib': 
        {'title': 'Language and power: An introduction to institutional discourse', 
        'author': ['A Mayr'], 
        'pub_year': '2008', 
        'venue': 'NA', 
        'abstract': 'How language is used in institutions and how institutions generate language is a key concern of both sociolinguistics and social theory. This readable and comprehensive introduction to language and power in institutions combines theoretical reflection with a'}, 
    'filled': False, 
    'gsrank': 1, 
    'pub_url': 'https://books.google.com/books?hl=en&lr=&id=7mw5LHs5C2kC&oi=fnd&pg=PR5&dq=Language+and+power:+An+introduction+to+institutional+discourse&ots=Ox7JAsoEAa&sig=tvJVFjYSdiYWNJlvA6Ime4oPjj4', 
    'author_id': [''], 
    'num_citations': 373, 
    'url_scholarbib': '/scholar?q=info:54vTINUitb0J:scholar.google.com/&output=cite&scirp=0&hl=en', 
    'url_add_sclib': '/citations?hl=en&xsrf=&continue=/scholar%3Fq%3DLanguage%2Band%2Bpower:%2BAn%2Bintroduction%2Bto%2Binstitutional%2Bdiscourse%26hl%3Den%26as_sdt%3D0,33&citilm=1&json=&update_op=library_add&info=54vTINUitb0J&ei=ADoFYPmpD8u0ywSA3Itw', 
    'citedby_url': '/scholar?cites=13669870542727121895&as_sdt=5,33&sciodt=0,33&hl=en', 
    'eprint_url': 'https://idoc.pub/documents/language-and-power-an-introduction-to-institutional-discourse-134w61v9own7'
    }
    """

    # dict = scholarly.pprint(citation_info)
    #  return render_template('index.html')
    return jsonify({'result': 'success', 'citation': bib, 'pub_year': pub_year, 'title': title, 'author': author,
                    'venue': venue,pub_url: pub_url})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
