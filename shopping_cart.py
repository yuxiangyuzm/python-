#encoding: utf-8

product_list = [('apple',500), ('car', 1000), ('phone', 600), ('pen', 50), ('ball', 120)]
shopping_list = []
salary = input('plz input your salary:')
if salary.isdigit():
    salary = int(salary)
    while True:
        for item in product_list:
            print(product_list.index(item),item)
        user_choice = input('选择要买的商品: ')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice>=0:
                p_item = product_list[user_choice]
                if p_item[1] < salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print('add %s into shopping cart,your balence is %s:'%(p_item,salary))
                else:
                    print('\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m'% salary) #高亮的用法
            else:
                print('product code [%s] is not exist'% user_choice)
        elif user_choice == 'end':
            print('- - - - shopping list - - - -')
            for p in shopping_list:
                print(p)
            print('your current balance is %s',salary)
            exit()
        else:
            print('invalid option')


