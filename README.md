# Django REST API

 🚀 ![Heroku](https://pyheroku-badge.herokuapp.com/?app=nat-api&style=flat)

A REST API for my personal projects 

/docs to see available endpoints and operations on each endpoint using Swagger 

# Installation and Usage
Navigate to root directory of this repository and open the terminal:   

To start up the server:     
`pipenv shell`   
`pipenv install`   
`python manage.py runserver`   

# Process
1. Install necessary dependencies and apps 
2. Create model, make migrations and add to admin
3. Create serializer and views
4. Add urls for list and :id, and to root for /destinations 
5. Add auth to routes - allow read only unless auth'd
6. Setup up for deployment and deploy!


Note to self:
To deploy: `git push heroku main`   
Perform migrations: `heroku run python manage.py makemigrations / migrate`

