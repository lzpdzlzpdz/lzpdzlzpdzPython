MYSQL下载路径：
http://ftp.ntu.edu.tw/MySQL/Downloads/MySQL-5.6/

运行服务器
python application.py --port=9001 --mysql_database=f2e --mysql_host=localhost --mysql_password=YOURPASSWORD --mysql_user=root


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