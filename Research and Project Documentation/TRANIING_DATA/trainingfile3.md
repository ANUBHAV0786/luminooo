NOw for STEP 3  we will connect Postgresql to our django FRAMEWORK 


firt GOTO PostgreSQL then create 
        1. first create a ROLE Login/Group USER with name as "luminoo_user"
        2. now create Databse with name luminooo_db and select  luminoo_user instead of postgres in the OWNER field





https://www.youtube.com/watch?v=MH6HGawX_Fo&list=PLgnySyq8qZmox-EAyxkPYe14ZVCVSBMdK&index=105


------------------
Now we connect Django to our Postgresql DATABASE 

    FIRSTLY we have to do 

        1. OPen settings.py file 
        2. look for database section 
        3. comment the default type completely in the database section
        4. Now add the below syntax 
                    'default':{
                        'ENGINE':'django.db.backends.postgresql',
                        'NAME':'luminooo_db',   this is the name of the database that we have created t our 
                        'USER':'luminooo_user',
                        'PASSWORD':'RUNLATERALinfosys@1994',   this shows we have used an empty password
                        'HOST': 'localhost',
                        'PORT': '5432',
                    }

    NOw we also need to install postgresql client so we can conenct django to postgresql
                use  # pip install psycopg


Once we have psycopg and we have changed our database from sqllite to postgresql so now we need to migrate our changes for tht we need to use 

        # py manage.py migrate





        =============
        ===========+
        =================


        chat gpt 

        Step 1: Install PostgreSQL
Download installer:
👉 https://www.postgresql.org/download/windows/

During installation:

Set a password for the postgres superuser. (e.g., admin or something you’ll remember)

Keep the port at default: 5432

After install, open pgAdmin 4 (GUI tool), or just run psql (CLI) if you're comfortable.

🔧 Step 2: Create a Database and User
Option 1: Use pgAdmin (GUI)
Open pgAdmin

Right-click Databases > Create > Database

Name: luminooo_db

Create a new role (user):

Go to Login/Group Roles > Create > Role

Name: luminooo_user

Go to "Privileges" → Grant login & create DB

Go to "Definition" tab → set password

Option 2: Use CLI (psql)
b

psql -U postgres
sql

CREATE DATABASE luminooo_db;
CREATE USER luminooo_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE luminooo_db TO luminooo_user;

🔧 Step 3: Install PostgreSQL Adapter for Django
In your Django environment:


pip install psycopg2


Or the safer version:


pip install psycopg2-binary
🧠 Step 4: Update settings.py in Django
python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'luminooo_db',
        'USER': 'luminooo_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
🚀 Step 5: Run Migrations
bash
Copy
Edit
python manage.py migrate
If all went well, you’ll see migrations apply without errors!

