from db.templates import UserActivity, AdminActivity, UserCart


def menu():
    print("1. Browse Categories 2. Exit")


def main():
    print('******************************************************')
    print('WELCOME TO MY CART'.center(50))
    print('******************************************************')
    useract = UserActivity()
    adminact = AdminActivity()
    cart = UserCart()
    flag = True

    while flag:
        print("select your choice\n")
        menu()
        choice = input()
        if choice == '1':
            useract.get_all_category()
            cat_choice = input("Select category\n")
            useract.get_products_by_category(category=cat_choice)
            prod_choice = input("Select Product\n")
            useract.get_product(name=prod_choice)
        if choice == '2':
            flag = False


if __name__ == '__main__':
    main()
