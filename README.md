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
- [UX] (https://github.com/leemolton/footy_fanspage/master/README.md#ux)
    - [Strategy] (https://github.com/leemolton/footy_fanspage/README.md#strategy)
    - [Existing Features] (https://github.com/leemolton/footy_fanspage/README.md#existing-features)
        - [Header and Footer] (https://github.com/leemolton/footy_fanspage/README.md#header-and-footer)
        - [Index] (https://github.com/leemolton/footy_fanspage/README.md#index)
        - [Dates for your Diary] (https://github.com/leemolton/footy_fanspage/README.md#dates-for-your-diary)
        - [Predictions] (https://github.com/leemolton/footy_fanspage/README.md#predictions)
        - [Checkout] (https://github.com/leemolton/footy_fanspage/README.md#checkout)
        - [Post] (https://github.com/leemolton/footy_fanspage/README.md#post)
        - [Comments] (https://github.com/leemolton/footy_fanspage/README.md#comments)
    - [Wireframes]    <Draw forms and ideas for each page on website and then take photos> (https://github.com/leemolton/footy_fanspage/README.md#wireframes)
- [Technologies, Libraries and Languages] (https://github.com/leemolton/footy_fanspage/README.md#technologies-libraries-and-languages)
    - [Python] (https://github.com/leemolton/footy_fanspage/README.md#python)
    - [Django] (https://github.com/leemolton/footy_fanspage/README.md#django)
    - [Bootstrap] (https://github.com/leemolton/footy_fanspage/README.md#bootstrap)
    - [HTML 5] (https://github.com/leemolton/footy_fanspage/README.md#html-5)
    - [CSS 3] (https://github.com/leemolton/footy_fanspage/README.md#css-3)
    - [Stripe] (https://github.com/leemolton/footy_fanspage/README.md#stripe)
- [Testing] (https://github.com/leemolton/footy_fanspage/README.md#testing)
    (Testing pages) <Create test pages> (https://github.com/leemolton/footy_fanspage/README.md#testing-pages)
    - [Manual Testing] (https://github.com/leemolton/footy_fanspage/README.md#manual-testing)
- [Heroku Deployment] (https://github.com/leemolton/footy_fanspage/README.md#heroku-deployment)
- [Credits] (https://github.com/leemolton/footy_fanspage/README.md#credits)
    - [Media] (https://github.com/leemolton/footy_fanspage/README.md#media)
    - [Resources that helped] (https://github.com/leemolton/footy_fanspage/README.md#resources-that-helped)
    - [Acknowledgements] (https://github.com/leemolton/footy_fanspage/README.md#acknowledgements)


## UX

### Strategy
<li>As a user, I would expect to enter my Predictions and enter the weekly competition.</li>
<li>As a user, I would expect to be able to see all the blog posts.</li>
<li>As a user, I'd expect to be able to comment on existing blog posts.</li>

## Existing Features

### Header and Footer
<li>The header displays the title of the website which is clickable and will take the user back to the home page.</li>
<li>There is a menu bar on the top right with navigation to the various pages of the website.</li>
<li>A Github icon displayed at the bottom of the page takes the user back to my original Github repository and
there are links to the various social media too - Facebook, Twitter and BBC Sport website.</li>

### Index
<li>The home page starts with an introductory paragraph of being a football fan and then a summary of the website 
encouraging users to have a look at the website.</li>
<li>On the right hand side there is a list of the Premier League results for the last weekend.</li>
<li>There is then an updated Premier League table for the user to be able to quickly see the League table.</li>
<li>At the bottom of the page is a link to two latest news football articles for viewers to have a read of.</li>

### Dates for your Diary
<li>The page starts with an introduction and then has a 3 monthly summary of the big games coming up. It details
whether it is a Premier League game, Champions League game or FA Cup game.</li>
<li>There are photos of footballers from the big games coming up.</li>

### Predictions
<li>There is an introduction to the Predictions page and the date of the Predictions, typically the forthcoming weekend.</li>
<li>A list of the weekend's Premier League games with boxes next to each team with numbers from 0 to 9.</li>
<li>On the right is the updated Premier League table to help users when making their predictions.</li>
<li>A submit button for the user to take them to the page to enter their credit card details to pay to enter the competition.</li>

### Checkout
<li>When the user clicks the submit button, it takes them to the checkout page. Here they have to enter their card details.</li>
<li>The user needs to enter their full name, e-mail address, card number, Security code (CVV number), expiry date and amount.</li>
<li>The user then clicks the validate credit card button to submit payment for the Predictions and enter the competition.</li>
        
### Post
<li>The Post page displays all the blog posts that have been submitted. It displays the author of the post, the date it was published on,
the number of views and the tag that writer of the blog has created.</li>
<li>Above this is a link to add a new post, this takes the user to the new post form.</li>
<li>The new post form asks the user for a title, the content of the blog post where the user can enter their blog post, 
an image if they want to add one and also a tag field where they can enter a tag.</li>
<li> The user then clicks on save to save the blog post and display it alongside all the other existing posts. </li>
<li>A Read More link is displayed underneath the blog title where users can view the post and comment on it through the comment form.</li>

#### Comments
<li>The Read More link then summarises the blog post with the title, author, date published, number of views and tag.</li>
<li>There is a link 'Get involved with your comments' to be able to comment on the blog post which will take the user to the comment form.</li>
<li>The comment form has an name and a comment box where they can leave their comments. This comment box can be extended by
dragging it down at the right-hand corner of the box. The submit button then displays the comment below the post on the previous page.</li>
        
### Wireframes 
<li>See the wireframes [here] (https://github.com/leemolton/footy_fanspage/tree/master/wireframes)

### Technologies, Libraries and Languages
## Python

- ## Django

- ## Bootstrap
 
- ## HTML 5

- ## CSS 3
 
- ## Stripe

### Testing
    (Testing pages) <Create test pages>
    
### Manual Testing
<li> </li>
<li> </li>
<li> </li>

## Heroku Deployment

## Credits

#### Media
    
#### Resources that helped
<li> </li>
<li> </li>
<li> </li>-

#### Acknowledgements
<li>The slack forum</li>
<li>My mentor     </li>