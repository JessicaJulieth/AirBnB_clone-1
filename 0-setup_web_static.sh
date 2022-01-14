#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Update Linux
sudo apt-get -y update && sudo apt-get -y upgrade

# Install nginx
sudo apt-get -y install nginx

# Create the folder /data/ if it doesn’t already exist
mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/

# Create HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Symbolic link /data/web_static/current linked to /data/web_static/releases/test/
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static
sudo sed -i "43i location /nombre_de_slug {todo lo que va adentro}"

# Restart nginx
sudo service nginx restart
