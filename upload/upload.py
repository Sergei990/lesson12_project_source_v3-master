import logging

from flask import Blueprint, render_template, request

from error_ import picture_extension_error
from functions import save_picture, write_new_post, all_posts

uploader_blueprint = Blueprint('uploader_blueprint', __name__, template_folder='templates')


@uploader_blueprint.get('/post/')
def post_form():
    """"""
    return render_template('post_form.html')


@uploader_blueprint.post('/post/')
def append_post():
    """"""
    try:

        picture = request.files.get('picture')

        content = request.form.get('content')

        save_pictures = save_picture(picture)

        new_post = {'pic': '/' + save_pictures, 'content': content.capitalize()}

        write_new_post(new_post)

        picture_extension_error(picture)

    except PermissionError:
        return 'Ошибка загрузки фотографии'

    except NameError:
        log_error_load_fila = logging.getLogger('log_error_load_file')
        logging.basicConfig(filename='log_two/error_log.txt', level=logging.ERROR)
        log_error_load_fila.error('error load fila')
        return 'Ошибка при загрузке файла'

    except AttributeError:

        return f'{all_posts}'

    else:
        return render_template('post_uploaded.html', new_post=new_post)
