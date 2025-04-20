PS E:\Final5\luminooo> .\env\Scripts\activate 
(env) PS E:\Final5\luminooo> cd .\luminooo_api\
Package           Version
----------------- -------
asgiref           3.8.1
Django            5.2
pip               24.2
psycopg           3.2.6
sqlparse          0.5.3
typing_extensions 4.13.2
tzdata            2025.2
(env) PS E:\Final5\luminooo\luminooo_api> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
(env) PS E:\Final5\luminooo\luminooo_api> py manage.py makemigrations
Migrations for 'main':
    + Create model CourseCategory
    + Create model Student
    + Create model Teacher
    + Create model Course
(env) PS E:\Final5\luminooo\luminooo_api> py manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, main, sessions
Running migrations:
  Applying main.0001_initial... OK
(env) PS E:\Final5\luminooo\luminooo_api> py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 20, 2025 - 17:33:28
Django version 5.2, using settings 'luminooo_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[20/Apr/2025 17:33:36] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[20/Apr/2025 17:33:37] "GET /favicon.ico HTTP/1.1" 404 2214
[20/Apr/2025 17:34:04] "GET /admin/ HTTP/1.1" 302 0
[20/Apr/2025 17:34:04] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4184
[20/Apr/2025 17:34:04] "GET /static/admin/css/dark_mode.css HTTP/1.1" 304 0
[20/Apr/2025 17:34:04] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[20/Apr/2025 17:34:04] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[20/Apr/2025 17:34:04] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[20/Apr/2025 17:34:04] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[20/Apr/2025 17:34:10] "POST /admin/login/?next=/admin/ HTTP/1.1" 200 4352
[20/Apr/2025 17:34:45] "POST /admin/login/?next=/admin/ HTTP/1.1" 200 4352
[20/Apr/2025 17:34:57] "POST /admin/login/?next=/admin/ HTTP/1.1" 200 4352
[20/Apr/2025 17:36:10] "POST /admin/login/?next=/admin/ HTTP/1.1" 200 4352
[20/Apr/2025 17:36:20] "POST /admin/login/?next=/admin/ HTTP/1.1" 200 4352
(env) PS E:\Final5\luminooo\luminooo_api> py manage.py deletesuperuser
Unknown command: 'deletesuperuser'. Did you mean createsuperuser?
Type 'manage.py help' for usage.
(env) PS E:\Final5\luminooo\luminooo_api> python manage.py shell
10 objects imported automatically (use -v 2 for details).

Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> User.objects.filter(is_superuser=True)
<QuerySet []>
>>> from django.db import connection
{'ENGINE': 'django.db.backends.postgresql', 'NAME': 'luminooo_db', 'USER': 'luminooo_user', 'PASSWORD': 'RUNLATERALinfosys@1994', 'HOST': 'localhost', 'PORT': '5432', 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True, 'CONN_MAX_AGE': 0, 'CONN_HEALTH_CHECKS': False, 'OPTIONS': {}, 'TIME_ZONE': None, 'TEST': {'CHARSET': None, 'COLLATION': None, 'MIGRATE': True, 'MIRROR': None, 'NAME': None}}
>>> from django.contrib.auth.models import User
>>> print(User.objects.all())
>>> ^Z

