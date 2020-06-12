<h1>Social Media</h1>
Milestone Project Three: In this project, I have built a data-driven web application using the technologies that I have learned throughout Data Centric Development.
<h2>The Given Brief and Requirements</h2>
Create a web application that allows users to store and easily access data
design a database schema based on Twitter and Facebook, and any other related properties and entities (e.g. views, upvotes, authors, etc).
Create the backend code and frontend form to allow users to add new data to the site.
Optionally, you may choose to add basic user registration and authentication to the site. This can be simple as adding a username field to the post creation form, without a password (for this project only, this is not expected to be secure)
<h2>UX</h2>
I aimed for a simple and modern interface with an easy to use forms for registration, sign in, add your thoughts and edit your posts. When a user looks for a social media application they want quick easy access that gets straight to the point. If the users likes the flow of the webapp and its usability they may be interested in contributing their own content to the database to make the application they enjoy using better for others to use.
<h2>User Stories</h2>
As a user I want an easy to use application that I can use on all devices. Whether using my Tablet, laptop, on desktop or mobile.
As a user I want access to see their posts and others with the correct information
As a user I want to be able to follower users whose posts I like
As a user I want to be able to contribute to the page with my own posts.
As a user I want to sign into my own account to have access to my own posts that I can edit or delete as I please.
 
<h2>Users</h2>
users of the application can use all functionality and leave with no registration or log in
users can create an account and log in / log out.
users that have created an account and are logged in. can add / edit / delete any of their posts they have contributed.
<h2>Existing Features</h2>
<h3>Create account and log in</h3>
A user is able to create and account and log in which changes the Navigation bar 
<h3>Home page</h3>
Home page gives information about the application's functionality. It shows all the latest posts, you can either view as a guest or sign in. 
Home page has a button link to create an account or a user can use the Nav bar.
log in and log out in Nav bar.
<h3>Navigation bar</h3>
The main Title on top left of Nav goes back to home page from any page.
The navbar has a login and register feature
 
<h2>Features left to implement</h2>
If I had more time to spend on this project I would like to add:
pagination is a must for any web app like this.
Image upload instead of url.
home page images would link to their page.
up voting on favourite posts
user comments on the posts so people have feedback.
delete function
A back button for Iphone users
drop down options to not sit in front of the submit button on the pop up modal.
most popular posts by views
<h2>Database</h2>
The database I have used Is MongoDB, Mongo DB is a document-oriented NoSQL database. Each database contains collections which in turn contains documents. Each document can be different with a varying number of fields. The Schema doesn't need to be defined beforehand as the fields can be created on the fly.

<h2>Technologies used</h2>
<h3>Languages</h3>
HTML5
Python 3
CSS3
JavaScript
<h3>Tools</h3>
GitPod code editor
MongoDB Atlas NoSql document oriented database.
GitHub hosting
Browserstack testing all browsers and devices
Git version control
<h3>Libraries</h3>
JQuery to simplify DOM manipulation.
Flask to redirect and render pages.
Bootstrap Simplify the structure of the website and make the website responsive easily.
Jinja displaying data from the backend
FontAwesome icons
Google Fonts font styling
<h2>Testing</h2>
Manual Testing
Home page
Text, controls and images are aligned properly
Color, shading, and gradient are consistent
Font size, style and color are consistent for each type of text
Text, images, controls, and frames do not run into the edges of the screen.
Typed text (data entry) scrolls and displays properly
Pages are readable on all resolutions.
Title link goes to the home page.
Front page
Cards are displaying correct data.
Read more buttons connected to a single
Log in and Log out
login signs that user into their account enabling that user to see their section and the option to add a post. 
log out pops the session removing the option to add posts and see their section user is flash a message 'logged out'
Register / Create and Account
warns users if that username is already taken
warns users if password is not the same after entering password in both input fields
register button submits that entry into the Flask collections
<h3>Browser Testing</h3>
All testing on the list of Browsers below.
Google Chrome (no issues found at time of testing)
Firefox (no issues found at time of testing)
Internet Explorer & Edge (no issues found at time of testing)
Opera (no issues found at time of testing)
Responsive-Design testing
Responsive testing done on Google DevTools – Device Mode and Browserstack.
<h2>Deployment</h2>
<br>App is deloyed here socialmedia-milestone3.herokuapp.com</br>
Heroku
Create a new app 
In the terminal: -log into heroku with heroku login using username and password.
initialise a git repository git init -link the GitHub repo to the app in heroku git remote add heroku 
creates a txt file with all the dependencies to run the app pip3 freeze --local > requirements.txt
This is a web app that will run on app.py echo web: python run.py >procfile .
will scale your app to one running dyno ps:scale web=1
In app.py set the app.config variables so Heroku can find them.
PORT = 8000
HOST = '0.0.0.0'
 
