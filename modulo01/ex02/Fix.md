## Boas práticas

1. É recomendável incluir uma lista de domínios permitidos e verificar o input do usuário. (white list)
Se não tiver, o item 8 é essencial

2. Permitir apenas `http/https` ou só `https`, principalmente em produção

3. Também é recomendável não permitir acesso de arquivos locais, desativando o acesso a `file://`
Se for necessário o acesso a arquivos locais, fazer um diretório "sandbox", onde serão criados e armazenados esses arquivos. Por exemplo:
```py
SANDBOX_DIR = os.path.abspath("./safe_files")
```
4. Permitir acesso apenas a tipos específicos de arquivos, por exemplo, `.txt`

5. Bloquear o acesso a metadados e hostnames normalmente sensíveis, como o `localhost` e serviços de nuvem e arquivos específicos, IPs locais e sensíveis (como `169.254.169.254`- AWS -, `metadata.google.internal`)
(black list)

6. Não permitir redirecionamento para evitar redirecionamento para rede interna

7. não permitir o formato `user:pass@host`

8. Se permitir acesso a arquivos locais, fazer um `path normalization` + checagem se está no diretório correto
Path normalization transforma o path no caminho real (resolve `.`, `..`, barras duplicadas e símbolos estranhos e redundantes), para não estar no formato de um atalho malicioso (passar do diretório permitido (path traversal), por exemplo)


### Na resposta (vai além do ):
1. Escapar o conteúdo para evitar XSS com por exemplo, `html.escape`

2. Adicionar headers de segurança na response:

```
"X-Content-Type-Options = "nosniff"
```
- impede que o navegador tente adivinhar o tipo de conteúdo de um arquivo e execute algum código e resulte em XSS
Por exemplo, evita que um arquivo `.txt` com o conteúdo `<script>alert(1)</script>` e enviado como `text/plain` seja interpretado como `text/html` e acabe executando o código

```
"Referrer-Policy = "no-referrer"
```
- Controla o que é enviado no header Referer (a URL de origem da requisição). Com essa opção, nenhuma informação da página anterior é enviada quando o usuário clica em links ou faz requisições