now exiting InteractiveConsole...
(env) PS E:\Final5\luminooo\luminooo_api> py manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: sharmaearth4@gmail.com
Password:
Password (again):
Superuser created successfully.
(env) PS E:\Final5\luminooo\luminooo_api> py manage.py runserver      
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 20, 2025 - 17:57:23
Django version 5.2, using settings 'luminooo_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[20/Apr/2025 17:57:45] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[20/Apr/2025 17:57:46] "GET /admin/ HTTP/1.1" 200 8949
[20/Apr/2025 17:57:46] "GET /static/admin/css/dashboard.css HTTP/1.1" 304 0
[20/Apr/2025 17:57:46] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 304 0
[20/Apr/2025 17:57:46] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 304 0
E:\Final5\luminooo\luminooo_api\main\models.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 20, 2025 - 18:00:47
Django version 5.2, using settings 'luminooo_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
E:\Final5\luminooo\luminooo_api\main\models.py changed, reloading.
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "E:\MTECH_hands-ON\python\Lib\threading.py", line 1075, in _bootstrap_inner
    self.run()
  File "E:\MTECH_hands-ON\python\Lib\threading.py", line 1012, in run
    self._target(*self._args, **self._kwargs)
  File "E:\Final5\luminooo\env\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "E:\Final5\luminooo\env\Lib\site-packages\django\core\management\commands\runserver.py", line 124, in inner_run
    autoreload.raise_last_exception()
  File "E:\Final5\luminooo\env\Lib\site-packages\django\utils\autoreload.py", line 86, in raise_last_exception
    raise _exception[1]
  File "E:\Final5\luminooo\env\Lib\site-packages\django\core\management\__init__.py", line 394, in execute
    autoreload.check_errors(django.setup)()
  File "E:\Final5\luminooo\env\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "E:\Final5\luminooo\env\Lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "E:\Final5\luminooo\env\Lib\site-packages\django\apps\registry.py", line 116, in populate
    app_config.import_models()
  File "E:\Final5\luminooo\env\Lib\site-packages\django\apps\config.py", line 269, in import_models
    self.models_module = import_module(models_module_name)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "E:\MTECH_hands-ON\python\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "E:\Final5\luminooo\luminooo_api\main\models.py", line 23
    class
         ^
SyntaxError: invalid syntax
E:\Final5\luminooo\luminooo_api\main\models.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 20, 2025 - 18:00:54
Django version 5.2, using settings 'luminooo_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
[20/Apr/2025 18:01:04] "GET /admin/ HTTP/1.1" 200 8950
[20/Apr/2025 18:46:11] "GET /admin/main/coursecategory/ HTTP/1.1" 200 9564
[20/Apr/2025 18:46:12] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[20/Apr/2025 18:46:12] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Apr/2025 18:46:12] "GET /static/admin/js/actions.js HTTP/1.1" 200 8076
[20/Apr/2025 18:46:12] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7887
[20/Apr/2025 18:46:12] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6878
[20/Apr/2025 18:46:12] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[20/Apr/2025 18:46:12] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 9777
[20/Apr/2025 18:46:12] "GET /static/admin/js/core.js HTTP/1.1" 200 6208
[20/Apr/2025 18:46:12] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 285314
[20/Apr/2025 18:46:12] "GET /static/admin/js/filters.js HTTP/1.1" 200 978
[20/Apr/2025 18:46:12] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 325171
[20/Apr/2025 18:46:12] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[20/Apr/2025 18:46:17] "GET /admin/main/teacher/ HTTP/1.1" 200 9508
[20/Apr/2025 18:46:17] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Apr/2025 18:46:24] "GET /admin/main/teacher/add/ HTTP/1.1" 200 15018
[20/Apr/2025 18:46:24] "GET /static/admin/css/forms.css HTTP/1.1" 200 8525
[20/Apr/2025 18:46:24] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 586
[20/Apr/2025 18:46:24] "GET /static/admin/js/calendar.js HTTP/1.1" 200 9141
[20/Apr/2025 18:46:24] "GET /static/admin/js/admin/DateTimeShortcuts.js HTTP/1.1" 200 19319
[20/Apr/2025 18:46:24] "GET /static/admin/css/widgets.css HTTP/1.1" 200 11991
[20/Apr/2025 18:46:24] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[20/Apr/2025 18:46:24] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[20/Apr/2025 18:46:24] "GET /static/admin/img/icon-calendar.svg HTTP/1.1" 200 1086
(env) PS E:\Final5\luminooo\luminooo_api>