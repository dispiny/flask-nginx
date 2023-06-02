# from fastapi import FastAPI, Request, HTTPException
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
# from fastapi.staticfiles import StaticFiles


# app_http = FastAPI()
# app_https = FastAPI()
# templates = Jinja2Templates(directory="templates")

# app_https.mount("/static", StaticFiles(directory="./static"), name="static")
# app_http.mount("/static", StaticFiles(directory="./static"), name="static")

# @app_https.get('/', response_class=HTMLResponse)
# async def index_https(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# @app_http.get('/')
# async def index_http():
#     redirect_url = "https://127.0.0.1"  # 여기에 HTTPS URL을 입력하세요.
#     return RedirectResponse(url=redirect_url, status_code=301)


# if __name__ == '__main__':
#     import uvicorn

#     uvicorn.run(app_https, host='0.0.0.0', port=443, ssl_keyfile="cert/private.key", ssl_certfile="cert/certificate.pem")
#     uvicorn.run(app_http, host='0.0.0.0', port=80)


from flask import Flask, render_template, redirect

app_http = Flask(__name__)

@app_http.route('/')
def index_https():
    return render_template('index.html')

if __name__ == '__main__':
    app_http.run(host='0.0.0.0', port=5000)