# Project Title -> Todo_List_API

## project Description
- The project Todo_List_API is a project i worked on for my "skill showing project" to join Websidia. 
- The project provides features such as registering new user, user authentication by simlejwt token, task creation, edition and deletion endpoints.

- To develope this api i used diffrent technologies, such as
        - django
        - rest_framework
        - mySQL(light)
        - rest_framework.authtoken and 
        - rest_framework_simplejwt.token_blacklist

- Getting in to the details of the project, to manage users properly i used custom user model extends "Abstractuser" class having username and email fields. and to manage(create) user and super user extending "BaseuserManager" class.
- To register a new user the user should access the "signup" endpoint with {"user/register/"} path. after accessing this path user should send username, email and password with constraints such as unique email, 8char or above password and username containing no spetial caharchters.
- After registration user should access "login" endpoint with {"user/login/"} path to get access token which will be used to authorize a user to create tasks, view tasks and edit tasks and their profile. since we are using jwt token, we ned to refresh it after some time using "token_refresh" endpoint with {"user/refresh/"} path.
-  A user can update its password, password and email after successful login by using "update_profile" with path {"user/update/"}. a user can also delete their account by accessing "delete_user" with path {"user/delete/}. after users performs various tasks they can logout using "logout" with path {"user/logout/"}.
- After a user logs in to the system they can perform various tasks starting with creating a new task by using "new_task" endpoint with path {"tasks/create/"} and giving task title, description, due_date and priority level. after creating a task, a user can list their tasks using "task_list" with path {"task/list/"}. the users also filter their tasks using priority, due_date and status. they can also search tasks using their title.
- When accessing task list using "task_list" endpoint the description of the task will be shortend. a user can accesse the details of the task using "task_detail" endpoint with path {"detail/<str:title>?'title_of_the_task'"} to fileter task by its name.
- A user can also edit their tasks to change their status, priority level, due date and all of its fields by using "edit_task" with path {"task/edit/<str:title>?'title'"}. when the user marks a task as completed, the system automaticaly gives completion time to the completed_at field of the task model.
- A user also can delete task using the endpoint "delete_task" with path {"delete/<str:title>?'title'"}. 
- To manage users i used "UserSerializer" and "UpdateProfile" serializers both extending from "serializers.ModelSerializer" giveing validation methods for username, password and email. Using these serializers i wrote four views to handle user creation, deletion, login and logut functionalities. For registration i used "RegistrationView" class extending from "generics.CreateAPIView" using "UserSerializer" to validate data. For loging out functionality, i wrote "LogoutView" extending from "APiview" using "token.blacklist()" method to block the refresh token given to the user at the login process. For editing user profile i wrote "UpdateProfileView" class extending form "generics.UpdateAPIView" using "UpdateProfile" serializer to handle validation. Finaly to handle user deletion i wrote a "DeleteUserView" extending from "APIView" using "user.delete()" method to delete instance of the user model.
- A user only can edit, delete, create and see its own tasks as well as only capable of deleting and updating its own profile.
- The reason i used title as serach parameter for edit, delete and detail views is because of the uniqeness of title in the task model.
- To manage the task model i wrote TaskListSerializer, TaskDetailSerializer, TaskCreateSerializer and TaskUpdateSerializer whish will validate the user inputs for creation and edition of tasks ensuring that the title and the due_date fields are valid for our task model. 
- To use these serializers and present them to the end points i wrote TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView and TaskDetailView all ensuring the user trying to access them is authenticated user.
- To insure the views, serializers, models and in general the program performs correctly, i wrote 26 total unit tests testing the endpoints in diffrent scenario.
- In some point of the code i used comment to explain why specific line of code is there to help undarstandig of the purpose of each line of code.

## to run it use postman not the browser. that is because i put an exception for localhost "127.0.0.1:8000/"  and test runs to not force https but most browsers inforce https. so if u want to run it in browser use incognito mode or just use postman.
## if you want to see details of endpoints in your browser, replace "DEBUG = False by DEBUG = True" in settings.py line 27.
## to access the endpoints for user, - http:/127.0.0.1:8000/user/regiseter
##                                   - http:/127.0.0.1:8000/user/login
##                                   - http:/127.0.0.1:8000/user/refresh
##                                   - http:/127.0.0.1:8000/user/logout
##                                   - http:/127.0.0.1:8000/user/delete
##                                   - http:/127.0.0.1:8000/user/update

## to access the endpoints for task, - http:/127.0.0.1:8000/tasks/list
##                                   - http:/127.0.0.1:8000/tasks/detail
##                                   - http:/127.0.0.1:8000/tasks/create
##                                   - http:/127.0.0.1:8000/tasks/edit
##                                   - http:/127.0.0.1:8000/tasks/delete



