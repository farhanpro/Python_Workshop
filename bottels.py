word = 'Bottels'
for beer_num in range(99,0,-1):
    print(beer_num,word,"on the wall")
    print("Take one down")
    print("Pass it around")
    if beer_num == 1: 
        print("No more Bottels on the wall")
    else: 
        new_num = beer_num -1
        if new_num == 1:
            word ="Bottel"
        print(new_num,word,"on the wall")
        print()