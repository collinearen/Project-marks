from account.logging_formatters import CustomJsonFormatter

LOG_SET = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_format': {
            'format': "{asctime}    {levelname}    {filename}    {message}",
            'style': "{"
        },
        'json_formatter': {
            '()': CustomJsonFormatter,
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            # На консоль я оставлю main formatter, так как было изначально в Django
            'formatter': 'main_format',
        },

        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'json_formatter',
            # А на запись в файл я поставлю json formatter
            'filename': "information.log"
        }
    },
    'loggers': {
        "main": {
            "handlers": ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
