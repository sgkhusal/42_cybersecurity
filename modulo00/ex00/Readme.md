# Cybersecurity M00 - EX00

## Cross-Site Scripting (XSS)

- Os cookies podem ficar disponíveis de forma insegura na variável do `document.cookie` (ao olhar o html de retorno, a variável está sendo setada em um script)
- Ao fazer `console.log` a variável aparece no console
- Ao olhar o html da página, o script do submit coloca o que foi digitado dentro da caixa em uma tag de script, e vemos o erro no console quando o código não consegue executar nada
- ao adicionar o código js abaixo nesse campo, o mesmo acaba sendo executado e resulta no output pedido:

```js
document.getElementById("cookieOutput").textContent = `Cookie value: ${document.cookie}`
```
De posse do cookie poderia se fazer requisições como se fosse o usuário, por exemplo:
```bash
curl -X POST -b 'ftCookies=If_You_See_Me_Its_Win' http://localhost:8000 --verbose
```

- XXS permite que se execute scripts maliciosos nas páginas, para roubar dados de cookies, como no exemplo, session tokens ou fazer outras coisas como se fosse o usuário. Através de um formulário, foi possível executar o script que retornou o dado do cookie.
- Essa vulnerabilidade é uma DOM-based XSS (existente no JS do lado do client)


## OWASP
(Open Worldwide Application Security Project)
A OWASP traz guidelines para o desenvolvimento de software de forma mais segura

