from distutils.core import setup

setup(
    name='karlooper',
    version='0.2.0',
    packages=[
        'karlooper',
        'karlooper.autoreload',
        'karlooper.config',
        'karlooper.escape',
        'karlooper.http_parser',
        'karlooper.logger',
        'karlooper.router',
        'karlooper.template',
        'karlooper.utils',
        'karlooper.web'
    ],
    data_files=[
        ('lib/python2.7/dist-packages/karlooper/logger', ['karlooper/logger/log.conf']),
        ('lib/python2.7/site-packages/karlooper/logger', ['karlooper/logger/log.conf'])
    ],
    url='https://github.com/karldoenitz/karlooper',
    license='',
    author='lizhihao',
    author_email='karlvorndoenitz@gmail.com',
    description='karloop plus frame work'
)
