## tyto

### OSINT (Open Source Intelligence)
- the practice of gathering and analyzing publicly available information to produce intelligence. It involves collecting data from various open sources, like websites, social media, news outlets, and public records, and then analyzing it to answer specific questions or assess situations. 
It excludes classified or private data that requires specific authorization to access

## weasel

### TLD (Top-Level Domain)
- a parte final de um nome de domínio de internet, como ".com" ou ".org"

### Directory listing
- acontece quando um servidor web não encontra um arquivo padrão (como `index.html`) em um diretório e, em vez disso, mostra todos os arquivos existentes nele.
- Solução: desabilitar o autoindex no servidor. Ex - Nginx:
`autoindex off`
- ex00: http://cybersec.42sp.org.br:3317/content/flag/

### Fuzzing (fuzz test)
- a software testing technique that involves providing random or invalid data as input to a program to uncover potential bugs and security vulnerabilities
- ajudar a encontrar rotas não documentadas

### Path traversal (“dot-dot-slash”, “directory traversal”, “directory climbing” or “backtracking”)
A path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder
By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files
fonte: [OWASP](https://owasp.org/www-community/attacks/Path_Traversal)
- ex02: ../flag.txt
///etc/passwd

### SQL Injection
- ex03: admin' OR '1'='1
Código vulnerável:
```py
user = request.args["user"]
query = f"SELECT * FROM users WHERE name = '{user}'"
cursor.execute(query)
```

Se alguém passar `admin' OR '1'='1` na tela de login no campo de usuário, a query vira:
`SELECT * FROM users WHERE name = 'admin' OR '1'='1'`
o que retorna todos os usuários

- sqlmap: ferramenta para ajudar a automatizar os testes de verificação de SQL Injection

## gecko

### Codificação (Encoding)
- Transformar dados em outro formato para compatibilidade ou transporte
- Reversível se souber o esquema usado
- Ex: Base64, URL encoding, UTF-8
- Usos: enviar arquivos binários em texto (e-mail, JSON); garantir que caracteres especiais não quebrem uma URL

### Hashing
- Gerar uma "impressão digital" única de um dado
- Ex: MD5, SHA-256, bcrypt, Argon2
- Não é reversível, é unidirecional (para testar precisa fazer o hashing e ver se dá igual)
- Usos: armazenamento de senhas (com salt + algoritmos adequados), garantir integridade de arquivos (checksum), identificar dados iguais sem expor conteúdo

### Criptografia
- Proteger informações confidenciais para que só quem tem uma determinada chave consiga acessar
- Reversível (se tiver a chave)
- Simétrica: mesma chave para criptografar e descriptografar
- Assimétrica: chave pública e privada (ex: RSA)
- Usos: comunicação segura via HTTPS, VPN, armazenamento de dados sensíveis, assinaturas digitais (com chaves assimétricas)

### Segurança por obscuridade
- envolve concatenar várias codificações juntas na esperança de que um atacante não conheça a sequência e não consiga decodificar os dados
- pode criar uma falsa sensação de segurança
- ex01: from Hex e from Base64

#### ex02 - passos:
- https://hashes.com
- 629cf0d815ccb448a2c7a4d3d9cc3989 - MD5
- 70616c69746f - Hex encoded

# John the Ripper
- an Open Source password security auditing and password recovery tool

#### ex03 - passos:
- https://hashes.com
- c967d488512ab5559b446f97843de1be0d615088 - SHA1
- 6c69616d75703275 - Hex encoded string