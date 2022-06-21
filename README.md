# Fresh Casts

<p align="center">
  <img src="" alt="Mockup of how the website looks on desktop, laptop and tablet"/>
</p>

[Link to Website](https://fresh-casts.herokuapp.com/)

[GitHub Repo](https://github.com/RickofManc/fresh-casts)


***

## About

<br />

Fresh Casts is a website built for people who enjoy listening to podcasts, and would also like to share and discover new shows and series.
Through clear and intuitive design, Fresh Casts goal is ensure the pleasure of listening, sharing and discussing podcasts is accessible to all possible user groups, no matter of age or background.

***
<br />

## Index - Table of Contents

* [User Experience R&D](#user-experience-research-and-design)
    * [Strategy](#strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Skeleton](#Skeleton)
    * [Surface](#Surface)
* [Data Model](#Data-Model) 
* [Features](#Features)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credit)

<br />

***
<br />

## User Experience Research and Design

<br />

### Problem Statement

It's difficult to find a website or app where you can share and discuss podcasts.
Listeners may feedback or rate a podcast within a listening app, however these apps generally do not allow listeners to post and discuss liked podcasts.
Podcast listenership continues to increase with over 2 million shows to choose from, and by nature humans are social, we like to converse.
There's an opportunity to help people share podcasts, making it easier to discuss and find shows that may have slipped under their radar.

<br />

### Objective

By summer 2022, I will develop and deploy a website that promotes the sharing and discussion of podcasts they are enjoying. 
All visitors will be able to listen to shared podcasts. Users who create a Fresh Casters profile will be able to comment and like shared shows, as well as posting their own favourites. The site will meet WCAG 2.1 AA standards, and will be thoroughly tested to ensure all user groups can access and enjoy content.

<br />

### Design Thinking

Following a Design Thinking process, I've identified four key personas to empathize with and define their requirements.


<details><summary><b>User Personas</b></summary>
  <img src="readme-images/fresh-casts-user-personas.png" alt="User Personas; Listener, Commenter, Blogger, Podcaster"/>
</details><br />


This phase led to User Stories being drafted complete with Acceptance Criteria and initial Tasks for the development phase. User Stories have been added to GitHub [here](https://github.com/users/RickofManc/projects/4) and are being tracked through to completion.


#### Strategic Opportunities

The chart below highlights the features roadmap assessed by importance versus viability/feasibility of development for the MVP (Minimal Viable Product). This analysis will ensure the features that will provide immediate user benefit will be development first.

<p align="center">
  <img src="readme-images/fresh-casts-features-roadmap.png" alt="Strategic Opportunities Roadmap"/>
</p>

<br />

### Scope

An agile approach of keeping the in scope features simple and aligned to the strategy for the MVP will be adopted. Below is a list of the leading features for the the Fresh Casts MVP.


#### In Scope Features
* Create an accessible website that follows convention for sites built to inform.
* Conventionally the site will have a fixed Header, Navbar and Footer.
* Main Menu accessible through a hamburger icon.
* By default, the homepage will show the latest posts in ascending order.
* A clickable link will enable Fresh Casters to find out more information on the post.
* Podcasts will be playable directly in the page browser.
* A user account will provide access to Commenting, Liking, Posting.
* Update own content - providing Fresh Casters with an option to edit their own posts.
* A 'Contact Us' page will enable Fresh Casters to get in touch with Site Admin.
* An Accessibility Statement will inform of how Fresh Casts cares about accessibility.
* The site will be responsive across differing devices, from mobile first design through to 5K screens supported.


#### Out of Scope Features - for future release
* Search and learn - Using keywords, Fresh Casters will be able to search and hone in their choices.
* Recent activity - Pulling commenting, liking, posting data from across the site into Fresh Casters profile page.
* Podcast downloading - enabling Fresh Casters to listen offline.
* Preferred app - allowing Fresh Casters to listen to a podcast in favourite listening app.
* Fresh Casters will be supported with a page dedicated to FAQ's.
* Single Sign On (SSO) - Use social apps such as Google, Facebook and Twitter to sign-in.
* Connecting Fresh Casters - Provide chat service to allow the community to interact directly.

<br />

### Structure

This website will be structured with the following design considerations.

* A Hub and Spoke structure, where the main content will be the homepage hub, and spokes are the pages to find out more information on a post. The spokes will also house the useful pages such as Sign-up, FAQ, Contact Us, About Us etc.
* Each post will be displayed in a shortened list view for the homepage with just enough information to entice the user. The post image and title will be clickable to open in a new page with full post details.
* Users wishing to add a comment or like will be asked to first create a user account as a Fresh Caster. Once a brief form has been completed and submitted, users will have immediate access to all features. 
* Having a user account will allow users to interact with the site, adding comments, likes and being able to post their own podcast review.
* All site visitors will be able to contact Fresh Casts through a contact form available from the Main Menu or Footer. 
* All pages will be available to users consistently through either the Main Menu or Footer - this should ensure users are never two clicks away from where they would like to be.


[Lucid Spark](https://lucidspark.com/) has been used to illustrate the Hub and Spoke structure for Fresh Casts website. Pages and features will be available from a single click from the Hub. The final structure for the MVP may differ slightly as development progresses, and from user feedback and testing.


<details>
    <summary><b>Site Structure</b></summary>
    <p align="center">
        <img src="readme-images/fresh-casts-site-structure.png" alt="Fresh Casts Site Structure"/>
    </p>
</details><br />


### Skeleton

Key to the UX attributes is the speed and ease for which users can learn about new podcasts, or what fellow users think about a podcast. 

The 'Hub and Spoke' structure should provide users with content from their initial landing, and allowing their intrigue to click on a post and find out more, or refine the content by choosing one of five categories located conveniently in the NavBar Menu, Footer or by clicking a category within the posts listed on the homepage.

Aesthetically pages will be clean to promote the information, and allow users to flow between differing categories and expanding posts to learn more and add a Like. Convention from popular information based sites will be adopted so users feel at home and therefore capture their engagement within the first few seconds.


#### Wireframes

As part of this phase wireframes for mobile and desktop devices have been produced using [Balsamiq](https://balsamiq.com/wireframes/) (see image below - the wireframes are located within the project [Repo](wireframes)).

The website is responsive through differing screen widths being designed for mobile first to a max-width of 767px. Tablets are responsive from 768px through to 1023px, and desktops from 1024px upward. 

<details>
    <summary><b>Wireframes</b></summary>
    <p align="center">
        <img src="readme-images/fresh-casts-mobile-wireframes.png" alt="Fresh Casts wireframe for mobile devices" />
    </p>
</details><br />


### Surface 

In consideration that accessibility is a key design criteria, the developed visual language offers contrast using a simple colour palette, readable font and clear layout. Throughout the website this language has been applied consistently to promote intuitive behaviour with the most important links and information easily recognised.


#### Colour

This palette has been carefully selected to bring high contrasting colours to improve accessibility to visually impaired users. As the primary aim of the site is to inform, Black text on a White background will be adopted throughout. The Teal based accents will be used to highlight buttons, points of reference or navigation and other key pieces of user information.

<details>
    <summary><b>Colour Palette</b></summary>
    <p align="center">
        <img src="readme-images/fresh-casts-colour-palette.png" alt="Fresh Casts Colour Palette"/>
    </p>
</details>
<br />


#### Logo

The logo has been selected from [Adobe Stock](https://stock.adobe.com/uk/contributor/208909039/2arm?load_type=author&prev_url=detail&asset_id=430392467). The design by **2arm** is being used under a  paid license with Adobe Stock. The design appealed as for it's clean design that identifies key components of podcasting; a microphone, projecting sound and listeners typically through headphones. I have applied Fresh Casts colour theme to the Vector using the free app [Photopea](https://www.photopea.com/).

<p align="center">
    <img src="readme-images/fresh-casts-b-and-g-logo_380px.png" alt="Fresh Casts Logo"/>
</p>
<br />

#### Fonts

**Roboto Flex and Roboto Condensed**

I've selected this popular [font family](https://fonts.google.com/share?selection.family=Roboto%20Condensed:ital,wght@0,400;0,700;1,400;1,700%7CRoboto%20Flex:opsz,wght@8..144,100;8..144,300;8..144,400;8..144,500;8..144,600;8..144,700) for its clean lines and legibility, being widely used on news and information based websites. It also offers a condensed style which can be used for larger text headers to offer some contrast to body text, without having to use a multiple font families.

<p align="center">
    <img src="readme-images/fresh-casts-roboto-flex-font.png" alt="Fresh Casts Font"/>
</p>
<br />

***

<br />

## Data Model

As part of the project planning phase a high-level design of the site [structure](#Structure) has been designed to understand the main entities, and the relationship between these entities set within a Hub and Spoke design.
This led to understanding the next level down through mapping out the tables, columns and attributes required for the database. The initial draft in Excel has been mapped into a data schema below using [draw.io](https://www.draw.io/index.html) to help understand how the entities and data will relate across the site.


In consideration of the a requirement for the data to be searchable, and in time understand patterns and trends in user behaviour, an Object-Relational Database using MVT architecture has been selected. I've opted for a PostgreSQL DBMS (Database Management System) as it can support the aforementioned requirements, PostgreSQL can also support multiple programming languages and libraries that which will be used to build the Fresh Casts application.

The diagram below shows the entity relationships between a blog post and their 'comments'. The Post Model is used by the Comment Model to ensure the right blog post is being commented on. The diagram also highlights that one blog post can have many comments. 

The key component in this relationship is the user. I have used the default Django User Model for ease, and whilst this is not declared in the models.py file, I have included within the diagram for clarity. 

Equally one user can add many likes throughout the site, however this functionality is built within the Post Model itself so has not been declared within this class level diagram. 

There are five categories created within the Django Admin panel. These are displayed to the user as a dropdown field choice when adding a blog post.

The diagram highlights the following relationships:
* One blog post can have one author (User)
* One blog post can have one category
* One blog post can have many comments
* One blog post can have many likes 
* One user can add one log post like
* One user can add many comments to one blog post

 
<p align="center">
    <img src="readme-images/fresh-casts-data-schema.png" alt="Data schema for Fresh Casts"/>
</p>
<br />



### Data Security

explaining the security features considered
gitignore file
secret key use for config variables
Securing data using CSRF toekn

The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their browser. A related type of attack, ‘login CSRF’, where an attacking site tricks a user’s browser into logging into a site with someone else’s credentials, is also covered.

The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC 7231#section-4.2.1) are side effect free. Requests via ‘unsafe’ methods, such as POST, PUT, and DELETE, can then be protected by following the steps below.


### Meta data

Meta data is included within the HTML head element to increase the traffic to the website. Additionally, site pages are titled appropriately as another method of informing users of their location.


***

<br />

## Technologies


### Languages

* HTML5
* CSS3
* Python
* Jquery
* Javascript

### Frameworks & Libraries

* [Django 3.2] LTS (Long Term Support) version of Django used as more preferable over the newest beta Django 4.
Gunicorn was used as the Web Server to run Django on Heroku
* [Cloudinary] was used to store the images used by the application
Django was used as the framework to support rapid and secure development of the application
Bootstrap5 was used to build responsive web pages
* Summernote provides WYSIWYG editing to adding and updating the blog post form.

* dj_database_url library used to allow database urls to connect to the postgres db
* psycopg2 database adapter used to support the connection to the postgres db
Django allauth used for account registration and authentication
Django crispy forms used to simplify form rendering


### Software & Web Applications

* [Balsamiq](https://balsamiq.com/) - Used to build wireframes in the Skelton phase.
* [Lucid Spark](https://lucidspark.com/) - Used for the high-level site structure.
* [draw.io](https://www.draw.io/index.html) - Used to build the data schema.
* PPP - Heroku, Django, Bootstrap, PPP This website was coded primarily using Python3, HTML5, CCS3 with [GitPod](https://gitpod.io/) used for the IDE and [GitHub](https://github.com/) as a hosting repository.
Git: was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
GitHub: is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.

* [Wave](https://wave.webaim.org/) - Accessibility Testing to ensure content is readable for all users.
* [HTML Validator](https://validator.w3.org/) - For validating HMTL code.
* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator) - For validating CSS code.
* [PEP8 Validator](http://pep8online.com/)  - For validating Python / Django code.
* [Code Beautify](https://codebeautify.org/) - For validating the layout of code.
* [IE NetREnderer](https://netrenderer.com/index.php) - For browser testing on Microsoft IE versions 7-10.
* [LambdaTest](https://www.lambdatest.com/) - For cross browser testing including, macOS Safari and Opera.


***

<br />

## Features


### Current Features


<p align="center">
    <img src="" alt=""/>
</p


### Future Features



***

<br />

## Testing 


### Automatic Testing


### Manual Testing 


### **Code** 
The code on each file has been assessed using the appropriate validation service; W3C Markup for HTML, W3C for CSS, and PEP8 Online for Python / Django.

Below are the summarised results from these tests:




### **Browser**




### **Device**




### **Accessibility**




### **Performance** 

                   


### **Bugs**




***

<br />

## Deployment

This project was deployed using the steps below with version releasing active. Please do not make any changes to files within this repository as any changes pushed to the main branch will be automatically reflected on the live website. Instead, please follow the steps below which guide you to forking the website where changes can be made without impact to the live website. Thanks!


### Fork and Deploy with GitHub

<details>
    <summary></summary>

To fork this website to either propose changes or to use as an idea for another website, follow these steps:
1. If you haven't yet, you should first set up Git. Don't forget to set up authentication to GitHub.com from Git as well
1. Navigate to the [Fresh Casts](https://github.com/RickofManc/fresh-casts).
1. Click the 'Fork' button on the upper right part of the page. It's in between 'Watch' and 'Star'
1. You will now have a fork of the VV Pizzas repository added to your GitHub profile. Navigate to your own profile and find the forked repository to add the required files.
1. Above the list of forked files click the 'Code' button
1. A drop-down menu will appear providing a choice of cloning options. Select the one which is applicable to your setup
Further details on completing the last step can be found on GitHub's [Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) page

To deploy from GitHub, follow these steps:
1. Log into your GitHub repository, create a GitHub account if necessary
1. Click 'Settings' in the main Repository menu
1. Click 'Pages' from the left-hand side navigation menu
1. Within the Source section, click the "Branch" button and change from 'None' to 'Main'
1. The page should automatically refresh with a url displayed
1. Test the link by clicking on the url
</details>

### Deploy with Heroku

<details>
    <summary></summary>

1. Log in to Heroku at https://heroku.com - create an account if needed.
1. From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
1. On the Create New App page, enter a unique name for the application and select region. Then click Create app.
1. On the Application Configuration page for the new app, click on the Resources tab.
1. In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list - click the "Submit Order Form" button on the pop-up dialog.
1. Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up.
1. Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
1. Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
1. The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

        DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

        SECRET_KEY = os.environ.get('SECRET_KEY')

1. In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate
1. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt
1. Commit and push any local changes to GitHub.
1. In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

Connect GitHub Repo to Heroku App

1. Navigate to Application Configuration page for the application on Heroku and click on the Deploy tab.
1. Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter and search for the required repository, then click on Connect to link them up..
1. Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - I chose the latter for the initial deployment to watch the build and then opted for Automatic Deployment.
1. The application can be run from the Application Configuration page by clicking on the Open App button.
1. Each time you push code from your GitHub Repo it will be automatically reflected in your Heroku App.

The url for this website can be found here https://freshcasts.herokuapp.com/
</details>


### Pre Production Deployment

<details>
    <summary></summary>

When you are ready to move to production, the following steps must be taken to ensure your site works correctly and is secure.

In GitPod:
1. Set DEBUG flag to False in settings.py
1. Check the following line exists in settings.py to enable Summernote to work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
1. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt
1. Commit and push code to GitHub
In the Heroku App:
1. Settings > Config Vars : Delete environment variable : DISABLE_COLLECTSTATIC
1. Deploy : Click on deploy branch
</details>
    

***

<br />

## Credit


### Acknowledgements

* Mentor Brian Macharia for continuing to guide and feedback throughout the projects lifecycle, especially on how to improve UX and my code.


### Code

Support with how to develop ideas into code also came from various online resources:

* In general the coding and testing has relied on the Code Institutes walkthrough projects "Hello Django" and "I Think Therefore I Blog" as part of their Full Stack Frameworks module.
* [W3schools](https://www.w3schools.com/) as a source of 'How to...' information throughout the build primarily on Django.
* [Django Project Docs](https://docs.djangoproject.com/en/4.0/ref/models/fields/) were referenced many times, especially in how to reference fields correctly across differing py files.
* [Codemy](https://codemy.com/) provided insight on blog building in Django.
* [GeekforGeeks](https://www.geeksforgeeks.org/urlfield-django-models) for using dynamic URL fields in html tags.
* [Code Grepper](https://www.codegrepper.com/code-examples/whatever/bootstrap+card+with+image+on+left+and+text+on+right) guided me on how to align the post image to the left of text for the homepage list view.
* [Jordan Raychev at Medium](https://medium.com/geekculture/django-tutorial-building-a-portfolio-application-contact-application-ac128d7b7b89) who provided an article on building a Contact app.
* [Wolterskluwer](https://www.wolterskluwer.com/en/solutions/kluwerlawinternational/user-agreement) for information on Blog User Agreements.
* [John Harbison](http://johnharbison.net/make-a-form-a-cancel-button) provided guidance on creating a Cancel Button as an input tag within a Form.
* [Stack Overflow](https://stackoverflow.com/questions/10615872/bootstrap-align-input-with-button) how to align an Input tag as a button using Bootstrap.





