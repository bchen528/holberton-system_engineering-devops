# 0x1A. Application server

[0-welcome_gunicorn-upstart_config](0-welcome_gunicorn-upstart_config) - Upstart config file that starts a Gunicorn instance to serve web_flask/0-hello_route.py from AirBnB_clone_v2

[0-welcome_gunicorn-nginx_config](0-welcome_gunicorn-nginx_config) - Nginx config file where route /airbnb-onepage/ points to the Gunicorn instance mentioned above, serves this page both locally and on its public IP on port 80

[1-pass_parameter-upstart_config](1-pass_parameter-upstart_config) - Upstart config file that starts a Gunicorn instance to serve web_flask/6-number_odd_or_even.py from AirBnB_clone_v2

[1-pass_parameter-nginx_config](1-pass_parameter-nginx_config) - Nginx config file where route/airbnb-dynamic/ points to Gunicorn instance mentioned above, serves this page both locally and on its public IP on port 80

[2-api-upstart_config](2-api-upstart_config) - Upstart config that starts a Gunicorn instance to serve api/v1/app.py from AirBnB_clone_v3

[2-api-nginx_config](2-api-nginx_config) - Nginx config where route /api/ points to Gunicorn instance mentioned above, serves this page both locally and on its public IP on port 80

[3-complete_webapp-upstart_config](3-complete_webapp-upstart_config) - Upstart config that starts a Gunicorn instance to serve web_dynamic/2-hbnb.py from AirBnB_clone_v4

[3-complete_webapp-nginx_config](3-complete_webapp-nginx_config) - Nginx config where route / points to Gunicorn instance mentioned above, properly serves the static assets found in web_dynamic/static/, serves this page both locally and on its public IP on port 80
