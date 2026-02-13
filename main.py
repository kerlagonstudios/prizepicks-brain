from fastapi import FastAPI
import random

app = FastAPI()

# This is a "Mock" database of PrizePicks data
# In a real version, we would replace this with a scraper
def get_prizepicks_data():
    players = ["LeBron James", "Kevin Durant", "Luka Doncic", "Tyrese Haliburton"]
    props = ["Points", "Assists", "Rebounds"]
    
    picks = []
    for _ in range(5):
        player = random.choice(players)
        line = round(random.uniform(5.5, 28.5), 1)
        picks.append({
            "player": player,
            "prop": random.choice(props),
            "line": line,
            "recommendation": "OVER" if line < 15 else "UNDER"
        })
    return picks

@app.get("/get_bets")
def read_root():
    return {"status": "active", "bets": get_prizepicks_data()}
