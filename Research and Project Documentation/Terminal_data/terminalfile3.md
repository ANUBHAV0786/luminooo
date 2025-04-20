(env) PS E:\Final5\luminooo> pip list
Package  Version
-------- -------
asgiref  3.8.1
Django   5.2
pip      24.2
sqlparse 0.5.3
tzdata   2025.2

---------------------------------============================================
there ia not more terminal command as there were errors and when the errors were resolved using different wways so the terminal is not required we need to use our mind to get it 

===============
======================================================
PS E:\Final5\luminooo> .\env\Scripts\activate 
(env) PS E:\Final5\luminooo> cd .\luminooo_api\
Package           Version
----------------- -------
asgiref           3.8.1
Django            5.2
pip               24.2
psycopg           3.2.6    --------------------this is the new that we have installed 
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
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(env) PS E:\Final5\luminooo\luminooo_api> 