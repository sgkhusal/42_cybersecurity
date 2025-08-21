# Cybersecurity M00 - EX01

## CSRF

Quando o hacker consegue fazer ações como se fosse o usuário. Ele aproveita da sessão ativa do usuário (cookies, tokens) e faz o navegador da vítima enviar requisições indesejadas
Geralmente é feito com a visita a um site malicioso

### Cenários:
- o exemplo do exercício: transferência de dinheiro em bancos
- alteração de senha em uma conta/e-mail
- ações administrativas em um sistema
- alterações de compra em e-commerce: enderaço de entrega, fazer pedidos


### O código:
- O endpoint /transfer aceita requisições POST sem nenhum tipo de verificação de autenticidade (ex: token CSRF, SameSite cookies, etc)
- Se o usuário estiver autenticado (por exemplo, via cookie de sessão), qualquer requisição POST com amount válido vai executar a transferência.
- No caso, não está autenticado, fazendo um simples POST via curl já consigo executar um script que executa a transferência:

```bash
curl -X POST -d "amount=1000" http://localhost:8080/transfer
```
