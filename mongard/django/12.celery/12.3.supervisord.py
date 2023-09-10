"""
- Daemonization
    * به برنامه‌ای میگن که تو پس زمینه داره اجرا میشه
- supervisord
    * app for Daemonization

"""
# 1
# install supervisor
"sudo apt-get install supervisor"

# 2
# all supervisor processes goes here "/etc/supervisor/conf.d"

# 3
# create project's celery configuration file for supervisor
"touch /etc/supervisor/conf.d/project_name.conf"

# 4.
# write supervisor configuration:
"nano /etc/supervisor/conf.d/project_name.conf"
"""
[program:project_name]
user=user
directory=/var/www/myproject/src/
command=/var/www/myproject/bin/celery -A myproject worker -l info
numprocs=1
autostart=true
autorestart=true
stdout_logfile=/var/log/myproject/celery.log # لاگ کل برنامه
stderr_logfile=/var/log/myproject/celery.err.log # لاگ ارورها
"""

# 5
# create log files
"touch /var/log/myproject/celery.log"
"touch /var/log/myproject/celery.err.log"

# 6
# update supervisor configuration
"supervisorctl reread"
"supervisorctl update"

# 7
# done
"supervisorctl {status|start|stop|restart} project_name"
