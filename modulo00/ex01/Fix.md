## Práticas OWASP

1. Utilizar tokens anti CSRF
- Cada requisição de ação sensível deve incluir um token secreto e imprevisível.
- O token deve ser validado pelo servidor antes de processar a requisição.
- Geralmente é inserido em inputs ocultos de formulários ou em cabeçalhos customizados em requisições AJAX

```html
<form action="/transfer" method="POST">
  <input type="hidden" name="csrf_token" value="valor-aleatorio">
  ...
</form>
```

2. SameSite Cookies
```
Set-Cookie: sessionid=abc123; HttpOnly; Secure; SameSite=Strict
```

- Configurar cookies de sessão com `SameSite=Lax` ou `SameSite=Strict` impede que sejam enviados em requisições cross-site.
- SameSite=Lax é hoje o padrão nos navegadores modernos. Ele aceita GET e HEAD requests e uma request de navegação top-level (por exemplo, ao clickar em um link e ser redirecionado para outro site)

3. Nunca permitir POST em vez de GET

4. Double Submit Cookie
- o servidor envia um cookie com um token e o cliente deve reenviar esse valor num campo do formulário ou cabeçalho.
- O servidor valida se o cookie e o campo coincidem.

5. Reautenticação ou verificação adicional em ações sensíveis como mudança de senha, transferência dinheiro

6. APIs com proteções adicionais (que verificam um cabeçalho customizado que não podem ser enviados automaticamente por navegadores) (`X-CSRF-Token: abc123`) - Django tem isso
A API verifica nas requisições esse dado

