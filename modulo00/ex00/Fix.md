## Código
- Não usar input de usuário como entrada para execução de scripts
Remover
```js
var script = document.createElement("script");
script.textContent = userInput;
document.body.appendChild(script);
```

- Além disso, a recomendação da OWASP nesse tipo de vulnerabilidade é sempre escapar os inputs de usuários, para que eles não sejam de fato executados
```js
var safeInput = userInput
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
```

ou usando o DoomPurify (pode ser instalado via CDN):
```js
var userInput = DOMPurify.sanitize(document.getElementById("inputText").value);
```
```js
<script src="https://unpkg.com/dompurify@3.0.9/dist/purify.min.js"></script>
```

- usar `textContent` ao invés de `innerHTML` pro `userInput`

- Usar Content Security Policy (CSP) - 
```Content-Security-Policy: default-src 'self'; script-src 'self';```

## Cookies
- também proteger os cookies de sessão com `HttpOnly`. Exemplo:
```Set-Cookie: sessionId=abc123; HttpOnly```
- Não setar cookie no código JS:
```js
document.cookie = "ftCookies=If_You_See_Me_Its_Win";
```
