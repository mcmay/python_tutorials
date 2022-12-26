from operator import itemgetter


def print_menu():
    menu = ['Sort stock list by:',
            '1) Sticker symbols',
            '2) Stock prices',
            '3) Both',
            '4) Reversed symbols',
            '5) Reversed prices',
            '6) Reversed both',
            '7) Quit']
    for menu_item in menu:
        print(menu_item)


stock_info = [('META', 108.25), ('QCOM', 110.68), ('GOOG', 88.26), ('IMB', 140.88),
              ('GOOG', 92.32), ('AAPL', 132.23), ('META', 117.12), ('AMZN', 83.79),
              ('MSFT', 238.19), ('AAPL', 128.25), ('TSLA', 125.35), ('AMZN', 85.29)]

print_menu()
QUIT = '7'
while (choice := input('Enter your choice: ')) != QUIT:
    if choice == '1':
        # same as sorted_stocks = sorted(stock_info, key=itemgetter(0), reverse=False)
        sorted_stocks = sorted(stock_info, key=itemgetter(0))
    elif choice == '2':
        # same as sorted_stocks = sorted(stock_info, key=itemgetter(0), reverse=False)
        sorted_stocks = sorted(stock_info, key=itemgetter(1))
    elif choice == '3':
        # same as sorted_stocks = sorted(stock_info, key=itemgetter(0,1), reverse=False)
        sorted_stocks = sorted(stock_info)
    elif choice == '4':
        sorted_stocks = sorted(stock_info, key=itemgetter(0), reverse=True)
    elif choice == '5':
        sorted_stocks = sorted(stock_info, key=itemgetter(1), reverse=True)
    elif choice == '6':
        # same as sorted_stocks = sorted(stock_info, key=itemgetter(0,1), reverse=True)
        sorted_stocks = sorted(stock_info, reverse=True)
    elif choice == QUIT:
        break
    else:
        print('Invalid choice.')
        print_menu()
        continue

    count = 0
    for stock in sorted_stocks:
        print(stock, end=' ')
        if (count + 1) % 3 == 0:
            print()
        count += 1

    print_menu()

print('Bye!')
