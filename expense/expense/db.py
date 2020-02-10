import dj_database_url
from decouple import config


class DB:
    @classmethod
    def config(cls, debug):
        return cls.development() if debug else cls.production()

    @classmethod
    def production(cls):
        return {
            'default': {
                **dj_database_url.parse(config('DATABASE_URL')),
                'ENGINE': 'django.db.backends.postgresql'
            }
        }

    # LOCAL ENV
    # @classmethod
    # def development(cls):
    #     return {
    #         'default': {
    #             'ENGINE': 'django.db.backends.postgresql',
    #             'NAME': 'postgres',
    #             'HOST': '127.0.0.1',
    #             'USER': 'postgres',
    #             'PASSWORD': 'olatunde123',
    #         }
    #     }
        
    # DOCKER
    @classmethod
    def development(cls):
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'expensedb',
                'HOST': 'db',
                'USER': config('DBUSER'),
                'PASSWORD': config('DBPASSWD'),
            }
        }
