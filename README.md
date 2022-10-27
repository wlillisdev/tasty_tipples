# Tasty Tipples

- You can see the live website [here](https://hikinghub.herokuapp.com/)..

![Home page Hiking Hub](static/readme/new_responsive.png)

This website is designed for Hiking Hub. Their aim is to become the go to blog for everything to do with hiking in Ireland.

# Aim of Website

The goal of this website is to create a hiking community blog. To provide a platform so users can share their hiking adventures. This blog will enable users to upload their own unique hike reviews, and share with others their experience they had on a particular hike or trail. So other users can discover hidden gems of hikes and trails all over Ireland.

# Target Audience

 Hiking is an activity enjoyed by all age groups. But is it recommended that users be aware of the risks involved with hiking. And not attempt difficult trails if you do not have a guide, relevant experience, proper equipment, clothing and supplies. Primally the website will be aimed at hiking enthusiasts 25+ based in Ireland  

# User Experience (UX)

### User Stories
- First Time Visitors Aims:
  - As a first-time visitor, I want to quickly and easily understand what this website is about and what it can do for me.
  - As a first-time visitor, I want to be able to easily navigate around the site to find the content I'm looking for.
  - As a first-time visitor, I want to be able to register and create an account to get full access to the blog.
  - As a first-time visitor, I want to quickly view a summary of blog posts on one page.
  - As a first-time visitor, I want to click on a blog post and view the post in detail.
  - As a first-time visitor, I want to be able to see comments and the amount of likes on a blog post.

- Returning Visitors Aims (logged in):
  - As a returning visitor, I would like to be able to add a blog post of my hike.
  - As a returning visitor, I would like to be able to update the content on my blog post.
  - As a returning visitor, I would like to be able to delete my blog post.
  - As a returning visitor, I would like to be able to comment and like and unlike a blog post.
  - As a returning visitor, I would like to be able to quickly log in and log out of my account.
  - As a returning visitor, I would like to find links to their social media channels and follow them.

- Admin super user Aims:
  - As a super user, I want to be able create a blog post from admin panel.
  - As a super user, I want to be able create a draft post so admin can finish at a later date.
  - As a super user, I want to be able filter and search through data quickly and easily.
  - As a super user, I want to be able to approve or Delete users blog posts.
  - As a super user, I want to be able to approve or delete comments.

# Agile Approach to Project Devlopment

An agile approach was taken in the development of this project. The project will be dissected into smaller parts and an iterative approach to project management and development will be used to achieve faster development of the project and optimise time usage.

- MoSoCoW Method:
  - I will also aim to integrate the MoSoCoW Method in to this project. Which is a four-step approach to prioritizing which project requirements need to be carried out first in order to achieve project goals and criteria of user stories. Custom labels will be created in github and allocated to each requirement so they can be easily filtered and identified.

  <img src="static/readme/moscow.png" alt="MoSoCoW Method" width="350"/>

- User Stories
  - The whole project was broken down in 18 individual user stories, each user story was a self-contained development mini project that helped reach the overall goal of the website. They were enterd into github as github issues.
  - [View List of 18 User Stories] (https://github.com/wlillisdev/hiking-hub/issues)
  - Specific acceptance criteria were allocated for each user story and a list of tasks were also established. Each task would need to be completed to ensure acceptance criteria is met. See example below.
  ![Issue Example](static/readme/user_story.png)
  - The Moscow method was then applied to each user story. And tags were applied to prioritise the order of work.
  - [Example of MOSCOW tags] (static/readme/must_have.png)
  - The user’s stories were then put in to 2 iterations. Iteration 1 had 14 user stories and these were deemed essential for the initial launch of the website. Iteration 2 currently has 4 user stories that will be carried out at a later date.
  - [View Project Iterations] (https://github.com/wlillisdev/hiking-hub/milestones)
  - A Kanban board was set up in github in order to manage the various project user stories. It was divided into 3 main areas to track the progress of user stories. The 3 Columns were To Do, In Progress, Done.
  ![Kanban Board](static/readme/kanban_board.png)
  -[View Kanban Board](https://github.com/wlillisdev/hiking-hub/projects/1)
 
# Features 

 [View Homepage Featuers](https://hikinghub.herokuapp.com/)

__Favicon__
 - As hiking is the theme of the website an icon of a person hiking was used, I came across a solution on stack overflow on how to turn font awesome logo in to favicon. Click
 [here](https://gauger.io/fonticon/)
  
![favicon](static/readme/favicon_home.png)

__Navigation Bar__
 
  - The Navigation bar is located at the top of all Pages. It is simple but clean design. It includes the logo, Home page, View Posts, Login & Register. this appears to users that are not logged in.
  - If a user has logged it changes, Add Post appears and logout becomes active in the nav bar. It will also display the name of logged in user.
  - It will allow a visitor to quickly and easily get around the site as each link logically leads to the next.
  - The nav elements also change colour when hovered which adds to the user experience.
  - The nav bar is responsive and collapse’s in to hamburger menu when on smaller screens.   
  - The nav bar below shows user logged in view.
  ![Navigation Bar When logged in](static/readme/navbar.png)
  - The responsive nav bar below.
  - <img src="static/readme/navbar_hamburger.png" alt="navbar hamburger" width="200"/>
 
__Landing Page__

  - The landing page contains an eye-catching background image of a beautiful landscape with a trail by a stream and immediately catches the user’s attention.
  - The text on the screen clearly tells the user what’s the site is about and what the user needs to do next. And they are encouraged to sign up with a bold sign-up button.
  - The hero image also has a Parallax Scrolling Effect with the text.
  - The text on the home screen changes depending on if the users is logged in or not.
  - Landing page below shows the text displayed when new user visits the site and is not registered.
  - <img src="static/readme/new_hiking_home.png" alt="hero not logged out" width="675"/>
  - Landing page below shows the text displayed when user is logged in.
  - <img src="static/readme/home_logged_in.png" alt="hero not logged in" width="675"/>

__Why Join Us__

- If the users scroll down from the hero image, looking for more information. They will come across the section why join us.
- With the help of Font Awesome and some carefully crafted bullets points of text. It outlines key area of why the user should sign up to this blog.
- <img src="static/readme/why_join_us.png" alt="why join us" width="600"/>

__Footer__

  - The footer is simple and clean design it is the same on all pages of the website.
  - It contains 4 social media platforms that will also open in a new window to allow easy navigation for the user.
  - The main aim of the footer is to increase engagement with visitors. With the goal of getting the user to subscribe to the social channels in order to get updates on new blog post and encouraging users to be part of the Hiking Hub Community.

 ![Footer Bar](static/readme/new_footer.png)

__Scroll Back To Top__
  - When the user scrolls below the fold the icon appears in the botton right of the screen. When the user clicks on it, the user will be retuned to the top of the screen.And the icon will be hidden. This featuer will improve user experience.

  - <img src="static/readme/scroll.png" alt="scroll featuer" width="600"/>

__About Us__

  - About Us section is a very brief description about hiking hub to quickly give the user more information about the website and why we started up this blog.
  - It also highlights the goals of the website so the user can understand and build trust with the blog.
  - <img src="static/readme/about_us.png" alt="About Us" width="450"/>

__Post List__
  - On the top nav bar the user can click on view posts. This will bring the user to a page where all the posts are displayed. 
  -  They are displayed in a card format in 2 rows of three in desktop view. Each card has quick summary of the blog post. Which include Title, Author, Location, and quick summary of the post, date created and the number of likes.
  -  When a user is logged in an edit and a delete button will appear on cards. Only on the blog posts the logged in user has created will the buttons appear. To allow them make edits to their previous blog posts.
  -  [View Post Summary with buttons](static/images/post_edit.png)
  ![post list](static/images/post_view.png)

__Pagination__
  - When 6 posts occupy a page it automatically creates a new page, this can be accessed at the bottom of the page. You can press next or previous to navigate between pages.
  - <img src="static/readme/new_paginate.png" alt="pagination" width="400"/>

__Post Detail__
  - [View typical post detail page](https://hikinghub.herokuapp.com/cannon-sheehan-loop/)
  - When a post summary card is clicked it will bring the user to a post detail page.
  - This page gives a detailed view of the blog post, it shows featured image, summary of hike details and a review of the hike.
  - <img src="static/images/post_detail.png" alt="post detail" width="400"/>
  - Buttons for edit and delete post also appear on the blog posts created by the user to allow editing at a later date.

__Comments__
  - At the bottom of the post detail page is a comments section. It displays comments left by users accompanied with the date.
  - There is also a counter to show how many times a post was liked and how many comments were made.
  - A feature of the site is that only registered users can make a comment or like a post, all comments are moderated and must be approved before appearing on site by the admin.
  - <img src="static/images/leave_comment.png" alt="post comment" width="550"/>
  - The user will also get an alert message that there comment was submitted
  ![Comment Submitted](static/readme/alert_comment.png)

__Add Post__
  - If the user is logged in, then they can add a post. The link to adding a post is displayed on the nav bar once the user has logged in.

  - The user is taken to a form with a WYSIWYG editor called Summernote to help them format their content by adding different headings, links, images etc.

  - Once the user has submitted their post, they are taken back to the home page, all post must be approved before final publishing on the blog.
  - [View add Post Form] (static/images/add_post.png)
  - The user will also get an alert message that there post was submitted
  ![Alert Add Post](static/readme/post_submitted.png)
  
__Update Post__
  - If the user is logged in, the update post button will be active on the blog posts they have created.
  - The user will be brought to a form that is prepopulated with the original blog post details they have written.
  - And edits can be made and update clicked at the bottom of the form and this new content will be now displayed.
  - [View add Update Post Form] (static/images/update_post.png)
   - The user will also get an alert message that there post was updated
  ![Alert Update Post](static/readme/update_post_alert.png)

__Delete Post__
  - If the user decides they want to delete a blog post they have created, they can click on the delete button.
  - As safety featuer the user is brought to a new page in case, they clicked on delete button by accident. This page asks again if the user is sure they want to delete the blog post. There is also a cancel button that will return the user back to the home page if they dont want to delete the post.
  - If deleted the post will be removed from the data base and the user will be redirected to the home page.
  ![Delete Post](static/images/delete.png)

__Sign Up__
  - The user will be brought to a sign-up form if they are new to the site and would like to set up an account. Users will have to register if they want to add posts, comment or like posts.
  - <img src="static/readme/sign_up_new.png" alt="sign up" width="400"/>

__Log in and Log Out Pages__
  - Users that are returning to the blog and want to log back into their account have a simplified form that requires just a username and password.
  - <img src="static/readme/sign_in_new.png" alt="log in" width="400"/>
  - When the user has successfully logged in the users will get an alert message and their user’s name displayed on the nav bar.
  ![Logged in](static/images/signin_page_loggedin.png)
  - When the user decides to leave and log out of their account, they will be brought to a screen that asks them are they sure they want to log out.
  - <img src="static/images/logout.png" alt="log out" width="400"/>
  - The user will get an alert message if they have successfully logged out.
  ![Logged Out](static/images/signed_out.png)

__Admin Panel__
  - A superuser was created at the start of this project to manage the administration section of teh blog.
  - Only approved admin users can access this section of the site and can do so by adding /admin to the URL home page and signing in.
  - The admin has got full CRUD functionality. They can create, read update and delete blog posts. Create draft posts, Delete and approve comments. Delete and add users. And has the functionality to filter and search though information.
  - <img src="static/images/admin.png" alt="admin panel" width="600"/>

__Error Pages__
 - Custom error pages were also created for this project.
   - 403 Page Forbidden - Access Forbidden the user does not have permission to access this resource
   - 404 Page Not Found - the user requested a page that is not available
   - 500 Server Error - internal server error 
   - <img src="static/readme/404_error.png" alt="404 error" width="600"/>

# Design
 - Theme
   - The Theme of the website was to build a bright and engaging hiking blog that had an easy user interface and the users could display their posts simply and elegantly. 
   - Fonts were imported from google fonts, Roboto & Lato were chosen. These were picked as they were bold, simple and easy to read and complimented each other and the theme of the site.

 - Data Model
   - Lucid Charts was used to design and visualise the models used in this project.

   ![Data Models](static/images/models.png)
    - FK refers to Foreign Key

 - Color Palette
   - The colour palette is made up of Three main colours. Although simple they create a good contrast with each other and helps support the overall theme. The Blue was used mainly for buttons and the grey for a hover effect.

 ![Color Palette](static/images/color_pallet.png)

- Imagery
   - The images that were selected for the website were bold and bright images related to the outdoor and hiking.

- Wireframes
   - To create the initial layout and wireframe I used Balsamiq. This helped fine tune the design and layout. It also helped in calculating the amount of content and images required. (Home Page Below)

  - ![Homepage Wireframe Concept](static/readme/hiking_hub_home.png)
  - [Display Posts Wireframe Concept](static/readme/posts_page_layout.png)
  - [Post Detail Wireframe Concept](static/readme/post_detail_wireframe.png)
   
# Future Development

- User Profiles
  - The user will be able to have a user profile with some info about them and they also be able to view all their posts they have created in their profile.

- Categories 
  - As the site grows specific categories will be added, such as difficulty or based on location

- Search functionality
  - A search box could be integrated tot eh nav bar to allow users to search for trails or hikes.

- Online Shop
  - As the site grows in order to monetize it an online shop can be added. To provide essential hiking supplies for its users.  

# Web Marketing

## Socail Media


### Facebook Page
<img src="assets/readme/facebook_cover.png" alt="log out" width="450"/>

<img src="assets/readme/facebook_body.png" alt="log out" width="450"/>






## Email Marketing

# Testing

### Validator Testing 

 - HTML Validator
   - [W3C](https://validator.w3.org/) site was used to validate the **HTML** code.
   - A number of small errors were initially flagged up.
     - [Erros From Validator Hompage](static/readme/error_html.png)
     
 ### All Pages are now error free see links below:

 ![Home Page](static/readme/html_heruko_home.png)
   - [Link to Homepage Test Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhikinghub.herokuapp.com%2F)
   - [Link to About Us Test Passed](https://validator.w3.org/nu/?doc=https%3A%2F%2Fhikinghub.herokuapp.com%2Fabout%2F)
  

## CSS Validator
  - The [W3C](https://validator.w3.org/) was used to validate the **CSS** code
  - The website passed with no errors

  ![CSS Pass](static/readme/css_pass_heruko.png)

  ## Python
  - Python files such as views.py, models.py ect. were run through  [Pep 8 ](http://pep8online.com/)validator and no errors found.
  - [some erros found during testing](static/readme/erros_views_py.png)
  - The Following python files passed testing with pep 8 
  ![Views.py](static/readme/pass_views_py.png)
  - [view passed urls.py](static/readme/urls.py_pass.png)
  - [view passed models.py](static/readme/models.py_pass.png)
  - [view passed forms.py](static/readme/forms.py_pass.png)
  - [view passed apps.py](static/readme/app.py_pass.png)
  - [view passed admin.py](static/readme/admin.py_pass.png)

  ## Java Script
  - [some erros found during testing](static/readme/js_error.png)
  - I found a solution on stack overflow for the  esversion: 6 error
  - [view passed js](static/readme/js_pass.png)
  

 
## Lighthouse
 - Lighthouse testing was carried out in Developer Tools in Chrome. Initially it gave a number of improvements and flagged up a number of images that needed to be reduced in size. Which was done.
 - [See Light House Before Improvements] (static/readme/lighthouse_before.png)
 - The results were also skewed as the chrome extensions on my testing device was affecting the lighthouse results. The tests were redone in incognito window and performance score increased. Results below from home page
 - Desktop Result’s
 ![Homepage](static/readme/heroku_lighthouse.png)
 - [Mobile Light House Results](static/readme/mobile_lighthouse.png)

 
## Manual Testing
  - All the site links were manually tested to see if they all worked ok and linked to the correct locations.
  - The site was further tested using feedback from mentor, family and friends who checked it on different devices they had.
  - All of the page's features were tested on Google Chrome, Microsoft Edge, Mozilla Firefox, Safari, and Opera.
  - Google Chrome's Developer Tool was used to inspect page elements during the build and helped identify and debug issues within the HTML and CSS.
  - The README.md was checked before final submission and links verified.

  ## Manual Feature Testing
  - A structured approach was taken to go through all of the sites  features to see it they worked properly. 
  
  | Feature Tested | Testing Method | Final Result |  
| --- | --- | --- |
| User Register account |- Each mandatory fields were left blank intentionally to check if error messages appeared if form submitted blank | Pass | 
| User Register account - Invalid Email Field | - An invalid email address was tested to ensure error message appeared | Pass | 
| User login to account - Blank Fields | - All fields were left blank to ensure an error message was displayed to the user | Pass |
| User login to account - wrong password | - Incorrect user password was intentionally used with wrong spelling and upper and lower case letters and numbers were tested to ensure an error message was displayed to the user | Pass |
| User logged in to account - name displayed in navbar and homepage | - Logged into account with registered user account to see if name displayed in navbar and welcome message  |  Pass |   
| Non registered user - can not add a blog post | - As a not registered user their is not option in nav bar or other pages for user to add a blog post |  Pass |
| Non registered user - can not like or comment on posts| - As a not registered user their is no option to add a blog comment to post. when the heart is clicked on it dose not activate and dose not add a like  |  Pass | 
| User Logged In - User name appears in nav & welcome message| - Logged in a register account. User name appeared in nav bar and also in welcome message on home page|  Pass |
| User Logged In - Add a blog Post in Nav Bar| - Logged in . Add a blog post option appears in the nav bar|  Pass |       
| Create a blog post -  Fields left blank | - This was tested with multiple times with one field being left blank each time. Pass criteria is that alert appears to prevent successful posting until all fields have been completed|  Pass | 
| Create a blog post -  No Featured Image | - Blog post was added with no featured image from user. A  placeholder image was added by default|  Pass |
| Create a blog post -  Unique Title | - A blog post with the same title as an existing post was created, error message displayed appeared saying unique title required |  Pass | 
| Update a blog post -  you are not the author | - If you are not the author of a blog post update button will be hidden from the user a 403 error will occur if /update typed into url |  Pass |
| Update a blog post -  you are the author | - If you are  the author of a blog post update button will be visible to the author |  Pass 
| Update a blog post -  prepopulated fields from blog post | - clicked on update button, update blog post form all the fields were populated from previous blog post |  Pass
| Update a blog post -  update fields on form | - All fields on the prepopulated form were updated and submitted and the blog post content was successfully updated |  Pass
| delete a blog post - you are not the author | - If you are not the author of a blog post the delete button will be hidden to the user and 403 error will occur if /delete is typed into url | Pass          
| delete a blog post - you are the author | - If you are the author of a blog post delete buttons will be visible to the author, on delete the post is successfully removed from website | Pass
| Alert message - sign in | Alert to confirm user has successfully signed in appears on top of screen. | Pass |  
| Alert message - sign out | Alert requests user to confirm they want to log out before logging out of site, and alert appears you have successfully signed out | Pass |  
| Alert message - Add Comment | Alert your comment was successfully added appears on top of screen | Pass |
| Alert message - Add blog post | Alert your blog post was successfully added appears on top of screen | Pass | 
| Alert message - Update blog post | Alert your blog post was successfully updated appears on top of screen | Pass |
| Admin - restricted access | - Only the admin/superuser account can log into the admin view panel. | Pass |
| Admin Panel - CRUD in the admin panel| - Admin has capability to create, update and delete blog posts, approve and delete comments | Pass |
| Error Alerts - custom error pages| - The Urls were manipulated to test 403,404, & 500 errors, all errors delivered a unique error page | Pass |



## User Sory / Issue Testing
  - All the issues previously created in git hub at the start of the project were checked to see if the acceptance criteria were met in the final project delivery of this iteration.

  | Issue | User Story | Acceptance Criteria | Result |  
| --- | --- | --- | --- |
| 1 | As a user, I can register an account so that I can gain access to the full range of features of the blog. | User can register a new account, User can have access to all features of the blog | Pass |
| 2 | As a registered user I can easily login and logout of the blog so that I can access the content i have created. | User can easily login and logout of the site | Pass |
| 3 | As an Admin I can **view, create, edit, update and delete all blog posts ** so that the Admin can easily moderate and control the website's content. | Admin can delete posts, Admin can edit posts, Admin can filter posts, Admin can search posts | Pass |
| 4 | As an admin I can create draft posts so that I can finish writing and editing blog posts later | Admin can create a draft blog post in admin panel | Pass |   
| 5 | As a user I can view a list of trails blog posts so that I can see easily move through the list of trails and pick one I want to read | Trails appear in the paginated list | Pass |   
| 6 | As a user I can see the location of the trail on google maps so that ** i can find out the exact location of the trail to visit there** | User can add click on Google Maps and get directions to the location of the trail. | not included | 
| 7 | As a user I can create a blog post about a trail I have done so that other users can view them | User can create a detailed blog post about a trail they have walked so other users can review and comment on it. User has to be registered in order to create a blog post | Pass | 
| 8 | As a user I can delete blog posts I have created so that I can remove any unwanted trail posts I have made | User can delete blog posts they have created from the website. User can only delete their own content linked to their registered account. | Pass |
| 9 | As a user I can edit my trail blog post so that I can update or make changes to my post | User can make edits and updates to a previously published blog post, User can only their own content | Pass |  
| 10 | As a user I can I can click on a blog post so that I can read the full detailed blog post | User can click on the paginated blog post list and read the full detailed blog post | Pass |
| 11 | As a user I can comment on trial posts so that I can give my feedback & opinion to other users |  User can make a comment on the blog post. User only can only make a comment if they are a registered user. | Pass |
| 12 | As a user or admin I can read comments on a post so that I can read other user's feedback and opinions | Admin can read comments on a blog post. User can read comments on a blog post | Pass |
| 13 | As a user I can view the number of likes on a blog post so that I can see which is the most popular hiking trail |  user can view the total number of likes given to an individual blog post | Pass |
| 14 | As an admin I can **approve or disapprove comments made ** so that I can filter out inappropriate comments |  admin can moderate and quickly filter comments and easily approve and delete comments in the admin panel of the blog | Pass |
| 15 | As a user I can understand the website's purpose quickly so that I know if it’s what I'm looking for |   User can quickly understand website's purpose and what to do next from the homepage of the website | Pass |
| 16 | As a user I can register an account with a social network so that **I can quickly register my account ** |   User can register an account using their Google/Facebook account info | not included |
| 17 | As a user I can get links to important information related to hiking so that so I can get important information related to the hill walking & safety |   user can access important information in relation to hillwalking | not included |
| 18 | As a user I can buy hiking equipment from the website so that ** I can be prepared for my next hike based on user's comments & recommendations** |   user can buy hiking related equipment and clothing from the website | not included |



  
# Fixed Bugs

  - After running the site through HTML checker, a number of small bugs were identified. Each error was identified and an appropriate solution applied, i went through all pages and fixed any errors. It was good lesson and practice in finding problems with code and fixing them.
  - After Running all the pages through lighthouse, it identified issues with a number of images due to size. Lighthouse suggested to change some larger images which was done.
  - After running all python code through pep 8 validator a number of errors were identified and fixed. 
  - When creating the add post form I didn’t want the slug to appear on the form but when removed  it broke the form. I research this problem and found a solution on stack overflow which fixed this problem. [Slugify](https://learndjango.com/tutorials/django-slug-tutorial)
  - On the display posts page unless the images were sized correctly at upload the post cards were out of alignment [Card Alignment issue] (static/readme/card_size_issue.png) and did not look great, I found a solution on how to size the images all the same on stack overflow [Cards images all the same size](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width)
  - The summer note WYSIWYG Editor on the add post form and the update posts form was not responsive and was huge, i did some research on this and found a solution on Github [Summer Note Github](https://github.com/summernote/django-summernote) I was able to customise the summer note WYSIWYG editor and get it to fit and be responsive.
  - There was a bug in the footer it wasent staying on the bottom of the page [Footer Issue](static/readme/fotter_bug.png). I found a solution on stack overflow that fixed this issue.


  # Unfixed Bugs
  - When the user deletes a blog post i can not get the alert message to appear on top of the screen.

  # Security
  - Cross-Site Request Forgery (CSRF) tokens were used on all forms.
  - Secret access keys were stored safely in env.py this was set up before the first push to Github.
  - Django allauth combined with Django’s LoginRequiredMixin and UserPassesTestMixin were used to ensure only signed in users can edit or detele post.


# Deployment

The site was deployed via Heroku.
1.  Firstly Log in to Heroku.
2.  Then, click New from the dashboard in the top right corner and from the drop-down menu select Create New App.  Create a unique app name.
3.  Next, select your region. Europe.
4.  Click on the Create App button.
5.  Go to Resources tab and add a Heroku Postgres database.
6.  The next page you will see is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars and enter the following:
    *   CLOUDINARY_URL = your cloudinary key 
    *   DATABASE_URL = the url of your heroku postgres database
    *   SECRET_KEY = a secret key for your app.
    *   PORT = 8000
    *   DISABLE_COLLECTSTATIC = 1 during development only

7.  Go to the top of the page and now choose the Deploy tab.
8.  Select Github as the deployment method.
9.  Confirm you want to connect to GitHub.
10. Search for your repository name and click the connect button.
11. Scroll to the bottom of the deploy page and select deployment type:
12. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.
13. Select the correct branch for deployment from the drop-down menu and click Deploy Branch for manual deployment.
14. Click on open app to view deployed site.

**** Ensure in Django settings, DEBUG is False & DISABLE_COLLECTSTATIC is removed from config var for final deployment, create a Procfile and save database and cloudinary urls and secret key to env.py.


 ## Version Control
  - Git was used as the version control software. Commands such as git add ., git status, git commit and git push were used to add, save, stage and push the code to the GitHub repository.

## Cloning

1. On [GitHub](www.github.com), navigate to the main page of the repository.  [Click Here for Reposititory Link](https://github.com/wlillisdev/hiking-hub)

2. Above the list of files, click Code.

3. click Use GitHub CLI, then click the copy icon.

4. Open Git Bash and change the current working directory to the location where you want the cloned directory.

5. Type git clone, and then paste the URL that was copied previously  in step 3.

6. Press Enter to create the local clone.

[git cloning steps with pictuers](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)

## Forking

- A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

1. Open GitHub
2. Find the 'Fork' button at the top right of the page
3. Once you click the button the fork will be in your repository


# Technologies Used

## Languages

  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - Markup language used to create webpages of the site. 
  - [CSS](https://en.wikipedia.org/wiki/CSS)
    - CSS is the language we use to style HTML and Bootstrap framework.
  - [Python](https://www.python.org/)
    -  It is used when creating the backend functionality in Django.

## Frameworks

  - [Django](https://www.djangoproject.com/)
    -  Python framework used to create all the backend logic
  - [Bootstrap](https://getbootstrap.com/)
    - CSS framework directed at responsive, mobile-first front-end web development.
  - [Django-allauth](https://django-allauth.readthedocs.io/en/latest/)
    - For authentication, registration, account management

## Databases

  - [SQLite](https://www.sqlite.org/index.html)
    - Database during development 
  - [PostgreSQL](https://www.postgresql.org/)
    - Database used to store all the data on deployment

## Django Packages

  - [gunicorn](https://gunicorn.org/)
    - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.
  - [psycopg2](https://pypi.org/project/psycopg2/)
    -  As an adaptor for Python and PostgreSQL databases
  - [Summernote](https://summernote.org/)
    - Simple WYSIWYG Editor 
  - [Cloudinary](https://cloudinary.com/)
    - The image hosting service used to upload images
  - [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Used to style and manage Django forms
  
## Tools
   - [Balsamiq](https://balsamiq.com/) 
     - Used to create wireframes
   - [Google Fonts](https://fonts.google.com/) 
     - Used to import fonts
   - [TinyPNG](https://tinypng.com/) 
     - Used to compress images
   - [Font Awesome](https://fontawesome.com/) 
     - Used to create the icons on site
   - [LucidCharts](https://www.lucidchart.com/) 
     - Data model design
   - [Coolors](https://coolors.co/) 
     - Used to design color pallet
   - [Heroku](https://heroku.com/) 
     - Used to host the project
   - [Google Developer Tools](https://developer.chrome.com/docs/devtools/) 
     -  used to debug the website and edit styling
   - [GitHub](https://github.com/) 
     -  GitHub is used to store the projects code 
   - [GitPod](https://www.gitpod.io/) 
     -  GitPod was the IDE used to create the site
   - [PEP8](http://pep8online.com/) 
     -  Used to validate and check Python code
   - [W3C - HTML](https://validator.w3.org/) 
     -  W3C was used to validate all the HTML code 
   - [W3C - CSS](https://jigsaw.w3.org/css-validator/) 
     -  W3C was used to validate the CSS code


## Images
  - All images were taken from [Pexels](https://www.pexels.com/)

## Content
  - Content & maps from All Trails was used to generate blog posts  [AllTrails](https://www.alltrails.com/ireland)
 
## Credits
   - Reference was made to the [Code Institute](https://codeinstitute.net/ie/) Django Codestar tutorials and modified.
   - [Corey Schafer Django Tutorial](https://www.youtube.com/watch?v=UmljXZIypDc) Very helpful with understanding all elements of setting up a django blog & for implementing user crud on blog posts.
   - [Codemy Django Blog Series](https://www.youtube.com/watch?v=B40bteAMM_M) Used to understand setting up views,templates & bootstrap.
   - [Net Ninja Django Tutorial series](https://www.youtube.com/watch?v=n-FTlQ7Djqc) recommended by other students in slack, provided a simplified explanation Djangos MVT.
   - [Parallax Scrolling Effect](https://www.w3schools.com/howto/howto_css_parallax.asp) used to create the effect on the homepage.
   - [Django Documentation ](https://docs.djangoproject.com/en/4.0/) used to trubleshoot problems and get information.
   - [Create Favicon](https://gauger.io/fonticon/) created favicon from font awsome icon found on stack overflow.
   - [GT Coding](https://www.youtube.com/watch?v=SJVCvnKM_lI) creates a icon that will scroll to top of page when clicked
   - [Django Slug Tutorial](https://learndjango.com/tutorials/django-slug-tutorial) creating slugs in django
   - [Bootstrap](https://www.youtube.com/watch?v=4sosXZsdy-s) Tutorials used to understand bootstrap.

  
## Resources
  - [Stack Overflow](https://stackoverflow.com/)
  - [W3Schools](https://www.w3schools.com/)
  - [w3docs](https://www.w3docs.com/)
  - Notes & Videos from course work from [Code Institute](https://codeinstitute.net/ie/)


## Acknowledgements
 - Special thanks to my mentor Miguel Martinez
 for his help and guidance in the development of my project. Special thanks to my tutor Kasia and our regular class meetings and members of the awesome slack community


# Conclusion
  - I would like to experiment more with Django and build some more projects. Overall, I learned a lot and enjoyed working with Django framework.
  - If I was to build this site again, I would spend more time on the wireframes and model designs.
  - If it had time, I would like to add user profiles and hike categories.   
  - I would also learn to make more commits during the project built.









































![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome wlillisdev,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
