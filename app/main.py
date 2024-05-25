from fastapi import FastAPI


app = FastAPI()

@app.get("/hotels")
def get_hotels(
    locations,
    date_from,
    date_to,
    stars,
):
    return "Отель Бридж Резорт 5 звезд"