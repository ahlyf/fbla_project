# Player stats kept in sepeate file for sake of organization

class Player:
  def __init__(self, name="", position="",  country=""):
      self.name = name
      self.position = position
      self.skills = {"shooting": 0, "passing": 0, "stamina": 0}
      self.reputation = 40
      self.team_relationships = {}
      self.wealth = 0
      self.age = 15
      self.team = ""
      self.country = country
class PlayStatistics:
  def __init__(self):
      self.goals = 0
      self.assists = 0
      self.trophies = 0
      self.games_played = 0
      self.yellow_cards = 0
      self.red_cards = 0

  def update_goals(self, goals):
      self.goals += goals

  def update_assists(self, assists):
      self.assists += assists

  def update_trophies(self, trophies):
      self.trophies += trophies

  def update_games_played(self, games):
      self.games_played += games

  def update_yellow_cards(self, yellow_cards):
      self.yellow_cards += yellow_cards

  def update_red_cards(self, red_cards):
      self.red_cards += red_cards
    
players_outcome = ["G.O.A.T", "Great Player", "Good Player", "Average Player", "Bad Player","National Legacy Player", "Team Legend", "Not the Best", "Amatuer Player", "Worst player" ]
