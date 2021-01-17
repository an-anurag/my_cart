from db.users import UserActivity, AdminActivity, UserCart


def menu():
    print("1. category 2. exit")


def main():
    print('******************************************************')
    print('MY CART'.center(50))
    print('******************************************************')
    useract = UserActivity()
    adminact = AdminActivity()
    cart = UserCart()
    flag = True

    while flag:
        print("select your choice")
        menu()
        choice = input()
        if choice == '1':
            useract.get_all_category()
        if choice == '2':
            flag = False


if __name__ == '__main__':
    main()
