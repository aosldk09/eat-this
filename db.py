from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbfood
db.dbfood.delete_many({})

db.dbfood.insert_one(
    {'id': 1, 'name': '모둠전', 'weather': 'Rain', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 2, 'name': '불고기전골', 'weather': 'Rain', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 3, 'name': '어묵탕', 'weather': 'Rain', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 4, 'name': '돌솥비빔밥', 'weather': 'Rain', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 5, 'name': '두부김치', 'weather': 'Rain', 'img': '', 'like': 0, 'dislike': 0})

db.dbfood.insert_one(
    {'id': 6, 'name': '설렁탕', 'weather': 'Clouds', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 7, 'name': '갈비탕', 'weather': 'Clouds', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 8, 'name': '감자탕', 'weather': 'Clouds', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 9, 'name': '국밥', 'weather': 'Clouds', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 10, 'name': '찌개', 'weather': 'Clouds', 'img': '', 'like': 0, 'dislike': 0})

db.dbfood.insert_one(
    {'id': 11, 'name': '삼겹살', 'weather': 'Dust', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 12, 'name': '소곱창', 'weather': 'Dust', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 13, 'name': '돈까스', 'weather': 'Dust', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 14, 'name': '피자', 'weather': 'Dust', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 15, 'name': '곱창전골', 'weather': 'Dust', 'img': '', 'like': 0, 'dislike': 0})

db.dbfood.insert_one(
    {'id': 16, 'name': '냉면', 'weather': 'Clear', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 17, 'name': '비빔면', 'weather': 'Clear', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 18, 'name': '냉모밀', 'weather': 'Clear', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 19, 'name': '삼계탕', 'weather': 'Clear', 'img': '', 'like': 0, 'dislike': 0})
db.dbfood.insert_one(
    {'id': 20, 'name': '물회', 'weather': 'Clear', 'img': '', 'like': 0, 'dislike': 0})
