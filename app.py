from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# client = MongoClient('mongodb://test:test@13.125.214.131', 27017)
client = MongoClient('localhost', 27017)
db = client.dbfood



# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("result.html")


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_food():
    weather = request.args['weather']
    query = {
        "weather": {
            "$regex": weather
        }
    }
    print(weather, query)
    food = list(db.dbfood.find(query, {'_id': False}))
    return jsonify({'recommended_food': food})


@app.route('/api/<food>', methods=['POST'])
def like_food(food):
    action = request.args['action']
    if action == 'like':
        target_food = db.dbfood.find_one({'name': food})
        current_like = target_food['like']
        new_like = current_like + 1
        db.dbfood.update_one({'name': food}, {'$set': {'like': new_like}})
        return jsonify({'msg': 'I like It!', 'food': food})
    elif action == 'dislike':
        target_food = db.dbfood.find_one({'name': food})
        current_dislike = target_food['dislike']
        new_dislike = current_dislike + 1
        db.dbfood.update_one({'name': food}, {'$set': {'dislike': new_dislike}})
        return jsonify({"msg": "I don't like It!", 'food': food})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
