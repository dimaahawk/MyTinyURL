# MyTinyURL
Flask URL Shortener


*DB Schema:*
```
CREATE TABLE `url_map` (
  `url_id` int(11) NOT NULL AUTO_INCREMENT,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `full_url_hash` varchar(255) NOT NULL,
  `short_url_hash` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1
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