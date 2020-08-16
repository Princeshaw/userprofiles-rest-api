# User Profiles Rest API using Django
## Introduction
This is a simple rest api for user registration ,login and user feeds.
<br/>
### User registration
* source : http://prince54shaw.pythonanywhere.com/api/profile/
##
### User Profile
* source: http://prince54shaw.pythonanywhere.com/api/profile/
* This will return you the list of all the users.
## 
### Authorization
* source: http://prince54shaw.pythonanywhere.com/api/login/
* this will return you a authorized token after login with you username ans password. Username should be the given email while registeration.
* this token will help you to use PUT,POST,PATCH and delete methods in profile API.
## 
### Edit and update user
* Source: http://prince54shaw.pythonanywhere.com/api/profile/<id>
* after adding the token you can apply put , post, patch and delete methods with your profile.
## 
### Add user's feed 
* source: http://prince54shaw.pythonanywhere.com/api/feed/
* This will add a status text with the authorized user.
