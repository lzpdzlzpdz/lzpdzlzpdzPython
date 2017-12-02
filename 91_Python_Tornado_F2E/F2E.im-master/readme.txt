MYSQL下载路径：
http://ftp.ntu.edu.tw/MySQL/Downloads/MySQL-5.6/

运行服务器
cd E:\8_Git\Git_Python_Code\lzpdzlzpdzPython\91_Python_Tornado_F2E\F2E.im-master

UPDATE user SET Password=PASSWORD('password') where USER='root';

python application.py --port=8125 --mysql_database=f2e --mysql_host=localhost --mysql_password='password' --mysql_user=root

password

1.F2E 社区成长线
E:\8_Git\Git_Python_Code\lzpdzlzpdzPython\91_Python_Tornado_F2E\F2E.im-master\static\pages\timeline

2. F2E导航页
E:\8_Git\Git_Python_Code\lzpdzlzpdzPython\91_Python_Tornado_F2E\F2E.im-master\static\pages\nav

3.F2E › 提醒消息
E:\8_Git\Git_Python_Code\lzpdzlzpdzPython\91_Python_Tornado_F2E\F2E.im-master\templates\notification

4. F2E 布局
{% set navigation_bar = [ ('/', 'topic', '社区'), ('/members', 'members', '成员'), ('/hots', 'hots', '热门'), ('/nodes', 'nodes', '结点'), ('/info', 'info', '信息'), ] -%} {% set navigation_bar = [ ('/', 'topic', '社区'), ('/members', 'members', '成员'), ('/static/pages/timeline/index.html', 'timeline', '大事记'), ('/static/pages/nav/index.html', 'nav', '导航'), ] -%} {% set active_page = active_page|default('index') -%}
{% for href, id, caption in navigation_bar %} {{ caption|e }} {% endfor %}

5. 创建主题
file:///E:/8_Git/Git_Python_Code/lzpdzlzpdzPython/91_Python_Tornado_F2E/F2E.im-master/templates/topic/create.html


mysqld –defaults-file=”C:\Program Files (x86)\MySQL\MySQL Server 5.6\my-default.ini” –console –skip-grant-tables


6. 权限不够怎么办
db = mysql.connect(host = 'localhost', user = 'root', passwd = 'rootkim', db = 'F2E')
cursor = db.cursor()
But, I get an error message in the first line of code.

OperationalError: (1045, "Access denied for user 'root'@'localhost' (using password: YES)")
To remedy the situation, I did the following:

$ mysql -u root-p
Enter password: rootkim

mysql> create database F2E;
mysql> grant usage on *.* to root@localhost identified by ‘password’;
mysql> grant all privileges on F2E.* to root@localhost ;
mysql> exit
If I have granted all access to the the database for the user "root" (me), why can't I still connect in python?