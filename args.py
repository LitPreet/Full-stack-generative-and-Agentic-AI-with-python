# arguments handling in python

def special_chai(*ingrediants, **extras):
    print("ingrediants", ingrediants)
    print("exras", extras)

special_chai("Cinnamin", "elaichi", sweetner="Honey",  foam="yes")

def chai_order(order=None):
    if order is None:
        order = []

chai_order()        
