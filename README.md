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
- To register a new user the user should access the "signup" endpoint with "/user/register/" path. after accessing this path user should send username, email and password with constraints such as unique email, 8char or above password and username containing no spetial caharchters.
- After registration user should access "login" endpoint with "user/login/" path to get access token which will be used to authorize a user to create tasks, view tasks and edit tasks and their profile. since we are using jwt token, we ned to refresh it after some time using "token_refresh" endpoint with "user/refresh/" path.
-  A user can update its password, password and email after successful login by using "update_profile" with path "user/update/". a user can also delete their account by accessing "delete_user" with path "user/delete/. after users performs various tasks they can logout using "logout" with path "user/logout/".

- After a user logs in to the system they can perform various tasks starting with creating a new task by using "new_task" endpoint with path "tasks/create/" and giving task title, description, due_date and priority level. after creating a task, a user can list their tasks using "task_list" with path "task/list/". the users also filter their tasks using priority, due_date and status. they can also search tasks using their title.
- When accessing task list using "task_list" endpoint the description of the task will be shortend. a user can accesse the details of the task using "task_detail" endpoint with path "detail/<str:title>?'title_of_the_task'" to fileter task by its name.
- A user can also edit their tasks to change their status, priority level, due date and all of its fields by using "edit_task" with path "task/edit/<str:title>?'title'". when the user marks a task as completed, the system automaticaly gives completion time to the completed_at field of the task model.
- A user also can delete task using the endpoint "delete_task" with path "delete/<str:title>?'title'. 

- To manage users i used "UserSerializer" and "UpdateProfile" serializers both extending from "serializers.ModelSerializer" giveing validation methods for username, password and email. Using these serializers i wrote four views to handle user creation, deletion, login and logut functionalities. For registration i used "RegistrationView" class extending from "generics.CreateAPIView" using "UserSerializer" to validate data. For loging out functionality, i wrote "LogoutView" extending from "APiview" using "token.blacklist()" method to block the refresh token given to the user at the login process. For editing user profile i wrote "UpdateProfileView" class extending form "generics.UpdateAPIView" using "UpdateProfile" serializer to handle validation. Finaly to handle user deletion i wrote a "DeleteUserView" extending from "APIView" using "user.delete()" method to delete instance of the user model.
- A user only can edit, delete, create and see its own tasks as well as only capable of deleting and updating its own profile.

- For Task model, """finish it including the secure connections."""