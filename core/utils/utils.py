from django.core.exceptions import ValidationError


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


def validate_size_image(file_obj):
    """
    Check image size
    :param file_obj:
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Максимальной размер файла {megabyte_limit}MB')
