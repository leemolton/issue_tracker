# Django Blog Football-Project

This is my final project for the Full Stack Development course and I decided to create my own idea. I wanted to create a Football Fans Website 
designed simply for football fans who love the game.The website wants to hear from fans through a weekly Predictions competition for the football 
fixtures for the forthcoming weekend. Also, there is a Post page where fans can add their own blog or comment on existing blogs. 
There is a Diary page where forthcoming big games are highlighted so fans know what games are coming up in the next month or two.


- Heroku app link
    - <Make Heroku link work first>

- Github repository link</li>
    - https://github.com/leemolton/footy_fanspage</li>

# Table of Contents
- [UX](https://github.com/leemolton/footy_fanspage/master/README.md#ux)
    - [Strategy](https://github.com/leemolton/footy_fanspage/README.md#strategy)
    - [Existing Features](https://github.com/leemolton/footy_fanspage/README.md#existing-features)
        - [Header and Footer](https://github.com/leemolton/footy_fanspage/README.md#header-and-footer)
        - [Index](https://github.com/leemolton/footy_fanspage/README.md#index)
        - [Dates for your Diary](https://github.com/leemolton/footy_fanspage/README.md#dates-for-your-diary)
        - [Predictions](https://github.com/leemolton/footy_fanspage/README.md#predictions)
        - [Checkout](https://github.com/leemolton/footy_fanspage/README.md#checkout)
        - [Post](https://github.com/leemolton/footy_fanspage/README.md#post)
        - [Comments](https://github.com/leemolton/footy_fanspage/README.md#comments)
    - [Wireframes](https://github.com/leemolton/footy_fanspage/README.md#wireframes)
- [Technologies, Libraries and Languages](https://github.com/leemolton/footy_fanspage/README.md#technologies-libraries-and-languages)
    - [Python](https://github.com/leemolton/footy_fanspage/README.md#python)
    - [Django](https://github.com/leemolton/footy_fanspage/README.md#django)
    - [Bootstrap](https://github.com/leemolton/footy_fanspage/README.md#bootstrap)
    - [HTML 5](https://github.com/leemolton/footy_fanspage/README.md#html-5)
    - [CSS 3](https://github.com/leemolton/footy_fanspage/README.md#css-3)
    - [Stripe](https://github.com/leemolton/footy_fanspage/README.md#stripe)
- [Testing](https://github.com/leemolton/footy_fanspage/README.md#testing)
    - [Automated tests](https://github.com/leemolton/footy_fanspage/README.md#automated-tests)
    - [Manual Testing](https://github.com/leemolton/footy_fanspage/README.md#manual-testing)
- [Heroku Deployment](https://github.com/leemolton/footy_fanspage/README.md#heroku-deployment)
- [Credits](https://github.com/leemolton/footy_fanspage/README.md#credits)
    - [Media](https://github.com/leemolton/footy_fanspage/README.md#media)
    - [Resources that helped](https://github.com/leemolton/footy_fanspage/README.md#resources-that-helped)
    - [Acknowledgements](https://github.com/leemolton/footy_fanspage/README.md#acknowledgements)


## UX

### Strategy
As a user, I would expect to enter my Predictions and enter the weekly competition.
As a user, I would expect to be able to see all the blog posts.
As a user, I'd expect to be able to comment on existing blog posts.

## Existing Features

### Header and Footer
The header displays the title of the website which is clickable and will take
the user back to the home page.
There is a menu bar on the top right with navigation to the various pages of 
the website.
A Github icon displayed at the bottom of the page takes the user back to my 
original Github repository and there are links to the various social media too 
- Facebook, Twitter and BBC Sport website.

### Index
The home page starts with an introductory paragraph of being a football fan 
and then a summary of the website 
encouraging users to have a look at the website.
On the right hand side there is a list of the Premier League results for the 
last weekend.
There is then an updated Premier League table for the user to be able to 
quickly see the League table.
At the bottom of the page is a link to two latest news football articles for
viewers to have a read of.

### Dates for your Diary
The page starts with an introduction and then has a 3 monthly summary of the 
big games coming up. It details
whether it is a Premier League game, Champions League game or FA Cup game.
There are photos of footballers from the big games coming up.

### Predictions
There is an introduction to the Predictions page and the date of the 
Predictions, typically the forthcoming weekend.
A list of the weekend's Premier League games with boxes next to each team with
numbers from 0 to 9.
On the right is the updated Premier League table to help users when making
their predictions.
A submit button for the user to take them to the page to enter their credit 
card details to pay to enter the competition.

### Checkout
When the user clicks the submit button, it takes them to the checkout page. 
Here they have to enter their card details.
The user needs to enter their full name, e-mail address, card number, 
Security code (CVV number), expiry date and amount.
The user then clicks the validate credit card button to submit payment for the
Predictions and enter the competition.
        
### Post
The Post page displays all the blog posts that have been submitted. 
It displays the author of the post, the date it was published on, the number of 
views and the tag that writer of the blog has created.
Above this is a link to add a new post, this takes the user to the new post 
form.
The new post form asks the user for a title, the content of the blog post 
where the user can enter their blog post, an image if they want to add one 
and also a tag field where they can enter a tag.
The user then clicks on save to save the blog post and display it alongside all
the other existing posts. A Read More link is displayed underneath the blog 
title where users can view the post and comment on it through the comment form.

#### Comments
The Read More link then summarises the blog post with the title, author, 
date published, number of views and tag.
There is a link 'Get involved with your comments' to be able to comment on the 
blog post which will take the user to the comment form.
The comment form has an name and a comment box where they can leave their 
comments. This comment box can be extended by dragging it down at the right-hand
corner of the box. The submit button then displays the comment below the post
on the previous page.
        
### Wireframes 
See the wireframes at (https://github.com/leemolton/footy_fanspage/tree/master/wireframes)

### Technologies, Libraries and Languages
## Python

- ## Django
Django has been used to load the menu pages from the menu bar by creating 
urls in the base.html page which link to the views created.

- ## Bootstrap
Bootstrap has been used for the type of menu bar and also to style the 
whole project.
 
- ## HTML 5
HTML has been used as the framework for the base.html and other html pages.

- ## CSS 3
CSS has been used to style the website from the background colour to images 
used on the front cover and diary page.
 
- ## Stripe
Stripe has been used for the checkout function of the Predictions page for the 
user to enter their credit card to have a go at the Predictions competition.

## Testing
    
- ### Responsive testing 
    
### Manual Testing

Navigation
The pages have been tested and all the links to the pages to ensure that they work
properly and take the user to the right place. The navigation bar is at the 
top of every page. All of the navigation has been tested on smaller screen 
devices too.

Predictions and checkout page
I tested the input of the Predictions and then submitted it using the submit 
button. Users can predict the scores of 10 Premier League games by clicking 
into the drop-down boxes and selecting a number from 0 to 9 for each team. 
On the checkout page I entered a test credit card number
and CVV security code to see the checkout work. 
The amount for the predictions entry is £1.
    
Post page
I tested the post page and displayed the blog posts that have been created 
so far. The page lists all the blog posts and lets the user open it up
and add a comment to it using the comment form.
    
Comment form
I added a comment to the blog post and then seen the comment listed below
the post.

## Heroku Deployment

#### Running the server
python3 manage.py runserver $IP:$C9_PORT
    
#### Resources that helped
Searching daily, weekly and monthly on the Stack Overflow website(https://stackoverflow.com)

#### Acknowledgements
The slack forum
My mentor