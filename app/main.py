from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import APPLICATION_DESCRIPTION
from config import APPLICATION_NAME
from config import DEBUG

app = FastAPI(debug=DEBUG, description=APPLICATION_DESCRIPTION, title=APPLICATION_NAME)


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


temporary_data = {
    "name": "new",
    "age": 10,
    "phone_number": 9500,
    "Pincode": 9500,
}


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "base.html", {"request": request, "title": "Hello There."}
    )


app.get("/react", response_class=HTMLResponse)


async def react_render(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
