# ***About my project***


> Good day everyone, this is my ShareIT application. briefly about it, what it is...
>
>ShareIT is a photo hosting service with the ability  to parse images from sites and add them to your account, 
>
> Giving you the opportunity to share, like and write descriptions for your pictures.
>
> This project implements an account system with user CRUD, a system of subscriptions, likes and ratings by views.

>The bottom line is that we use a button that contains a JS script
>by dragging and dropping onto bookmarks in the browser. When the user >clicks on the bookmark, the JS code is executed in the open web page.
>When a user clicks on our bookmark while visiting another web page,  
>a script opens that parses the entire html page and searches for matches >using selectors ***.jpg", .jpeg, .png, .webp***
>shows a list of all found images, and when you click on any image
>redirects to our website, passing in the get request the Title of the web 
>page from which this script was launched, the image itself, and the site   
>address (which the user can leave if desired)
>

## This application implements the following technical challenges..

* All necessary views have been created for ***registration***, ***login*** and ***logout***. A model for user profiles was also created, and a specific authentication backend was created to allow login using an email address. Additionally, a password reset feature has been implemented that works through an SMTP server (sending emails with a password reset link using unique identifiers that are appended to the address of the password reset page)

* Social authentication, the ability to use your existing accounts (I took <a href="https://docs.allauth.org/en/latest/socialaccount/providers/google.html">Google</a> as an example. The Python Social Auth mechanism and social authentication using the <a href="https://pypi.org/project/django-allauth/">OAuth 2.0</a> authorization protocol were used.
* Implementation of the bookmarklet itself:
    * the user drags a link from your site to the bookmarks bar of their browser. The link contains the JavaScript source code in the href attribute. This source code will be saved as a bookmark;
    * The user goes to any site, clicks on a bookmark in the bookmarks bar or favorites bar. The bookmark's JavaScript source code will be executed.
    * Retrieves the main bookmarklet container by getting the DOM element with the bookmarklet ID using
        ```javascript
        document.getElementById()
        ```
    * The bookmarklet element is used to retrieve a child element with class images. The ***querySelector()*** method allows you to retrieve DOM elements using CSS selectors. Selectors provide the ability to find DOM elements to which a set of CSS rules are applied.
    * The image container is given empty HTML, and the bookmarklet becomes visible on the page when the CSS display property is set to block.
    * Uses the #close selector to find a DOM element with ID close. A click event is attached to this element using the ***addEventListener()*** method. When users click on an element, the main bookmarklet container is hidden and its display property is set to none.
    * After loading the bookmarklet's styles and HTML code, you need to find the images on the current web page. If the images are smaller than the specified size, they are added to the bookmarklet HTML. Modify the static <a href="https://github.com/collinearen/share-this-project/blob/test_case/share/images/static/js/bookmarklet.js">bookmarklet.js</a> file to add ***bookmarklet()*** to the end of the function
    * In the code below
        ```javascript
        images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"], img[src$=".webp"]');
        ```
        the selectors are used to find all IMG elements whose SRC attribute ends with .jpg, .jpeg, .webp. png respectively. Using these selectors with ***document.querySelectorAll()*** function helps to find all **JPEG**, and **PNG** images on a website. The ***forEach()*** loop then iterates through the results. Small and overly large images are removed because they are not considered suitable. As a result, only those images whose dimensions exceed the dimensions specified in the **minWidth**, **minHeight**, **maxWidth**, **maxHeight** variables are taken into account.

        Below is the implementation
            ![Alt text](https://github.com/collinearen/share-this-project/blob/test_case/image-2.png)

    * The display of user images is implemented using **thumbnails** - small images representing a large image. Thumbnails load quickly in the browser and are a good way to display images in different sizes. For this project, the <a href="https://pypi.org/project/easy-thumbnails/">easy-thumbnails</a> library was used (a utility that allows you to create thumbnails of images. It can process images in batch mode, supports all common image formats), which was ideal and allowed us to create thumbnails.
    For example
    ![Alt text](https://github.com/collinearen/share-this-project/blob/test_case/image-3.png)


,

![Alt text](https://github.com/collinearen/share-this-project/blob/test_case/image.png)







<!-- Add badges with link to Shields IO -->
![GitHub release (latest by date including pre-releases)] 

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
: Shows the current release version.

![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
: Shows the last commit time. Good indication of the project activity.

![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
: Dynamic badge that shows the number of open issues in the project.

![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
: Similar dynamic badge, but for pull requests.

![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)
: Shows the open source license the project uses.

# Quickstart/Demo

<!-- Add a demo for your project -->

I believe that you should bring value to the reader as soon as possible. You should be able to get the user up and running with your project with minimal friction.

If you have a quickstart guide, this is where it should be.

Alternatively, you can add a demo to show what your project can do.

# Table of Contents

GitHub has a ToC feature now. It works really well, so this might not be needed. Still, if you want to add a ToC in the README, you can add it here.

I just learned that VS Code automatically updates the ToC if you change any of the headings. Pretty cool!

- [Project Title](#project-title)
- [Quickstart/Demo](#quickstartdemo)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
- [License](#license)

# Installation
[(Back to top)](#table-of-contents)

> **Note**: For longer README files, I usually add a "Back to top" buttton as shown above. It makes it easy to navigate.

This is where your installation instructions go.

You can add snippets here that your readers can copy-paste with click:

```shell
gh repo clone navendu-pottekkat/awesome-readme
```

# Usage
[(Back to top)](#table-of-contents)

Next, you have to explain how to use your project. You can create subsections under here to explain more clearly.

# Development
[(Back to top)](#table-of-contents)

You have people who want to use your project and then you have people who want contribute to your project.

This is where you provide instructions for the latter.

Add instructions on how to set up a development environment, clone, and build the project.

You can use the code snippets here as well:

```shell
command to clone your project
command to build your project
command to run your project in development mode
```


# Contribute
[(Back to top)](#table-of-contents)

You can use this section to highlight how people can contribute to your project.

You can add information on how they can open issues or how they can sponsor the project.

# License
[(Back to top)](#table-of-contents)

You can also mention what license the project uses. I usually add it like this:

[MIT license](./LICENSE)
