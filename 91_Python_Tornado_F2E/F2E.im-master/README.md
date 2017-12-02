## ABOUT F2E.im

F2E is a community for front-end-developer.

## How to contribute

Fork and send pull request.

## How to run f2e.im on your own machine

1. install all required modules:

    ```
    shell> pip install -r requirements.txt
    ```

2. create database and then execute sql file in dbstructure/

    ```
    shell> mysql -u YOURUSERNAME -p

    mysql> create database f2e;
    mysql> exit
    shell> cd path of f2e.sql
	       such as cd E:\8_Git\Git_Python_Code\lzpdzlzpdzPython\93_myF2E-master\dbstructure
    shell> mysql -u root -p --database=f2e < f2e.sql
	shell> mysql -u root -p --database=myf2e < myf2e.sql
    ```

3. set your mysql user/password and smtp server config in `application.py` and `lib/sendmail.py`.
4. check above, using ``python application.py`` to start server.

    ```
    shell> python application.py --port=9001 --mysql_database=f2e --mysql_host=localhost --mysql_password=YOURPASSWORD --mysql_user=YOURUSERNAME
    ```

## How to set up a production enironment

You need to know a little of supervisor and nginx, all config files are available in conf/
