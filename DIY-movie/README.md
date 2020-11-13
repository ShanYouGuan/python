1.该项目是一个基于django 1.8.2版本的项目（地址http://121.42.156.185:8000/getmovielist/)
  主要包括电影展示，播放，电影问答，在线聊天，
  在线聊天不支持离线，离线消息接受不到，待完善


2.克隆完项目后，创建数据库，在setting.py中可以更改数据库地址;然后可以在数据库中执行：
  source /dnomoive/dnomovie.sql该命令，可以往数据库导入测试数据也可以用
  python manage.py makemigrations来创建空数据库;

3.pip install -r /dnomovie/requirements.txt安装项目需要的库

4.安装完后就可以启动了python manage.py runserver 0.0.0.0:8000 可能会报一个jpeg的错，装一个库就可以了。

测试用户：后台：admin  密码123
         普通：alex   密码 123或者1234



