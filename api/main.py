from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MatchInput(BaseModel):
  home_team:str
  odd_home:float
  odd_away:float

@app.get("/team/{team_name}")
def get_team(team_name:str):
  return {"Team":team_name}

@app.get("/odds")
def get_odds(home:float, away:float):
  diff= home-away
  return {"Home":home, "Away":away,"Difference":diff}

@app.post("/predict")
def predict_match(data:MatchInput):
  return {
    "received":data.home_team,
    "odd difference":data.odd_home-data.odd_away
  }
