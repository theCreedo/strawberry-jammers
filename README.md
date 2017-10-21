# strawberry-jammers
The goal is to create a web app people can use to build a list of songs for people to use to worship.


## Getting Started
It is highly recommended to use a virtualenv to manage dependencies.
1. Create a PostgreSQL database named `strawberry-jam`
2. Run `pip install -r requirements.txt`
3. Create a `.env` file with your configuration like the following:
```
    LOG_LEVEL=debug
	SERVICE_NAME=strawberry-jam
	DEBUG=True
	DATABASE_URL='postgresql://theCreedo@127.0.0.1:5432/strawberry-jam' 
	NONCE_SECRET='y0urS3cr3tH3r3'
	HASHIDS_SALT='ur salt here'
	SECRET_KEY='a0th3rS3cr3tH3r3'
	BASE_URL='http://localhost:5000'
	GENERAL_INFO_EMAIL='hownl96@utexas.edu'
	CDN_URL=''
	REDISTOGO_URL='127.0.0.1:6379'
```
4. Making sure PostgreSQL is running, set up the tables by running `python manage.py db upgrade`
5. Run the server by running `python manage.py runserver`
