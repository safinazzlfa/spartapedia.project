from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import requests
import re

app = Flask(__name__)

client = MongoClient('mongodb+srv://safina:Safinamongodb@cluster0.ysbgvsy.mongodb.net/')
db = client.dbsafina

OMDB_API_KEY = "d9368fe7"


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/movie", methods=["POST"])
def movie_post():

    # ambil data dari client
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    # ambil id film dari link imdb
    match = re.search(r'tt\d+', url_receive)
    imdb_id = match.group()

    # request ke OMDb API
    api_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}"
    data = requests.get(api_url).json()

    # ambil data film
    image = data['Poster']
    title = data['Title']
    desc = data['Plot']

    # simpan ke database
    doc = {
        'image': image,
        'title': title,
        'description': desc,
        'star': star_receive,
        'comment': comment_receive
    }

    db.movies.insert_one(doc)

    return jsonify({'msg': 'Data berhasil disimpan'})


@app.route("/movie", methods=["GET"])
def movie_get():

    movie_list = list(db.movies.find({}, {'_id': False}))

    return jsonify({'movies': movie_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

#Nama : Safina Zalfalia Putri
#No Absen : 25
#Kelas : XI TKJ 4