[Русский](https://github.com/collinearen/share-this-project/blob/main/READMEru.md)

# <p align="center">***About my project***</p>

> Good day everyone, this is my ShareIT application. briefly about it, what it is...
>
>ShareIT is a photo hosting service with the ability  to parse images from sites and add them to your account, 
>
> Giving you the opportunity to share, like and write descriptions for your pictures.
>
> This project implements an account system with user CRUD, a system of subscriptions, likes and ratings by views.
>
>
>The bottom line is that we use a button that contains a JS script
>by dragging and dropping onto bookmarks in the browser. When the user >clicks on the bookmark, the JS code is executed in the open web page.
>When a user clicks on our bookmark while visiting another web page,  
>a script opens that parses the entire html page and searches for matches >using selectors ***.jpg", .jpeg, .png, .webp***
>shows a list of all found images, and when you click on any image
>redirects to our website, passing in the get request the Title of the web 
>page from which this script was launched, the image itself, and the site   
>address (which the user can leave if desired)
>

## 
## <p align="center">***This application implements the following technical challenges..***</p>
* All necessary views have been created for ***registration***, ***login*** and ***logout***. A model for user profiles was also created, and a specific authentication backend was created to allow login using an email address. Additionally, a password reset feature has been implemented that works through an SMTP server (sending emails with a password reset link using unique identifiers that are appended to the address of the password reset page)

* Social authentication, the ability to use your existing accounts (I took <a href="https://docs.allauth.org/en/latest/socialaccount/providers/google.html">Google</a> as an example. The Python Social Auth mechanism and social authentication using the <a href="https://pypi.org/project/django-allauth/">OAuth 2.0</a> authorization protocol were used.
* Implementation of the bookmarklet itself:
    * The user drags a link from your site to the bookmarks bar of their browser. The link contains the JavaScript source code in the href attribute. This source code will be saved as a bookmark;
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
        the selectors are used to find all IMG elements whose SRC attribute ends with .jpg, .jpeg, .webp. png respectively. Using these selectors with ***document.querySelectorAll()*** function helps to find all **JPEG**, and **PNG** images on a website. The ***forEach()*** loop then iterates through the results. Small and overly large images are removed because they are not considered suitable. As a result, only those images whose dimensions exceed the dimensions specified in the **minWidth**, **minHeight**, **maxWidth**, **maxHeight** variables are taken into account.        Below is the implementation


        <img src="https://github.com/collinearen/share-this-project/blob/test_case/image-2.png" style="max-width: 500px; border-radius: 10px;">
        

* The display of user images is implemented using **thumbnails** - small images representing a large image. Thumbnails load quickly in the browser and are a good way to display images in different sizes. For this project, the <a href="https://pypi.org/project/easy-thumbnails/">easy-thumbnails</a> library was used (a utility that allows you to create thumbnails of images. It can process images in batch mode, supports all common image formats), which was ideal and allowed us to create thumbnails. For example
    <img src="https://github.com/collinearen/share-this-project/blob/test_case/image-3.png" style="max-width: 500px; border-radius: 10px;">

* There was an extended standard User model in Django Extended using the Profile model, into which we transferred the ability to upload our avatars, as well as the is_active field, which tracked the user’s activity (if the user simply created an account and did not add a single image, then he is considered inactive but if it adds an image then ***is_active*** = ***True***)
* An images table has also been created - which is linked by a foreign key to **User** (**user_id** of the photo is linked to the **User.id** of the ***User***). There are fields ***image*** - the path to this photo (photos are stored in the media folder), ***slug*** - the name of the picture taken from the site (which the user can be deleted when created, also translated from English and Russian), There is a ***total_likes*** field - in which the number of likes for a given photo is recorded, as well as a ***private*** field - which is determined at the stage of creating the photo (If the user believes that this is a photo for personal use (as a note to yourself), then it will only be visible to the user on his images page and therefore the field ***private*** = ***True***

* In this application I worked with Redis, namely with the help of Redis I implemented the following, created image.id as a key, and wrote total_views as a value (That is, when the user visited a page with an image, the following code would be executed
    ```python
    total_views = r.incr(f'image:{image.id}:views')
    ```
    as well as increasing the image rating by 1
    ```python
    r.zincrby('image_ranking', 1, image.id)
    ```


# <p align="center">All technologies, libraries that I used in this project</p>


![Static Badge](https://img.shields.io/badge/django-collinearen?logo=django&label=django&labelColor=rgb(34%2C%2076%2C%2011)&color=white)


![Static Badge](https://img.shields.io/badge/collinearen-css?style=css&logo=css3&logoColor=blue&label=css&color=white)

![Static Badge](https://img.shields.io/badge/collinearen-docker?logo=docker&logoColor=blue&label=docker&labelColor=gray&color=white)


![Static Badge](https://img.shields.io/badge/collinearen-redis?logo=adminer&label=REDIS&labelColor=red&color=white)

![Static Badge](https://img.shields.io/badge/collinearen-postgresql?logo=postgresql&label=postgresql&labelColor=white&color=white)

![Static Badge](https://img.shields.io/badge/collinearen-js?logo=javascript&logoColor=yellow&label=javascript&labelColor=white&color=white)

![Static Badge](https://img.shields.io/badge/collinearen-thumbnails?logo=thumbtack&logoColor=blue&label=thumbnails&labelColor=white&color=white)



# <p align="center">**To try to run it for yourself**</p>


# ***Installation***
[(Back to top)](#table-of-contents)

> **Note**: For longer README files, I usually add a "Back to top" buttton as shown above. It makes it easy to navigate.

### <p align="center">you need to download the project to your local computer</p>
```shell
git clone https://github.com/collinearen/share-this-project.git
```
### <p align="center">Next you need to create a virtual environment in Python and activate it</p>
```shell
python -m venv venv
```
### <p align="center">and activate her</p>

```shell
source venv/bin/activate
```
### <p align="center">Enter the following commands to upgrade pip and download all modules and libraries that were used (they are located in the ***reqi.txt*** folder)</p>
```shell
pip install --upgrade pip
```
```shell
pip install -r reqi.txt
```
### <p align="center">Create a database, assign your data in the .env file</p>

```shell
python manage.py migrate
```
### <p align="center">Starting the server</p>
```shell
python manage.py runserver_plus --cert-file cert.crt
```
