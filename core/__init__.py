import os

if True if os.environ.get('DEBUG') == 'True' else False:
    import pymysql
    pymysql.install_as_MySQLdb()