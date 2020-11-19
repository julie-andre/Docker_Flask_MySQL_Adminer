# Docker_Flask_MySQL_Adminer
A flask application containerized with Docker. This app works with two other containerized services which are Adminer and a MySQL database.
The dependencies and other parameters are defined in the docker-compose.yaml file.
This app is a simple blog, which store posts in a mysql table. 
It displays a page where the user can submit his first post, another page is then displayed with the list of Posts, and for each post auhor's ip adress and creation date and time.
Below this list, there are a text input and a submit button where the user can enter new posts. The posts are inserted in the database with author's ip and datetime and displayed on the web page.
The database and table are created by the python code (app.py) but the user can also create it with the help of Adminer. 
Therefore, the posts of the database are also visible with Adminer.
