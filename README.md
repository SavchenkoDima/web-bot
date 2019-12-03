# web-bot
,telegram-bot
,nginx
,rest-Api
,flask

ngnix - config file
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	listen 443 ssl http2;        
	listen [::]:443 ssl http2; 
	root /var/www/html;

	# Add index.php to the list if you are using PHP
	index index.html index.htm index.nginx-debian.html;

	server_name localhost;

	ssl_certificate /etc/ssl/certs/webhook_cert.pem;        
	ssl_certificate_key /etc/ssl/private/webhook_pkey.pem;
                
	ssl_protocols TLSv1.2 TLSv1.1 TLSv1;
	# This is location for the telegram bot
  location / {
		proxy_http_version 1.1;
                proxy_pass http://127.0.0.1:5000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Real-IP $remote_addr;
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
	}

  # This is location for the REST-API. Category
	location /Category/ {
		proxy_http_version 1.1;
                proxy_pass http://127.0.0.1:4000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Real-IP $remote_addr;
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
	}
  # This is location for the REST-API. Product
	location /Product/ {
		proxy_http_version 1.1;
                proxy_pass http://127.0.0.1:4000;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Real-IP $remote_addr;
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
	}



	# pass PHP scripts to FastCGI server
	#
	#location ~ \.php$ {
	#	include snippets/fastcgi-php.conf;
	#
	#	# With php-fpm (or other unix sockets):
	#	fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
	#}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
}
