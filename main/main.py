import json
import logging
from flask import Flask, request, Blueprint, render_template

from functions import search_by_qwery, load_json, all_posts

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.get('/')
def general_page():
    """Главная страница"""
    return render_template('index.html')


@main_blueprint.get('/search/')
def search_page():
    """"""
    try:

        word = request.args.get('s')
        search_for_posts = search_by_qwery(word)

        log_one = logging.getLogger('lod_one')
        logging.basicConfig(filename='log/log_search.txt', level=logging.INFO)

        log_one.info(f'{word}')
        

        # logging_search = logging.FileHandler('log/log_info_search.txt')
    except TypeError:
        return f'{all_posts}'

    else:

        return render_template('post_list.html', search_for_posts=search_for_posts, word=word)
