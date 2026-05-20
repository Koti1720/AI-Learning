from fastapi import FastAPI
import random   

app = FastAPI()

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why did the bicycle fall over? Because it was two tired!",
    "Why did the math book look sad? Because it had too many problems!",
    "What do you call a fish with no eyes? Fsh!",   
    "Why did the coffee file a police report? It got mugged!"
]

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(JOKES)}
    