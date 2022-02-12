def get_path_upload_avatar(instance, file):
    """
    Get account avatar path
    :param instance:
    :param file:
    :return: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instance.id}/{file}'


def get_path_upload_article_img(instance, file):
    """
    Get article image path
    :param instance:
    :param file:
    :return: (media)/avatar/user_id/photo.jpg
    """
    return f'article/{instance.id}/{file}'
