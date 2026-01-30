# HTTPS Deployment Configuration

This Django application is configured to enforce HTTPS using Django's
built-in security settings.

## SSL / TLS Setup
In a production environment, HTTPS would be enabled using a web server
such as Nginx or Apache with valid SSL/TLS certificates.

Example (Nginx):
- SSL certificates issued by Let's Encrypt
- Port 443 configured with SSL enabled
- All HTTP traffic redirected to HTTPS

## Django Configuration
- SECURE_SSL_REDIRECT ensures all traffic uses HTTPS
- HSTS headers instruct browsers to always use HTTPS
- Secure cookies are enabled to prevent data leakage
