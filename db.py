from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbfood


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def show_food():
    food = list(db.dbfood.find({}, {'_id': False}))
    return jsonify({'recommended_food': food})


@app.route('/api/post', methods=['POST'])
def love_food():
    name_receive = request.form['name_give']
    target_food = db.dbfood.find_one({'name': name_receive})

    current_love = target_food['love']
    new_love = current_love + 1

    db.dbfood.update_one({'name': name_receive}, {'$set': {'love': new_love}})

    return jsonify({'msg': 'love 완료!'})

#
# @app.route('/api/post', methods=['POST'])
# def Hate_food():
#     name_receive = request.form['name_give']
#     target_food = db.dbfood.find_one({'name': name_receive})
#
#     current_hate = target_food['love']
#     new_hate = current_hate + 1
#
#     db.dbfood.update_one({'name': name_receive}, {'$set': {'hate': new_hate}})
#
#     return jsonify({'msg': 'hate 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

db.dbfood.insert_one({'id': 1, 'name': '모둠전', 'weather': 'Rain', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 2, 'name': '우동', 'weather': 'Rain', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 3, 'name': '어묵탕', 'weather': 'Rain', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 4, 'name': '돌솥비빔밥', 'weather': 'Rain', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 5, 'name': '두부김치', 'weather': 'Rain', 'img': '', 'love': 0, 'hate': 0})

db.dbfood.insert_one({'id': 6, 'name': '설렁탕', 'weather': 'Clouds', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 7, 'name': '갈비탕', 'weather': 'Clouds', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 8, 'name': '감자탕', 'weather': 'Clouds', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 9, 'name': '국밥', 'weather': 'Clouds', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 10, 'name': '찌개', 'weather': 'Clouds', 'img': '', 'love': 0, 'hate': 0})

db.dbfood.insert_one({'id': 11, 'name': '삼겹살', 'weather': 'Dust', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 12, 'name': '소곱창', 'weather': 'Dust', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 13, 'name': '돈까스', 'weather': 'Dust', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 14, 'name': '피자', 'weather': 'Dust', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 15, 'name': '곱창전골', 'weather': 'Dust', 'img': '', 'love': 0, 'hate': 0})

db.dbfood.insert_one({'id': 16, 'name': '냉면', 'weather': 'Clear', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 17, 'name': '비빔면', 'weather': 'Clear', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 18, 'name': '냉모밀', 'weather': 'Clear', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 19, 'name': '삼계탕', 'weather': 'Clear', 'img': '', 'love': 0, 'hate': 0})
db.dbfood.insert_one({'id': 20, 'name': '물회', 'weather': 'Clear', 'img': '', 'love': 0, 'hate': 0})
