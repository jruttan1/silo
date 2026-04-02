import networkx as nx
from crud import get_all_edges, get_all_notes
from sqlmodel import Session
from db import engine

G = nx.Graph()

def create_graph():
    with Session(engine) as session:
        edges =  get_all_edges(session)
        nodes = get_all_notes(session)