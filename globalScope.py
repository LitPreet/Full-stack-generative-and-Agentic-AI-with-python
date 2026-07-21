chai_type = "Elaichi"

def front_desk():
    def kitchen():
      global chai_type
      chai_type = "Erani"
    kitchen()

front_desk()    
print("After update",chai_type)  

