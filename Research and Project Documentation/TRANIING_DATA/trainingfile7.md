https://www.youtube.com/watch?v=VDloLxSHJRY
===============================================================================================
===============================================================================================

STEP 7 
Now we will perform authentication and permission 
we will apply basic authentication in this step for our browser API.
===============================================================================================
===============================================================================================

step 7.a 
In our views.py we will import the permission package from REST framework
and add auth permission to our code 
    using permission_classes = [permissions.IsAuthenticated] 

    

===============================================================================================

step 7.b 

In our luminooo_api/urls.py add 

path ('api-auth/', include('rest_framework.urls'))


so our code look like this 

                    from django.contrib import admin
                    from django.urls import path, include  
                    urlpatterns = [
                        path('admin/', admin.site.urls),
                        path('api/', include('main.urls')), 
                        path ('api-auth/', include('rest_framework.urls')) ## this provides a login link

===============================================================================================
