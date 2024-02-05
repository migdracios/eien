from json import JSONDecodeError
from fastapi import FastAPI, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# 정적 파일을 제공하기 위한 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 엔진을 사용하기 위한 설정
templates = Jinja2Templates(directory="templates")

# index.html을 렌더링하는 엔드포인트
@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 이미지 파일 제공 예제
@app.get("/images/{image_name}")
async def get_image(image_name: str):
    return FileResponse(f"static/images/{image_name}", media_type="image/png")

# report posting api
@app.post("/api/report")
async def post_report(request: Request):
    receive_form = await request.form()
    for field_key, field_value in receive_form.items():
        print(field_key, field_value)
    


    return ""