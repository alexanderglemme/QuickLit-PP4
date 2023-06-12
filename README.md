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
- [User Stories](#user-stories)
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

# User Stories
As a student, I want to search for specific textbooks or literature materials I need for my classes.

As a student, I want to create an account and list textbooks or literature materials that I want to sell.

As a student, I want to browse listings from other students to find the best deal for the textbooks or literature materials I need.

As a student, I want to buy textbooks or literature materials from other students and leave feedback on the transaction.

As an administrator, I want to be able to manage user accounts and listings.

# Features
## Landing page:
The Landing page features a hero section and a slogan, and displays the four newest items.
![landing page]( "Title Text 1")

# Testing
Testing is an essential part of ensuring the functionality and stability of a Django project. As of now only manual testing has been performed, even though it is recommended to also incorporate automated tests for more comprehensive coverage. Here are the tests that have been conducted so far:

__1. User Registration and Login:__ Successfully registered new users and verified their ability to log in with the created credentials.

__2. 404 Page Handling:__ Checked that accessing invalid URLs directs users to the appropriate 404 error page.

__3. SalesAd Management:__ Tested the ability to delete SalesAd entries, both as a regular user and as a superuser. Verified that new SalesAd entries can be  created, edited and deleted by users and that placeholder images appear as intended when SalesAds are marked as sold and/or lack the users uploaded image.

__4. Study Group Management:__ Created Study Groups as a user and ensured the ability to edit and delete them. Verified that the chat functionality within Study Groups allows users to exchange messages successfully.

__5. Chat Functionality:__ Tested the chat functionality within Study Groups by creating Study Groups and exchanging messages between test users.

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
