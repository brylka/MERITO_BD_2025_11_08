from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()

@app.get("/")
def hello():
    return { "message": "Aplikacja edukacyjna MERITO BD"}

@app.get("/json")
def get_json():
    return { "title": "Witaj świecie!", "author": "Bartosz Bryniarski" }

@app.get("/xml")
def get_xml():
    xml_data = f"""<?xml version="1.0"?>
    <message>
        <title>Witaj świecie!</title>
        <author>Bartosz Bryniarski</author>
    </message>
    """
    return Response(content=xml_data, media_type="application/xml")

@app.get("/html", response_class=HTMLResponse)
def get_html():
    html_data = """<!DOCTYPE html>
<html>
    <head>
        <title>Witaj świecie!</title>
    </head>
    <body>
        <author>Bartosz Bryniarski</author>
    </body>
</html>"""
    return html_data



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
