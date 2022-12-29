class PictureError(Exception):
    pass


def picture_extension_error(photo):
    """Обрабтка собственых ошибок"""
    #
    extension = {'jpeg', 'png', 'jpg'}
    #
    filename = str(photo.filename)
    #
    file = filename.split('.')[-1]
    #
    if not file in extension:
        #
        raise PictureError
    #
    return PictureError



