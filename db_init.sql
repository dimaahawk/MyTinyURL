CREATE TABLE `url_map` (
  `url_id` int(11) NOT NULL AUTO_INCREMENT,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `full_url_hash` varchar(255) NOT NULL,
  `short_url_hash` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `visits` int(11) DEFAULT '0',
  `ip_address` varchar(255) NULL DEFAULT NULL,
  `user_agent` varchar(255) NULL DEFAULT NULL,
  PRIMARY KEY (`url_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1