from openai import OpenAI

class Agent:

   def __init__(self, session):
      self.client = OpenAI()
      self.session = session
      self.history = []
