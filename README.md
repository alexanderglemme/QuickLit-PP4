# QuickLit - User-to-User Marketplace for Student Literature
QuickLit is a Django-based web application that allows students to buy and sell used textbooks and other literature materials directly with each other. The application offers full CRUD functionality and user authentication to ensure secure access.

[Deployed project](https://quicklit-pp4.herokuapp.com/)
[Project repo](https://github.com/alexanderglemme/QuickLit-PP4)

# Table of Contents
- [Usage](#usage)
- [User Stories](#user-stories)
- [Testing](#testing)
- [Documentation](#documentation)
- [Deployment](#deployment)
- [Dependencies](#dependencies)
    - [External Resources and CDNs](#external-resources-and-cdns)
- [Troubleshooting](#troubleshooting)
- [Support and Contact](#support-and-contact)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

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
### Testing is an essential part of ensuring the functionality and stability of a Django project. As of now only manual testing has been performed, even though it is recommended to also incorporate automated tests for more comprehensive coverage. Here are the tests that have been conducted so far:

1. User Registration and Login: Successfully registered new users and verified their ability to log in with the created credentials.
2. 404 Page Handling: Checked that accessing invalid URLs directs users to the appropriate 404 error page.
3. SalesAd Management: Tested the ability to delete SalesAd entries, both as a regular user and as a superuser. Verified that new SalesAd entries can be  created, edited and deleted by users and that placeholder images appear as intended when SalesAds are marked as sold and/or lack the users uploaded image.
4. Study Group Management: Created Study Groups as a user and ensured the ability to edit and delete them. Verified that the chat functionality within Study Groups allows users to exchange messages successfully.
5. Chat Functionality: Tested the chat functionality within Study Groups by creating Study Groups and exchanging messages between test users.

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

It is important to note that the availability and functionality of these resources are subject to the CDN providers services and policies. Though it is generally recommended to consider alternatives such as self-hosting the necessary files or utilizing package managers and build tools to manage dependencies more effectively it can in fact be more efficient to use external resources.

To clarify that I am aware of the risks with this approach, I have listed some well known pros and cons that are worth considering:

### Why using CDNs is not recommended for prod:

1. __Dependency and version control:__ When using CDN delivery links, your project relies on external codebases. This means that you're introducing a dependency on those external services. If the CDN goes down or the link becomes invalid, it could break the project and/or disrupt its functionality. Also, you have limited control over the versions of the code delivered via the CDN, which can lead to compatibility issues or unexpected behavior if updates or changes are made. This is espacially worth noting if you're reliant on multiple CDNs and other external dependencies.

2. __Security concerns:__ By relying on external CDN links, you're essentially trusting the content provided by that particular CDN. While most reputable CDNs have extensive security measures in place, there is always a risk of compromised or malicious code being delivered through the CDN. This could potentially introduce vulnerabilities or security risks to your project and/or the end users.

3. __Performance impact:__ While CDNs are designed to improve performance by delivering content from geographically distributed servers, relying on external CDN links could to the contrary also introduce some extra latency. If the CDN experiences issues or if the users network connectivity is lacking, it can negatively impact the loading time and overall performance of your project.

### Why someone might still choose to use CDNs:

1. __Ease of implementation:__ Using a CDN delivery link is convenient and straightforward to integrate in your project. It allows you to quickly integrate third-party libraries or resources into your project without having to host the files yourself or manage their updates. This can save time and effort both during and after development. 

2. __Potential bandwidth and server load reduction:__ By leveraging CDNs, you can offload the delivery of static files to external servers, effectively reducing the bandwidth and server load on your own infrastructure. This can be particularly useful when dealing with high traffic or large files, as CDNs are optimized for efficient content delivery.

3. __Access to the latest updates:__ CDNs often update their libraries or resources automatically, though this easily can become an issue, it ensures that you have access to the latest versions without having to manually update your project. This can be beneficial in terms of bug fixes, performance improvements, and new features.

# Contributing
### Contributions to QuickLit are welcome! If you would like to contribute, please open a pull request on GitHub and I will review it when I have time to do so.
