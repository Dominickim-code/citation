from scholarly import  scholarly
from flask import Flask, render_template,jsonify,request

app = Flask(__name__)

# 'Perception of physical stability and center of mass of 3D objects'
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET'])
def get_citation():
    keyword_receive = request.args.get('search')
    print(keyword_receive)
    raw_citation_info = scholarly.search_pubs(keyword_receive.replace("'",""))
    citation_info = next(raw_citation_info)
    scholarly.pprint(citation_info)
    
    # dict = scholarly.pprint(citation_info)
    # return render_template('index.html', result=dict)
    return jsonify({'result': 'success', 'citation': 'temp','name': '','affiliation': '', })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
