# MyTinyURL
Flask URL Shortener


*DB Schema:*
```
create database mytinyurl;
use mytinyurl;
drop table if exists url_map;
create table url_map (
  url_id int not null auto_increment,
  full_url_hash varchar(255) not null,
  short_url_hash varchar(255) not null,
  url varchar(255) not null,
  primary key (url_id)
);
```


*Apache Config:*
```
<VirtualHost *:80>
  ServerName [SERVER NAME]

  WSGIDaemonProcess webtool threads=5 home=/opt/MyTinyURL/
  WSGIScriptAlias / "/opt/MyTinyURL/webtool.wsgi"

  <Directory "/opt/MyTinyURL">
    Options Indexes FollowSymLinks MultiViews ExecCGI
    AllowOverride None
    Require all granted
    WSGIProcessGroup webtool
    WSGIApplicationGroup %{GLOBAL}
  </Directory>
</VirtualHost>
```
