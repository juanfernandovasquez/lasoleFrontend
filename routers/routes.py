from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from modules.import_data import get_data

router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@router.get('/',response_class=HTMLResponse)
def return_index(request: Request):
    productos = get_data()
    return templates.TemplateResponse("index.html", {"request": request, "productos":productos})

