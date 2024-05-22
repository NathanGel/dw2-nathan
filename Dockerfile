FROM ubuntu

RUN apt-get update && apt-get install -y apache2 && apt-get clean

RUN date >/var/www/html/buildtime.txt

COPY html /var/www/html

EXPOSE 81

RUN sed -i 's/listen 80/listen 81/' /etc/apache2/ports.conf
RUB sed -i 's/:80/:81/' /etc/apache2/sites-available/000-default.conf

CMD ["apache2ctl", "-D", "FOREGROUND"]