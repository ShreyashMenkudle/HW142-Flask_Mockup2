from flask import Flask,jsonify,request

from storage import all_articles, liked_articles, not_liked_articles
from demographic import output
from content import get_recommendations

app = Flask(__name__)

@app.route("/get-articles")

def get_articles():
    return jsonify({"data": all_articles[0],"status":"success"})


@app.route("/liked-article", methods = ["POST"])

def liked_articles():
    articles = all_articles[0] 
    all_articles = all_articles[1:] 
    liked_articles.append(articles) 
    
    return jsonify({ "status": "success" }), 201


@app.route("/not_liked-articles", methods = ["POST"])

def not_liked_articles():
    articles = all_articles[0] 
    all_articles = all_articles[1:] 
    not_liked_articles.append(articles) 
    
    return jsonify({ "status": "success" }), 201

@app.route("/popular-articles") 
def popular_articles(): 
    article_data = [] 
    for article in output: 
        _d = { 
            "url": article[0], 
            "title": article[1], 
            "text": article[2], 
            "lang": article[3], 
            "Total_events": article[4] } 
        
        article_data.append(_d) 
        
    return jsonify({ "data": article_data, "status": "success" }), 200

@app.route("/recommended-articles")

def recommended_articles(): 
    all_recommended = [] 
    
    for liked_article in liked_articles: 
        output = get_recommendations(liked_article[4]) 
        for data in output: 
            all_recommended.append(data) 
            
        import itertools 
        all_recommended.sort() 
        all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended)) 
        article_data = [] 
        for recommended in all_recommended: 
            _d = { 
                "url": recommended[11], 
                "title": recommended[12], 
                "text": recommended[13], 
                "lang": recommended[14], 
                "Total_events": recommended[15] } 
                
            article_data.append(_d) 
            
        return jsonify({ "data": article_data, "status": "success" }), 200


if __name__ == "__main__" :
    app.run()