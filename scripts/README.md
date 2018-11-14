## Project deployment steps

*This is just copied from wholesaler*

1. Add DNS record in Veebimajutus admin, test that it works (wait a bit)

        ping aed.herbfoods.eu

2. Install Apache and required packages

        apt install libapache2-mod-wsgi-py3 apache2 \
            python3-pip python3-virtualenv \
            build-essential software-properties-common

3. Add user

        sudo adduser herbfoods

4. Create project base directory

        sudo mkdir /var/www/projects/herbfoods
        sudo chown herbfoods: /var/www/projects/herbfoods

5. Generate SSH key

        sudo su herbfoods
        ssh-keygen
        cat ~/.ssh/id_rsa.pub

6. Add SSH key to GitLab project
7. Clone project and create htdocs directory

        cd /var/www/projects/herbfoods
        git clone git@gitlab.com:herbfoods/wholesaler.git
 
8. Verify that WSGI script is configured properly and that requirements.txt
   exists and contains Pillow and that DEBUG is off in settings, email sending
   and logging works, upload permissions are correct etc

        --- a/wholesaler_app/wsgi.py
        +++ b/wholesaler_app/wsgi.py

        -import os
        +import os, sys
         
         from django.core.wsgi import get_wsgi_application
         
        +BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        +sys.path.append(BASE_DIR)

9. Setup virtualenv

        python3 -m virtualenv --python=python3 venv
        . venv/bin/activate
        pip install --requirement=src/requirements.txt

10. Test email sending

        ./src/manage.py shell
        from django.core.mail import send_mail
        from django.conf import settings
        send_mail('subject', 'message', settings.SERVER_EMAIL, ['mart.somermaa@gmail.com'], fail_silently=False)

11. Create admin user

        ./src/manage.py migrate
        ./src/manage.py createsuperuser

12. Configure Apache virtualhost

        cd /etc/apache2/sites-available/
        sudo su
        cat > herbfoods.conf <<EOF
        <VirtualHost *:80>
            ServerName      aed.herbfoods.eu

            DocumentRoot    /var/www/projects/herbfoods/wholesaler/htdocs
            CustomLog       /var/log/apache2/herbfoods.access.log combined
            ErrorLog        /var/log/apache2/herbfoods.error.log

            Alias /static      /var/www/projects/herbfoods/wholesaler/htdocs/static
            Alias /robots.txt  /var/www/projects/herbfoods/wholesaler/htdocs/robots.txt
            Alias /favicon.ico /var/www/projects/herbfoods/wholesaler/htdocs/favicon.ico

            Alias /dashboard   /var/www/projects/herbfoods/wholesaler/htdocs/static/media/dashboard

            # Uncomment after HTTPS is enabled
            # WSGIPassAuthorization On

            # WSGIScriptAlias / /var/www/projects/herbfoods/wholesaler/src/wholesaler/wsgi.py
            # WSGIDaemonProcess herbfoods \\
            #         user=herbfoods threads=15 display-name=herbfoods \\
            #         python-path=/var/www/projects/herbfoods/wholesaler/venv/lib/python3.5/site-packages
            # WSGIProcessGroup herbfoods

        </VirtualHost>
        EOF

13. Activate, verify and enable new configuration

        a2ensite herbfoods
        apache2ctl -S
        service apache2 reload

14. Open HTTPS port in firewall if it is closed
15. Get Let's Encrypt certificate and enable HTTPS support

        sudo add-apt-repository ppa:certbot/certbot
        sudo apt-get update
        sudo apt-get install python-certbot-apache
        sudo certbot --apache
        sudo certbot renew --dry-run
        sudo su
        cat > /etc/cron.daily/letsencrypt-cert-renewal <<EOF
        #!/bin/sh
        certbot renew -q
        EOF
        chmod 755 /etc/cron.daily/letsencrypt-cert-renewal
        /etc/cron.daily/letsencrypt-cert-renewal

16. Allow SSH key-based access to developers

        scp id_rsa.pub herbfoods@aed.herbfoods.eu:
        cat id_rsa.pub >> /home/herbfoods/.ssh/authorized_keys 

17. Test deployment script

        sudo apt-get install fabric
        ./scripts/deploy.sh

