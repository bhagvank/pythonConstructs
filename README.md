# pythonConstructs

  * python coding constructs
  * Django Polls App - with Mysql
  * Django Todo App - with Mysql
## Django Polls App - with Mysql

1. Ensure that mysql is installed, python3 and django for polls app - mysite folder.

  * [Python3](https://www.python.org/downloads/)

  * [Django](https://docs.djangoproject.com/en/2.0/topics/install/#installing-official-release)

  * [Mysql](https://dev.mysql.com/downloads/mysql/)

2. Configure django_development - mysql database

   
   * You can use [mysql workbench](https://dev.mysql.com/doc/refman/8.0/en/programs-client.html)
 
      or 
   
   * Command Line
```
      login to mysql by: mysql -uroot

       mysql> create database django_development;
```
3. Configure new_user  and assign rights to django_development

     
   
      * You can use [mysql workbench](https://dev.mysql.com/doc/refman/8.0/en/programs-client.html) 
  
           or 

      * Command Line 
  ```    
        login to mysql by: mysql -uroot

        mysql> create user 'newuser' identified by 'newuser';

        mysql> grant all privileges on django_development.* to 'newuser';
```
4. Ensure that you have mysqlclient package installed
```
   pip3 install mysqlclient
```   
   
### Workarounds/fixes for errors :

1. sh: mysql_config: command not found
```
     ln -s /usr/local/mysql/bin/* /usr/bin
```   
   
2. "Error loading MySQLdb module: "
   
    the number 20 can be replaced by the one relevant to the error message
```   
    sudo ln -s /usr/local/mysql/lib/libmysqlclient.20.dylib /usr/lib/libmysqlclient.20.dylib
  
    sudo ln -s /usr/local/mysql/lib /usr/local/mysql/lib/mysql
```
