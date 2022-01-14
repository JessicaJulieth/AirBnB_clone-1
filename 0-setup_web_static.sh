#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Update Linux
sudo apt-get -y update && sudo apt-get -y upgrade

# Install nginx
sudo apt-get -y install nginx

# Create the folder /data/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Create HTML file
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Symbolic link /data/web_static/current linked to /data/web_static/releases/test/
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static
sudo sed -i '25i location /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
