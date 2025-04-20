STEP 1  wE'RE GOING TO SETUP OUR DJANGO FRAMEWORK 


    STEP 1.A 
    First we will create the virtual environment using the terminal
        So open the Folder terminal in our case it is Luminooo
        to create virtual environment we need the package virtualenv 
            to install this use # pip install virtualenv }}}}}}}}}}}}}}}}}}}]
                we will get our terminal like the step1a.image.png inside imagesfortraining folder 

        Now we will create our virtual environment 
            use # py -m venv env    }}}}}}}}}}}}}}}}}}}}}}}
                    as we type above command it shall create a env name folder by itself,  check project structure and this env shall contains --Include,--Lib,--Scripts and --pyvenv.cfg

                    we're creating venv so it wont create dependency create issue 

        Now we need to activate the virtual environment
            to activate we need to use the command written below 
                #    .\env\Scripts\activate         }}}}}}}}}}}}}}}}}}}}

            Now on activating you can find env written at start like the below example

               example::  (env) PS E:\Final5\luminooo> 

        -----------------------------------------------------------------------------------------------------------

    Step 1.B
    Second now we install dependency package of Django to create our project in django
            
                use command # pip install django    }}}}}}}}}}}}}}}}}}}}}

            Now to create project use command 

                use # django-admin startproject <project_name>

                for our case it is  # django-admin startproject luminooo_api }}}}}}}}}}}}}}}

                    we can only use django-admin once our django is installed 
                    this will create an empty project  in our folder of Luminoo

        Once our project is created we will go to our folder luminooo.api using  #cd luminooo.api

            Once inside our project we will create the APP using the command below:

                ## py manage.py startapp    }}}}}}}}}}}}}}}}}}}}}}}}}}}]
                
        once we done the steps of 1.B we will find luminooo_api folder and this folder has the 2 sub-folders and 1 file 
                    2 sub-folders -> luminooo_api and main 
                    1 file manage.py 

                    main contains modules or application [main is our main Application ]

                    luminooo_api is  a project level folder where we define settings 


        
    ------------------------------------------------------------------------------------------------------------------------------

    STEP 1.C
                Now we need to register the application(main) into the project(luminoo_api)

                    Go to luminoo_api(sub-folder of luminoo_api) and then find the settings.py file and open it .

                        now Go To--> "INSTALLED APPS" Heading and add the main as an attribute [just simply write 'main',]

                        once done we will run the commad to start the server 
                            #py manage.py runserver }}}}}}}}}}}}}}}}}}}}



    OKAY SO STEP1 COMPLETED HERE NOW CHECK THE TERMINALFILE1 FOR THE TERMINAL DATA FOR THE BETTER CLEARENCE


                 
THANKS 

    
                 