app = Flask(__name__)
app.secret_key = 'noelquirke900@hotmail.com'

In the terminal line entered:
git add
git commit -m "message"
git push -u heroku master pushes the project to Heroku.
In Heroku:
Go to the project > setting > config vars
IP = `0.0.0.0`
PORT =  `5000`
SECRET_KEY = noelquirke900@hotmail.com
More > restart all dynos
<h2>How to run the project locally?</h2>
To run this project these instructions are given for a code editor I am using GitPod on a windows desktop.
You will need:
MongoDB Atlas
Python 3
Git
Pip
How to get started
From Github repository Repo download.zip and extract to your chosen destination.
Using python in gitpod you need to set up a virtual environment. check to see if pip is installed with pip -h get help setting up environment Install the virtualenv package
pip install virtualenv
Create the virtual environment
virtualenv mypython
Activate the virtual environment
mypython\Scripts\activate
install all requirements needed to run this app using
pip install -r requirements.txt.

Create a file called config.py In the terminal line enter echo 'config.py' > gitignore to hide the config.py file. 
Create app.py file In app.py, set the app.config variables to the variables set in the config.py file import config

In the terminal line enter:
python -m flask run which will run on http://127.0.0.1:5000
<h3>Errors Occured</h3>
Unfortunately my deployment did not work, after discussions with members of slack and my mentor we could not overcome the following issues. 
020-06-12T13:25:42.553759+00:00 heroku[web.1]: State changed from crashed to starting
2020-06-12T13:25:46.109577+00:00 heroku[web.1]: Starting process with command `python app.py`
2020-06-12T13:25:48.071381+00:00 heroku[web.1]: Process exited with status 1
2020-06-12T13:25:48.118805+00:00 heroku[web.1]: State changed from starting to crashed
2020-06-12T13:25:48.023814+00:00 app[web.1]: Traceback (most recent call last):
2020-06-12T13:25:48.023837+00:00 app[web.1]:   File "app.py", line 1, in <module>
2020-06-12T13:25:48.023991+00:00 app[web.1]:     import models
2020-06-12T13:25:48.023992+00:00 app[web.1]:   File "/app/models.py", line 3, in <module>
2020-06-12T13:25:48.024110+00:00 app[web.1]:     from flask_login import UserMixin # noqa
2020-06-12T13:25:48.024156+00:00 app[web.1]: ModuleNotFoundError: No module named 'flask_login'

As project due date has arrived the main focus was to submit the project as is, and further research into the issue is needed. 

Once feedback received, the project will be updated. 
<h2>Code Used</h2>
code templates used for cards
index page layout theme bootstrap theme
code templates used for modals
code templates used for dropdowns
code templates for sign in and registration
<h2>Credits</h2>
Special thanks to
My Tutor and Mentor, and the Code Institute tutors for helping me throughout this project and the never ending effort made by the Slack community to answer any questions I may have. 
<h2>Media</h2>
Font Awesome for icons
Git for version control and pushing to GitHub
Each commit should be used to save each new change to keep record of what changes have been made. Throughout this project between study early morning, work through the day, study after work and into the evening I have used both git (saving locally) and pushing to github as more of a general save option. I have a greater understanding of version control than what I have used in this project.

