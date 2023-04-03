
## No Raspberry Pi
1 - Instalar todas as dependências
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - Executar
```bash
source venv/bin/activate
flask --debug run --host=0.0.0.0
```
