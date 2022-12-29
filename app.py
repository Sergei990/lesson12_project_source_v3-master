import json
import logging


from flask import Flask, request, render_template, send_from_directory

from error_ import  PictureError
# from error_ import error
# from functions import ...
from main.main import main_blueprint
from upload.upload import uploader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

app.register_blueprint(uploader_blueprint)


@app.errorhandler(PictureError)
def picture_error(PictureError):
    """Ощибка расшерения файла,"""
    log_three = logging.getLogger('log_three')
    logging.basicConfig(filename='/log_three/log_three.txt', level=logging.INFO)
    log_three.info('The uploaded file is not a jpeg,png,jpg extension.')


    return 'Загруженный фаил не кертинка расшерения jpeg,png,jpg.'





@app.route("/uploads/<path:path>")

def static_dir(path):
    """Даёт доступ к файлам из дерeктории uploads"""
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
