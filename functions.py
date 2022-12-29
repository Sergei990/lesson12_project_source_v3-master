import json
UPLOAD_FOLDER = "uploads/images/"
# POST_PATH = "posts.json"


def load_json(POST_PATH)->list[dict] :
    """Чтение файла JSON"""
    try:
        # Открываем фаил JSON
        with open(POST_PATH, encoding='UTF-8') as file:
            #
            result = json.load(file)

    # Если нет файла JSON
    except FileNotFoundError:

        return 'Нет файла json.'
    # Если файл JSON Не список
    except json.decoder.JSONDecodeError:

        return 'Файл json не превращается в список.'
    # Если нет ошибок
    else:
        return result

all_posts = load_json(POST_PATH='posts.json')




def search_by_qwery(word:str)->list:
    """Сортировка постов"""
    search_posts = []
    for posts in all_posts:
        if word.lower() in posts['content'].lower():
            search_posts.append(posts)


    return search_posts
def save_picture(picture)->str:
    """Для сохранения фотографий"""
    filename = picture.filename

    picture.save(f'{UPLOAD_FOLDER}{filename}')
    return f'{UPLOAD_FOLDER}{filename}'


def write_new_post(new_post:dict):
    """Запись нового поста"""
    all_posts.append(new_post)

    with open('posts.json', 'w', encoding='UTF-8') as file:

        o = json.dump(all_posts, file, ensure_ascii=False)



