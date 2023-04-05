# Streaming de vídeo utilizando Raspberry Pi Zero

## Impressões 3d
Case - https://www.thingiverse.com/thing:1325361
<br>
Camera - https://www.thingiverse.com/thing:504196

<br>

<img src="static/case_raspberry.jpeg" style="width:45%">
<img src="static/suporte_camera.jpeg" style="width:35%">

<br>

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
