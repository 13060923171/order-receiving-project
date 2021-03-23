def buyToys():
    d = {
        '1':'[Barbie,25.99,6]',
        '2': '[GI Joy,44.78,9]',
        '3': '[Mary,23.99,6]',
        '4': '[Allen,22.99,6]',
        '5': '[Olivia,21.99,6]',
        '6': '[Natasha,19.99,6]',
        '7': '[Kevin,18.99,6]',
        '8': '[Rose,17.99,6]',
        '9': '[Kelly,16.99,6]',
        '10': '[Jeanne,15.99,5]',
        '11': '[James,14.99,6]',
        '12': '[Edith,12.99,6]',
        '13': '[Sophia,13.99,6]',
        '14': '[Charles,11.99,6]',
        '15': '[Ashley,10.99,6]',
        '16': '[William,9.99,6]',
        '17': '[Hale,5.99,6]',
        '18': '[Steve,55.99,6]',
        '19': '[David,65.99,6]',
        '20': '[Done Shopping]',
    }
    print(d)
    a = '如果你想要购买玩具,请说出玩具的号码!'
    print(a)
    b = input("请在这里输入号码:").split(",")
    print(b)
    for i in b:
        print(d[i])




if __name__ == '__main__':
    buyToys()