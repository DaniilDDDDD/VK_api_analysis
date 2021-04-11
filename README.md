# VK_api_analysis

### Description
This project displays on the web page a graph of the data received from the VK_api:
- By selecting a "Wall", you will display a graph built according to data from the page
 of the user whose ID is entered in the field "owner_id"
- By selecting a "Stats", you will display a graph built according to data from community page,
the administrator of which is the owner of the token.
The community ID must be entered in the "group_id' field,
and the application ID must be entered in the "app_id" field.
In fields "timestamp_from" and "timestamp_to" you need to insert period of time for which the data will be analyzed.
In field "interval" you need to choose interval.
In field "intervals_count" you need to insert number of intervals.

There are choice of two types of graphics.

To use this app user need to click get token: click "Token" button, copy "access_token" from url and paste it
to "access_token" field.

### Launch of the project:
To start this app, you need to:
- Clone project from https://github.com/DaniilDDDDD/VK_api_analysis.git
- Go to the VK_api_analysis\VK_api_analysis directory of the project
- Activate python virtual environment and execute ```pip install -r requirements.txt```
- Execute ```python manage.py migrate``` then ```python manage.py runserver```
- Open node.js command prompt in the VK_api_analysis\Front directory, execute ```npm i``` and then ```npm start```
- App would be started on 8000 (backend) and 3000 (front) ports