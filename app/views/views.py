from flask import Blueprint, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

main_bp = Blueprint('main', __name__)

cookies = {
    'userid': '671e035d-2c92-4671-802f-2fae6504c544',
    'uuid': '671e035d-2c92-4671-802f-2fae6504c544',
    'oid': '0yC7LPk7yRtYtLLHlnVI',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain;charset=UTF-8',
    # 'Cookie': 'userid=671e035d-2c92-4671-802f-2fae6504c544; uuid=671e035d-2c92-4671-802f-2fae6504c544; oid=0yC7LPk7yRtYtLLHlnVI',
    'Origin': 'https://eu.hitmotop.com',
    'Referer': 'https://eu.hitmotop.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = '{"visitor_id":"671e035d-2c92-4671-802f-2fae6504c544","utm_source":"kd","utm_campaign":341672,"utm_content":"","domain":"hitmotop.com","proto":"https:","mode":"strict_native"}'

response = requests.post('https://wogimyk.com/88467', cookies=cookies, headers=headers, data=data)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/music', methods=['POST'])
def get_music():
    search_query = request.form['search_query']
    songs = songs_title(search_query)
    return jsonify(songs)


def songs_title(search_query):
    url = f"https://eu.hitmotop.com/?s={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    song_blocks = soup.find_all('div', class_='content-inner')

    song_titles = []
    for song_block in song_blocks:
        song_title = song_block.find('h1', class_='').text.strip()
        song_titles.append(song_title)

    return song_titles
