# Django REST API

 🚀 ![Heroku](https://pyheroku-badge.herokuapp.com/?app=nat-api&style=flat)

A REST API for my personal projects 

/docs to see available endpoints and operations on each endpoint using Swagger 

Using [Kaffeine](http://kaffeine.herokuapp.com/) ☕️ to keep my dyno awake! 

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

<details>
<summary>Note to self</summary>

To deploy: `git push heroku main`    
Perform migrations: `heroku run python manage.py makemigrations / migrate` (must migrate locally first and then push)

🚧 food: add option to upload multiple images to a post 🚧

</details>

