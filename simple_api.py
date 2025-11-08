from fastapi import FastAPI, Response
import uvicorn


app = FastAPI()

@app.get("/")
def hello():
    return { "message": "Witaj świecie!", "author": "Bartosz Bryniarski" }

@app.get("/xml")
def get_xml():
    xml_data = f"""<?xml version="1.0"?>
    <message>
        <title>Witaj świecie!</title>
        <author>Bartosz Bryniarski</author>
    </message>
    
    """
    return Response(content=xml_data, media_type="application/xml")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
