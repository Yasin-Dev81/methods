

# 0
# install nginx
"sudo apt install nginx"

# 1
# install venv python
"sudo apt install -y python3-venv"

# 2
# create venv
"python -m venv django_env"

# 3
# open venv
"source django_env/bin/activate"

# 4
# clone project and install requirements
"git clone [github-project]"
"pip install -r requirements.txt"

# 5
# install gunicorn
"pip instll gunicorn"

# 6
# open settings.py and add server-ip
"nano [project-name]/config/settings.py"
ALLOWED_HOSTS = ['[server-ip]']

# 7
# create gunicorn config and paste bellow code
"mkdir conf"
"nano conf/gunicorn_config.py"

command = '/home/root/django_env/bin/gunicorn'
pythonpath = '/home/root/[project-name]'
bind = '[server-ip:8000]'
workers = 3

# 8

"gunicorn -c conf/gunicorn_config.py [project-name].wsgi"
"ctrl+C"

"bg"

# 9
"sudo service nginx start"

# "mkdir static"

# 10
# create bellow file and paste bellow code
"sudo nano etc/nginx/sites-available/[project-name]"
"""
server {
    listen 80;
    server_name [server-ip];

    location /static/ {
        root /home/root/static/;
    }

    location / {
        proxy_pass http://[server-ip]:8000;
    }
}
"""

# 11
"cd /etc/nginx/sites-enabled/"
"sudo ln -s /etc/nginx/sites-available/[project-name]"
"ls -l"

# 12
"sudo systemctl restart nginx"

