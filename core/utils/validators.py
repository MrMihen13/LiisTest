from django.core.exceptions import ValidationError


def image_size_validator(file_obj):
    """
    Check image size
    :param file_obj:
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'Максимальной размер файла {megabyte_limit}MB')


def custom_password_validator(password):

    if not any(c.isdigit() for c in password):
        raise ValidationError('Password must container at least 1 digits.')

    if not any(c.isupper() for c in password):
        raise ValidationError('Password must container at least 1 uppercase letter.')
