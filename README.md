Cloudinary Django 
====
This is an example that demonstrates storage of image files on [Claudinary](https://cloudinary.com/).

#### Key files
1. `settings.py` in the main app. Note that `cloudinary` is on the list of `INSTALLED_APPS`. Also notice that
    there is a variable that configures cloudinary.
    ```
    # Cloudinary config - You need to create a free claudinary account.
    CLOUDINARY = {
        'cloud_name': os.getenv('CLOUDINARY_NAME'),
        'api_key': os.getenv('CLOUDINARY_KEY'),
        'api_secret': os.getenv('CLOUDINARY_SECRET'),
        'secure': True
    }
    ```
2. `.env.example`. Very self explanatory examples of the Claudinary environment variables are provided. All these 
    values can be obtained from a free Claudinary account.
    
3. `models.py` in the foo app. A model is created the usual way in `Django` but Claudinary offers the `CloudinaryField` 
    which does all the magic. It works in a much similar fashion to Django's `ImageField`. The difference is that 
    instead of storing the image on the filesystem it uploads it to Claudinary. Just like the ImageField it stores the 
    name of the image on the database.
    
4. `admin.py` in the foo app. The `Foo` model is registered on the admin site.

#### Setup and running
1. Clone the repo

    `git clone git@github.com:mutaimwiti/cloudinary_app.git`
    
2. Navigate into the repo

    `cd cloudinary_app`
    
3. Create a virtual environment and activate it

    `python3 -m venv venv`
        
    `source source venv/bin/activate`
    
4. Install required packages

    `pip install -r requirements.txt`
    
5. Migrate the database

    `python manage.py migrate`
    
6. Create a superuser

    `python manage.py createsuperuser`
    
7. Set the required environment variables.
    - `cp .env.example .env` : copy environment example config.
    - Edit the variables to suit your Claudinary account. If you don't have one create it.
    - `source .env` : export the environment variables.

8. Run the application
    - `python manage.py runserver`
    - Visit using the browser on [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin).
    - When prompted enter the credentials for the superuser that was created in step 6
    
9. Creating images
    - Click on the `+ Add` link under `Foos`.
    - Choose an image file.
    - Click save to save it on Claudinary. You should get a success message.
    - Click the `Foo object (x)` link where x is the object number e.g. 1.
    - Under `currently` is a link that when opened displays the uploaded image.
    
10. What to expect on the database

    A quick check on the database will show image names that look like this:
    
    `image/upload/v1748512764/d449tpwzfgelj1tfghvbn.jpg`.
    
    These can be used to reference the images like this:
    
    `https://res.cloudinary.com/foobaz/image/upload/v1748512764/d449tpwzfgelj1tfghvbn.jpg`

#### Note
In an attempt to keep things simple the default `sqlite` database that ships with Django is used. Only Claudinary 
needs to be configured.

#### More information
For more information visit [https://cloudinary.com/documentation](https://cloudinary.com/documentation).
