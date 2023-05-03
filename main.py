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