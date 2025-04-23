https://www.youtube.com/watch?v=wuzNWPOmaZ0

curl -H "Authorization: Token ab564c7f6f2378bd23dd37df3ebcf6fbde49de4d" http://127.0.0.1:8000/api/teacher/
STEP 8

        how we can implement token authentication and how it works

=============================================================================
=============================================================================

Token authentiction Image at Step8TOKENAUTH.image.png

Step 8.a : ABOUT HOW TO SAVE  the Token

        1. We need to provide in  rest_framework.authtoken in Installed Apps in settings.py file

        2. we need to add a code of block in our settings.py
                            REST_FRAMEWORK = {
                                'DEFAULT_AUTHENTICATION_CLASSES': (
                                    'rest_framework.authentication.TokenAuthentication',
                                ),
                                

        3.THEN WE HAVE TO RUN THE MIGRATION by # py manage.py migrate

                this make our terminal look like below ::

                                    (env) PS E:\Final5\luminooo\luminooo_api> py manage.py migrate  
                                Operations to perform:
                                Apply all migrations: admin, auth, authtoken, contenttypes, main, sessions
                                Running migrations:
                                Applying authtoken.0001_initial... OK
                                Applying authtoken.0002_auto_20160226_1747... OK
                                Applying authtoken.0003_tokenproxy... OK
                                Applying authtoken.0004_alter_tokenproxy_options... OK
                                (env) PS E:\Final5\luminooo\luminooo_api> 

        4. We need to also check at our PGADMIN 
                go to database and refresh it 
                we will find a new Table under Schema with table name authtoken_token

=============================================================================
 
 Step 8.b Howw to create a token
            1. Directly from Terminal
                    py manage.py drf_create_token -r admin

                    using -r flag for recreating token for the same user
                    
                    (env) PS E:\Final5\luminooo\luminooo_api> py manage.py drf_create_token -r admin
                        Generated token ab564c7f6f2378bd23dd37df3ebcf6fbde49de4d for user admin
                        (env) PS E:\Final5\luminooo\luminooo_api> 


                    Now go to PGAdmin and refresh the authtoken_token  we will find that the token generated above has itself migrated to the Database.



========================================================================================================

step 8.c 
            Now run the server 

            Now GO TO POSTMAN tool and try to hitand we shall be getting the error like below 

                 Unauthorized: /api/teacher/
                [23/Apr/2025 07:04:12] "POST /api/teacher/ HTTP/1.1" 401 58

    NOw our main task is to pass that generated bearer token

    POSTMAN has some issue we need to check this later 

    USE CURL command to verify 
                curl -H "Authorization: Token ab564c7f6f2378bd23dd37df3ebcf6fbde49de4d" http://127.0.0.1:8000/api/teacher/