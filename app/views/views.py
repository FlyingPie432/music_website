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
    songs_info = song_search(search_query)
    return jsonify(songs_info)


def song_search(search_query):
    url = f"https://eu.hitmotop.com/?s={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_blocks = soup.find_all('li', class_='tracks__item')

    songs_info = []
    for song_block in song_blocks:
        song_title = song_block.find('div', class_='track__title').text.strip()
        author = song_block.find('div', class_='track__desc').text.strip()
        audio_link = song_block.find('a', class_='track__download-btn')['href'] if song_block.find('a') else None
        songs_info.append({'title': song_title, 'author': author, 'audio_link': audio_link})

    return songs_info
