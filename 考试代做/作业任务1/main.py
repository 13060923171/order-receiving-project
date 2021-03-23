def displayWelcome():
    print(r"""
 __      __       .__                                  __           _____.___.            .__/\       ___________                      __
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   \__  |   |__ _________|__)/______ \__    ___/___ ___.__.   _______/  |_  ___________   ____
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \   /   |   |  |  \_  __ \  |/  ___/   |    | /  _ <   |  |  /  ___/\   __\/  _ \_  __ \_/ __ \
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  \____   |  |  /|  | \/  |\___ \    |    |(  <_> )___  |  \___ \  |  | (  <_> )  | \/\  ___/
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   / ______|____/ |__|  |__/____  >   |____| \____// ____| /____  > |__|  \____/|__|    \___  >
       \/       \/          \/            \/     \/                  \/                           \/                 \/           \/                          \/
""")


def populateAvailableToylist():
    from Toy import Toy
    t1 = Toy("LEGO Star Wars", 88.98, 3)
    t2 = Toy("Sand Molds", 9.99, 3)
    t3 = Toy("Water Gun", 14.99, 4)
    t4 = Toy("Caterpillar Construction Fleet Excavator", 9.99, 5)
    t5 = Toy("Pokemon Pokeball", 9.99, 3)
    t6 = Toy("Nintendo Super Mario Odyssey Cappy Plush Hat", 17.99, 2)
    t7 = Toy("Camera for Kids", 20.99, 6)
    t8 = Toy("Horse Care Play Set", 20.99, 3)
    t9 = Toy("Funtime Tractor", 4.99, 2)
    t10 = Toy("Thomas Wood Diesel Wooden Tank Engine Train", 8.60, 2)


    d = {
        '1': 'Toy name:{}\nprice:{}\nMinAgeReq:{}\n'.format(t1.name,t1.price,t1.minAge),
        '2': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t2.name, t2.price, t2.minAge),
        '3': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t3.name, t3.price, t3.minAge),
        '4': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t4.name, t4.price, t4.minAge),
        '5': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t5.name, t5.price, t5.minAge),
        '6': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t6.name, t6.price, t6.minAge),
        '7': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t7.name, t7.price, t7.minAge),
        '8': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t8.name, t8.price, t8.minAge),
        '9': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t9.name, t9.price, t9.minAge),
        '10': 'Toy name:{}\n price:{}\n MinAgeReq:{}\n'.format(t10.name, t10.price, t10.minAge),
    }
    return d


def buyToys():
    d = populateAvailableToylist()
    print(d)
    a = 'If you want to buy a toy, please state the toy number!'
    print(a)
    b = input("Please enter the number here(Please use commas to separate them):").split(",")
    print("{:=^100}".format("Split Line"))
    for i in b:
        print(d[i])
        print("{:=^100}".format("Split Line"))


if __name__ == '__main__':
    displayWelcome()
    populateAvailableToylist()
    buyToys()


