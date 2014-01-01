from django.conf import settings


PRINT_URL = getattr(
    settings,
    'LITTLE_PRINTER_DIRECT_PRINT_BASE_URL',
    'http://remote.bergcloud.com/playground/direct_print/'
)
