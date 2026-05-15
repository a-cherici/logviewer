openssl req -x509 -nodes -days 825 \
  -newkey rsa:4096 \
  -keyout private.key \
  -out certificate.crt \
  -config san.cnf