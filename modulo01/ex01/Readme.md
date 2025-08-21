# Cybersecurity M01 - EX01

## XML External Entities (XXE)
O XML permite definir entidades externas, que podem apontar para arquivos locais ou URLs remotas. Resolver essas entidades é uma opção do parser utilizado.

1. Se o parser não desabilita isso, um atacante pode vazar informações sensíveis do servidor, como o arquivo `/etc/passwd`

2. Pode ser usado também para fazer SSRF (Server-Side Request Forgery) via XXE, fazendo requisições HTTP internas
- acontece quando a entidade externa aponta para URLs remotas

Ex:
```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://localhost:5000/admin">
]>
<data>&xxe;</data>
```
- Normalmente usado para acessar serviços internos (intranet, localhost. cloud metadata e outros) que não são acessíveis diretamente pelo hacker
- o hacker consegue mapear a rede interna; pode acessar painéis de admin que só rodam em `localhost` ou rede privada
- pode roubar credenciais da nuvem
Ex: na AWS, `http://169.254.169.254/latest/meta-data/iam/security-credentials/` devolve chaves da conta
- pode tentar acessar outras máquinas

3. DoS em XML - Billion Laughs Attack

4. XPath Injection
Se não tiver sanitização pode acontecer algo semelhante a SQL injection
- XPath é uma linguagem usada para navegar e consultar dados em documentos XML
- Pode conseguir fazer login sem senha
- Extração de dados confidenciais
- Em alguns casos, até execução de código XSLT

5. XSLT Injection
Se o sistema aceita XSLT (Extensible Stylesheet Language Transformations), uma linguagem baseada em XML usada para transformar documentos XML em outros formatos (outro arquivo XML, HTML, JSON), o atacante pode injetar código malicioso e até executar comandos.
- XSLT é como se fosse um “template engine” para XML