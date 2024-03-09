from flask import Flask, render_template, request, jsonify, Blueprint
from bs4 import BeautifulSoup
import requests

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/music', methods=['POST'])
def get_music():
    search_query = request.form.get('search_query')
    song_info = songs_search(search_query)
    return jsonify(song_info)


def songs_search(search_query):
    url = f"https://eu.hitmotop.com/?s={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_blocks = soup.find_all('li', class_='tracks__item')

    songs_info = []
    for song_block in song_blocks:
        song_title = song_block.find('div', class_='track__title').text.strip()
        author = song_block.find('div', class_='track__desc').text.strip()
        songs_info.append({'title': song_title, 'author': author})

    return songs_info


me = songs_search('test')
print(me)
