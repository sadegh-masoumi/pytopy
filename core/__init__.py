import os

if not (os.environ.get('DEBUG') == 'True'):
    import pymysql

    pymysql.install_as_MySQLdb()
