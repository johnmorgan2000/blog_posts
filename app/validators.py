from django.core.exceptions import ValidationError


def validate_not_empty(value):
    if len(value.strip()) <= 0:
        raise ValidationError('Input cannot be empty.')
