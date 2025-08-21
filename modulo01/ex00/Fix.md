Evitar inserir código dinâmico do usuário dentro de templates.

Nunca colocar a entrada do usuário diretamente dentro de {{ {user_input }}}, que executa o input do usuário como código. Algumas estratégias seguras:

1. Usar render_template com variáveis ao invés de render_template_string

```py
@app.route('/render', methods=['POST'])
def render():
    user_input = request.form.get('input')
    return render_template("index.html", name=user_input)
```

O Jinja2 vai escapar automaticamente HTML e não vai interpretar código Python.
Entrada do usuário nunca vira código executável.

2. Se realmente precisar de render_template_string, não usar f-strings:

```py
template = 'Hello, {{ name }}!'
return render_template_string(template, name=user_input)
```

Aqui o usuário só é tratado como valor, não como código.
Evita a execução de qualquer payload de template.

3. Validar e sanitizar entrada
