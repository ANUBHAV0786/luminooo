STEP 2 : Here now we will setup our ADMIN PANEL



BUT beforee jumping on STEP 2

when we installed django it comes with default models, database , tables so we need to migrate 

to migrate we need to use command 
                # py manage.py migrate }}}}}}}}}}}}}}}}}}}

                and our terminal generate the result like 

                            System check identified no issues (0 silenced).

                            You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.

                            Run 'python manage.py migrate' to apply them.

                            (env) PS E:\Final5\luminooo\luminooo_api> py manage.py migrate
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


------------------------------------------------------------------------------------------------------------------------------------
| STEP 2 |

    See django comes with the group and user model and if we use superuser it will create a USER which have all the authority.

    To create superuser use command :
                                        # py manage.py createsuperuser }}]}}}

                            Once we enter above command it will prompt us to enter username , email, password 

                            Use Username : admin  ( all small)

                            email address : sharmaearth4@gmail.com (changed)

                            Password : RUNLATERALinfosys@1994 (changed for security this is the hint)

                            once we done this we need to run the server again 
                            and then in our address add "/admin" which will open the Admin login page by itself, It will give you GUI to work with ADMIN 
                            this the feature provided by the django 

                    NOTE**** : We need to create superuser again because we're going to use different database
                                see jango provide sqlite3 but we're going to use 