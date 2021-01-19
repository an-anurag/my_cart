from db.templates import UserActivity, AdminActivity, UserCart


def menu():
    print("1. Browse Categories 2. Exit")


def main():
    print('******************************************************')
    print('WELCOME TO MY CART'.center(50))
    print('******************************************************')
    user_act = UserActivity()
    admin_act = AdminActivity()
    cart = UserCart()
    flag = True

    while flag:
        print("Enter your choice\n")
        menu()
        choice = input()

        if choice == '1':
            user_act.get_all_category()
            cat_choice = input("Select category\n")
            user_act.get_products_by_category(category=cat_choice)
            prod_choice = input("Select Product\n")
            user_act.get_product(name=prod_choice)

        if choice == '2':
            flag = False


if __name__ == '__main__':
    main()
