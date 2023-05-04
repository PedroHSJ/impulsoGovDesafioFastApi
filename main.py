from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import pytz

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url='/fusos-horarios')

@app.get("/fusos-horarios")
def obter_fusos_horarios():
    try:
        # Fuso horário -3 GMT
        fuso_horario_menos_3gmt = pytz.timezone('Etc/GMT-3')
        agora_3gmt = datetime.now(fuso_horario_menos_3gmt)

        # Fuso horário GMT -5
        fuso_horario_gmt_menos_5 = pytz.timezone('Etc/GMT-5')
        agora_gmt_menos_5 = datetime.now(fuso_horario_gmt_menos_5)

        return {
            "fuso_horario_menos_3gmt": agora_3gmt.isoformat(),
            "fuso_horario_gmt_menos_5gmt": agora_gmt_menos_5.isoformat()
        }
    except Exception as e:
        return {
            "erro": str(e)
        }

@app.get("/fusos-horarios_params/")
def obter_fusos_horarios_params(fuso: int):
    try:
        if(fuso == None):
            return {
                "erro": "Fuso horário não informado"
            }
        if(fuso > 0):
            fuso_horario = pytz.timezone(f'Etc/GMT+{fuso}')
        if(fuso < 0):
            fuso_horario = pytz.timezone(f'Etc/GMT{fuso}')
        agora = datetime.now(fuso_horario)
        return {
            "fuso_horario": agora.isoformat()
        }
    except Exception as e:
        return {
            "erro": str(e)
        }