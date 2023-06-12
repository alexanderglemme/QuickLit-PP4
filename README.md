# QuickLit - Your user-to-user Marketplace for Student Literature
QuickLit is a Django-based web application that allows students to buy and sell used textbooks and other literature materials directly with each other. The application offers full CRUD functionality and uses Djangos built in user authentication to ensure secure access.

[Deployed project](https://quicklit-pp4.herokuapp.com/)

[Project repo](https://github.com/alexanderglemme/QuickLit-PP4)

# Table of Contents
- [Background, Purpose, Goals and Context](#background-purpose-goals-and-context)
    - [Background](#background)
    - [Purpose](#purpose)
    - [Goals](#goals)
    - [Relevant Context](#relevant-context)
- [Usage](#usage)
    - [Important message: Please read the Terms of Use!](#important-message-please-read-the-terms-of-use)
    - [How to post a sales ad (and how to sign up and log in)](#how-to-post-a-sales-ad-and-how-to-sign-up-and-log-in)
    - [How to read and update your sales ad](#how-to-read-and-update-your-sales-ad)
    - [How to mark your ad as SOLD, and how to Delete](#how-to-mark-your-ad-as-sold-and-how-to-delete)
    - [How to find and buy a book](#how-to-find-and-buy-a-book)
    - [How to start a study group](#how-to-start-a-study-group)
    - [How to navigate back to the home page after a 404 error](#how-to-navigate-back-to-the-home-page-after-a-404-error)
    - [How to delete your account](#how-to-delete-your-account)
- [Epics and User Stories](#epics)
- [Testing](#testing)
- [Documentation](#documentation)
- [Deployment](#deployment)
- [Dependencies](#dependencies)
    - [External Resources and CDNs](#external-resources-and-cdns)
- [Troubleshooting](#troubleshooting-common-bugs-and-fixes)
    - [Login Failure: "Invalid credentials" error](#1-login-failure-invalid-credentials-error)
    - [Broken Page Layout: Missing CSS or JS files](#2-broken-page-layout-missing-css-or-js-files)
    - [Database Integrity Error: ForeignKey constraint violation](#3-database-integrity-error-foreignkey-constraint-violation) 
- [Support and Contact](#support-and-contact)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

# Background, Purpose, Goals and Context
## Background
The educational journey is often accompanied by the need for course literature, which can be expensive and hard to find. Additionally, students can greatly benefit from collaborating with peers and engaging in study groups to enhance their learning experience. Recognizing these challenges and opportunities, QuickLit was created as a student-to-student marketplace and community platform.

## Purpose
QuickLit aims to provide a centralized platform where students can easily connect with each other to buy and sell course literature while fostering a collaborative learning environment. By bringing together buyers and sellers within a student community, QuickLit streamlines the process of acquiring textbooks and study materials at affordable prices, enabling students to save money and make their educational journey more accessible.

## Goals
### The main goals of QuickLit are:

- __Simplify the buying and selling of course literature:__ QuickLit offers a user-friendly interface where students can create sales ads for their textbooks, study guides, and other course materials. Potential buyers can easily search for specific books, browse listings, and contact sellers directly, streamlining the process of acquiring necessary materials at a reasonable price.

- __Facilitate study groups:__ QuickLit goes beyond being a simple marketplace. It provides features for students to connect and form study groups based on common interests or courses. Users can join existing groups or create new ones, enabling collaboration, knowledge sharing, and enhanced learning experiences.

- __Promote student engagement and networking:__ QuickLit encourages students to interact with one another, not only through buying and selling but also by participating in discussions, sharing ideas, and organizing study meetups. By fostering a sense of community, QuickLit aims to create an engaging platform that enhances student connections and facilitates academic growth.

## Relevant Context
The development of QuickLit was motivated by the challenges faced by students as myself when searching for affordable course literature and the lack of a dedicated online platform for fostering collaborative study groups that is directly connected to a marketplace. By combining these functionalities in a single application, QuickLit offers a holistic solution that addresses both the financial and academic aspects of a student's journey.

Through QuickLit, students can save money on textbooks, connect with peers who are studying similar subjects, and benefit from collective knowledge sharing. Whether you are a buyer in search of course materials, a seller looking to declutter your bookshelf, someone that wants to join an exciting and dynamic study group or all of the above simultaneously, QuickLit provides a platform that simplifies the process and enhances the overall student experience.

# Usage

## Important message: Please read the Terms of Use!
As you sign up to QuickLit you automatically agree that you acknowledge and accept to the Terms of Use. These terms are constantly located inside the footer of the website and are accessible throughout the entirety of the website. __See the video down below on how to access them:__
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/9b65d47e-75ba-4cb6-b33f-bad9c087e36a


## How to post a sales ad (and how to sign up and log in):
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/c6d3e95e-43c1-4561-bd3e-3f96d48a9852


## How to read and update your sales ad:
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/48456a43-6d84-4b4d-a18a-089f21a439e3


## How to mark your ad as SOLD, and how to Delete:
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/80670a36-9443-472e-a2e6-190977aa312b


## How to find and buy a book:
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/97d856f0-ced7-400d-a61d-071f44e5c91f


## How to start a study group:
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/f5d3d73d-1f59-4107-b5cc-0cd8921db73b


## How to navigate back to the home page after a 404 error:
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/8a5ad38c-7f95-4b87-9d94-65def6a23568


## How to delete your account:
https://github.com/alexanderglemme/QuickLit-PP4/assets/113175237/57e9fffa-a9fc-4c9d-9f49-32e0b5758588

# Epics
The Epics and their corresponding User Stories listed down below are the ones that have been successfully implemented. Worth noting is that these are not included in the project section of the projects repo. This is due to the lack of experience in using this feature on my part, resulting in me writing them all down on pen and paper and then manually transcribing them into this readme file. Though this approach is not reccommended, since I am the sole creator and developer behind this project, this unorthodox approach has seemed to work out okay. If however this project was bigger, and included any collaborators, a more reliable and secure method would have chosen.

## 1. Marketplace with full CRUD functionality

This section describes the CRUD (Create, Read, Update, Delete) functionality for sales ads that were implemented in the QuickLit website. It includes the following user stories:

### User Stories

1. **Create Sales Ad**: As a seller, I want to be able to create a sales ad for a textbook or course literature that I want to sell.

2. **Update Sales Ad**: As a seller, I want to be able to update the details of my sales ad such as the book title, book author, price, description and location.

3. **Delete Sales Ad**: As a seller, I want to be able to delete a sales ad once the item is sold or is no longer available.

4. **Make Sales Ads unavailable without deleting them**: As a seller, I want to preliminarily take my sales ad down until the actual transaction has taken place without having to delete the actual sales ad and all of the conversations associated with it.

4. **Search for Textbooks**: As a buyer, I want to be able to search for specific textbooks or course literature that I need for my classes.

5. **View Sales Ad Details**: As a buyer, I want to be able to view the details of a sales ad, including the book title, author, price, description and location of the seller.

6. **Contact Seller**: As a buyer, I want to be able to contact the seller directly to arrange a meet up, exchange shipping addresses or negotiate the price.

7. **Manage Sales Ads**: As a site admin, I want to be able to manage my sales ads, including creating, editing, and deleting them if necessary.

## 2. Study Group Feature

This section describes the Study Group feature on the QuickLit website. It enables users to form study groups, and engage in discussions within said Study Groups. The feature includes the following user stories:

### User Stories

1. **Start a Study Group**: As a user, I want to be able to create a study group for a specific course or subject and interact with multiple users simultaniously.

2. **Delete Study Groups**: As a user, I want to be able to delete a study group after it has expired its usefullness.

3. **Add new users to a Study Group**: As a user, I want to be able to add a new member to the study group.

4. **Post Messages and Discussions**: As a user, I want to be able to post messages and engage in discussions within a study group.

5. **Receive Notifications**: As a user, I want to be able to receive notifications about new study group messages.

# Testing
Testing is an essential part of ensuring the functionality and stability of a Django project. As of now only manual testing has been performed, even though it is recommended to also incorporate automated tests for more comprehensive coverage. Here are the tests that have been conducted so far:

1. **User Registration and Login**: Successfully registered new users and verified their ability to log in with the created credentials.

2. **404 Page Handling**: Checked that accessing invalid URLs directs users to the appropriate 404 error page.

3. **SalesAd Management**: Tested the ability to delete SalesAd entries, both as a regular user and as a superuser. Verified that new SalesAd entries can be  created, edited and deleted by users and that placeholder images appear as intended when SalesAds are marked as sold and/or lack the users uploaded image.

4. **Study Group Management**: Created Study Groups as a user and ensured the ability to edit and delete them. Verified that the chat functionality within Study Groups allows users to exchange messages successfully.

5. **Chat Functionality**: Tested the chat functionality in both user Conversations and in Study Groups by creating and exchanging messages between different test users within both Study Groups and Conversations.

6. **Account deletion**: Tested the account deletion mechanism. Effectively ensuring that all of the cascading delete functionality works as intended by deleting a registered test user that was a member in multiple Conversations and Study Groups, and had multiple active Sales Ads.

# Deployment
## To deploy QuickLit to Heroku, you can follow these steps:

1. Create a Heroku account if you haven't already done so.
2. Install the Heroku CLI if you haven't already done so.
3. Clone the QuickLit project from GitHub.
4. Create a new Heroku app from the Heroku dashboard.
5. In the Heroku app settings, add a new PostgreSQL database.
6. Set the DATABASE_URL environment variable in the Heroku app settings to the URL of the PostgreSQL database.
7. Use the Heroku CLI to push the QuickLit project to your Heroku app.
8. Run the migrations on your Heroku app using the Heroku CLI.

# Cloning the Project from GitHub
## To clone the QuickLit project from GitHub, you can follow these steps:

1. Fork the QuickLit project on GitHub.
2. Clone your forked version of the QuickLit project to your local machine.
3. Create a virtual environment for the project.
4. Install the project dependencies using pip.
5. Set up the database using Django's migrate command.
6. Start the development server using Django's runserver command.

# Dependencies
## QuickLit requires the following dependencies:

- Python 3.8+
- Django 3.1+
- PostgreSQL
- Cloudinary

## External Resources and CDNs
This project also relies on external resources and utilizes Content Delivery Networks (CDNs) for certain libraries or assets. The following external resources are used:

- Bootstrap 5: Almost all styling was done with Bootstrap 5s CSS classes and JS functionality, both of which are integrated via CDNs.

- jQuery: The project includes the jQuery library through a CDN for enhanced JavaScript functionality and DOM manipulation.

- select2 library: The select2 library is used for creating enhanced select input fields. It is included via a CDN for easy integration and access to select2 features.

It is important to note that the availability and functionality of these resources are subject to the CDN providers services and policies. Though it is generally recommended to consider alternatives such as self-hosting the necessary files or utilizing package managers and build tools to manage dependencies more effectively it can in fact be as efficient to use external resources.

To clarify that I am aware of the risks with this approach, I have listed some well known pros and cons that are worth considering:

### Why using CDNs is not recommended for prod:

__1. Dependency and version control:__ When using CDN delivery links, your project relies on external codebases. This means that you're introducing a dependency on those external services. If the CDN goes down or the link becomes invalid, it could break the project and/or disrupt its functionality. Also, you have limited control over the versions of the code delivered via the CDN, which can lead to compatibility issues or unexpected behavior if updates or changes are made. This is espacially worth noting if you're reliant on multiple CDNs and other external dependencies.

__2. Security concerns:__ By relying on external CDN links, you're essentially trusting the content provided by that particular CDN. While most reputable CDNs have extensive security measures in place, there is always a risk of compromised or malicious code being delivered through the CDN. This could potentially introduce vulnerabilities or security risks to your project and/or the end users.

__3. Performance impact:__ While CDNs are designed to improve performance by delivering content from geographically distributed servers, relying on external CDN links could to the contrary also introduce some extra latency. If the CDN experiences issues or if the users network connectivity is lacking, it can negatively impact the loading time and overall performance of your project.

### Why someone might still choose to use CDNs:

__1. Ease of implementation:__ Using a CDN delivery link is convenient and straightforward to integrate in your project. It allows you to quickly integrate third-party libraries or resources into your project without having to host the files yourself or manage their updates. This can save time and effort both during and after development. 

__2. Potential bandwidth and server load reduction:__ By leveraging CDNs, you can offload the delivery of static files to external servers, effectively reducing the bandwidth and server load on your own infrastructure. This can be particularly useful when dealing with high traffic or large files, as CDNs are optimized for efficient content delivery.

__3. Access to the latest updates:__ CDNs often update their libraries or resources automatically, though this easily can become an issue, it ensures that you have access to the latest versions without having to manually update your project. This can be beneficial in terms of bug fixes, performance improvements, and new features.

# Troubleshooting: Common Bugs and Fixes
During the development of this project, the following common bugs has appeared and have been fixed:

## 1. Login Failure: "Invalid credentials" error
Symptoms: When attempting to log in, users may receive an "Invalid credentials" error message even with correct login information.

__Potential Cause:__ This issue can occur due to incorrect authentication settings or a mismatch between the entered credentials and those stored in the database.

__Solution:__ Verify the following:

- Ensure that the authentication backend is correctly configured in the Django settings.
- Double-check the entered login credentials and confirm that they match the corresponding user records in the database.
- If using a custom authentication system, review the implementation for any potential errors or misconfigurations.

## 2. Broken Page Layout: Missing CSS or JS files
__Symptoms:__ Pages may appear with broken or unstyled layouts, and interactive elements may not function properly.

__Potential Cause:__ This issue can arise when the static files (CSS, JS) are not being served correctly or when the paths to these files are misconfigured.

__Solution:__ Consider the following steps:

- Hard reload the page __(Hard reload on: Windows: CTRL + Shift + R, Mac: CMD + Shift + R)__ to ensure that the browsers cache is clean.
- If you are hosting your static files on an external hosting service (e.g, cloudinary), make sure that it's hooked up correctly in your settings.py file.
- Check the file paths specified in the HTML templates to ensure they are correctly referencing the static files.
- Check your config variables on heroku (if you're deploying on heroku), and make sure they're correctly set up.
- Visit the hosting services website, log in, and look for potential causes as to why your static files are not being accessed in your project.
- Ensure that the Django settings properly define the static files directories and their corresponding URLs.

## 3. Database Integrity Error: ForeignKey constraint violation
__Symptoms:__ Users may encounter integrity errors when attempting to delete a related object (e.g., deleting a Study Group associated with user accounts).

__Potential Cause:__ This issue can occur due to a misconfiguration of the foreign key relationships or a failure to handle any cascading deletes properly.

__Solution:__ Consider the following steps:

- Review the database models and verify that the foreign key relationships are correctly defined.
- If using Django's built-in ORM, make use of the on_delete parameter when defining the foreign key fields to specify the desired cascading behavior (e.g., models.ForeignKey(..., on_delete=models.CASCADE)).
- Ensure that any related objects are properly handled before deleting the associated object (e.g., deleting all Study Group members before deleting a Study Group).

# Contributing
### Contributions to QuickLit are welcome! If you would like to contribute, please open a pull request on GitHub and I will review it when I have time to do so.
