from .link_geometry import create_link
from .placement import duplicate_and_place

def run():
    return duplicate_and_place(create_link())
