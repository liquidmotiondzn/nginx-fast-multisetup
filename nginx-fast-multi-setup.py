print("////// Nginx Setup //////")
print()
print("requirements: nginx, certbot already setup")
print("Input your Domain (ex. mydomain.com)")
domain = str(input())

def get_domain(domain):
    print()
    print("-----NGINX part-----")
    print()
    print("sudo mkdir -p /var/www/" + domain + "/html")
    print("sudo chown -R $USER:$USER /var/www/" + domain + "/html")
    print("sudo chmod -R 755 /var/www/" + domain)
    print("sudo nano /var/www/" + domain + "/html/index.html")
    print()
    print("<html>")
    print("    <head>")
    print("        <title>Welcome to your_domain</title>")
    print("    </head>")
    print("    <body>")
    print("        <h1>Success! Your Nginx server is successfully configured for <em>your_domain</em>. </h1>")
    print("        <p>This is a sample page.</p>")
    print("    </body>")
    print("</html>")
    print()
    print("--- Control + O ---")
    print("--- Control + X ---")
    print()
    print("sudo nano /etc/nginx/sites-available/" + domain)
    print()
    print("server {")
    print("        listen 80;")
    print("        listen [::]:80;")
    print()
    print("        root /var/www/" + domain + "/html;")
    print("        index index.html index.htm index.nginx-debian.html;")
    print()
    print("        server_name " + domain + " www." + domain + ";")
    print()
    print("        location / {")
    print("                try_files $uri $uri/ =404;")
    print("        }")
    print("}")
    print()
    print("--- Control + O ---")
    print("--- Control + X ---")
    print()
    print("sudo ln -s /etc/nginx/sites-available/" + domain + " /etc/nginx/sites-enabled/")
    print("sudo nginx -t")
    print("sudo systemctl restart nginx")
    print()
    print("-----Certbot part-----")
    print()
    print("sudo certbot --nginx -d " + domain + " -d www." + domain)
    print("sudo certbot renew --dry-run")
    print("-----DONE-----")

get_domain(domain)
