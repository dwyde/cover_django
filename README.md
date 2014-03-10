A simple Django project to test coverage.py 3.7.1.

Note: Django's FastCGI support requires the "flup" package.

# setup

    pip install -r requirements.txt
    
    <start lighttpd with the included "lighttpd.conf">

# manage.py runfcgi

`manage.py runfcgi` does not seem to work, with the included simple
lighttpd config (lighttpd version 1.4.31):

    coverage run --source=. manage.py runfcgi socket=/tmp/server.sock daemonize=false

    <browse to http://localhost:80>

    coverage report
    
    Name                    Stmts   Miss  Cover
    -------------------------------------------
    cover_django/__init__       0      0   100%
    cover_django/settings      17      0   100%
    cover_django/urls           2      2     0%
    cover_django/views          3      3     0%
    cover_django/wsgi           4      0   100%
    manage                      6      0   100%
    -------------------------------------------
    TOTAL                      32      5    84%


# manage.py runserver

`manage.py runserver --noreload` works correctly:

    coverage run --source=. manage.py runserver --noreload
    
    <browse to http://localhost:8000>
    
    coverage report
    
    Name                    Stmts   Miss  Cover
    -------------------------------------------
    cover_django/__init__       0      0   100%
    cover_django/settings      17      0   100%
    cover_django/urls           2      0   100%
    cover_django/views          3      0   100%
    cover_django/wsgi           4      0   100%
    manage                      6      0   100%
    -------------------------------------------
    TOTAL                      32      0   100%

