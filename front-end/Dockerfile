FROM php:7.3.3-apache

COPY source/ /var/www/html/
COPY php.ini /usr/local/etc/php/
COPY mime.conf /etc/apache2/mods-enabled/

RUN apt-get update && apt-get install -y vim
RUN docker-php-ext-install mysqli

EXPOSE 80