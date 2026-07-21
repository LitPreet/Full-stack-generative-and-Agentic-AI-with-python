def update_order():
    chai_type = "elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
        print(chai_type)
    kitchen()
    print("After update",chai_type)

update_order()        


