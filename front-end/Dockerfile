FROM php:7.3.3-apache

COPY source/ /var/www/html/
COPY php.ini /usr/local/etc/php/

RUN apt-get update && apt-get install -y vim
RUN docker-php-ext-install mysqli

EXPOSE 80