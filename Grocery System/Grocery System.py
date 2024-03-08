def data(filename,index1,index2):
    dict = {} 
    file = open(filename,'r')
    for line in file.readlines(): 
        line = line.strip()
        k = line.split('  ')[index1]    
        v = line.split('  ')[index2] 
        dict[k] = v 
    file.close()        
    return dict      

def main_selection():
    selection = input('--------------------\nWelcome to FRESHCO Sdn Bhd\n1.Admin\n2.New Customer\n3.Registered Customer\n4.Exit the program\nPlease enter the number for service(1/2/3/4)\n')
    if selection == '1' :     
        admin_login()
    elif selection == '2' :
        new_customer()
    elif selection == '3' :
        customer_login()
    elif selection == '4' : 
        exit()
    else :
        print('Invalid number')  
        main_selection()

def new_customer():
    selection = input('----------New Customer----------\n1.View Groceries detail\n2.Register\nChoose a service(Press any other word or number to exit new customer mode)\n')
    if selection == '1' :         
        view_grocery()
    elif selection == '2' : 
        register()
    else : 
        main_selection()

def register() :
    with open('./customer.txt','r') as file:
        customer_data = file.read()
    name = input('Please enter your detail:\nName: ')
    add = input('Address: ')
    email = input('Email ID: ')
    content = input('Content Number: ')
    gender = input('Gender: ')
    dob = input('Date of Birth: ')
    uid = input('User ID: ')
    while True:
        pwd = input('Password: ')
        pwd2 = input('Rewirte Password: ')
        if pwd2 == pwd:
            break
        else:
            print('Please make sure password and rewrite password are same')
    if uid not in customer_data :
        file = open('./customer.txt','a')  
        file.write(name+'  '+add+'  '+email+'  '+content+'  '+gender+'  '+dob+'  '+uid+'  '+pwd+'  '+'\n')
        file.close() 
    else :
        print('This User ID had already register')
    new_customer()

def admin_login() :
    for _ in '123': 
        pwd = input('Please enter password to login to access system: ')
        if pwd == 'tp069006':
            admin_mode()
            break
        else:
            print('Incorrect Password')
    else:
        print('3 times of incorrect password,please login again')
        main_selection()

def customer_login() :
    uid = input('Please enter your User ID: ')
    pwd = input('Please enter your password: ')
    uid_pwd = data('customer.txt',6,7)
    if uid in uid_pwd and pwd == uid_pwd.get(uid):
        with open('login.txt','w') as file :
            file.write(uid)
        print(f'Welcome back {uid}')
        customer_mode()
    else:
        print('User ID or password invalid')
        main_selection() 

def admin_mode() :
    selection = input('----------Admin Mode----------\n1.Upload Groceries\n2.View all Groceries\n3.Update Groceries information\n4.Delete Groceries information\n5.Search Groceries detail\n6.View all customers\' order\n7.Search customer\'s order\nChoose a service(Press any other word to exit admin mode)\n')
    if selection == '1' :
        upload_grocery()
    elif selection == '2' :
        view_all_grocery1()
    elif selection == '3' :
        update_grocery()
    elif selection == '4' :
        delete_grocery()
    elif selection == '5' :
        search_grocery()
    elif selection == '6' :
        view_customer_order()
    elif selection == '7' :
        search_customer_order()
    else :
        main_selection()

def upload_grocery() :
    with open('./grocery.txt','r') as file: 
        data = file.read()
    file = open('./grocery.txt','a')
    name = input('Name: ')
    price = input('Price(RM): ')
    exp = input('Exp Date(DD/MM/YY): ')
    spe = input('Specification: ')
    if name not in data : 
        file.write(name+'  '+price+'  '+exp+'  '+spe+'\n')
        file.close()
        print('Groceries had been uploaded')
    else :
        print('This grocery is already in system')
    admin_mode() 

def view_all_grocery2() :
    with open('grocery.txt','r') as file : 
        grocery_data = file.readlines()
        print('Name of groceries:')
        for lines in grocery_data : 
            grocery = lines.strip().split("  ")[0]
            print(grocery,end = '  ')
            print()
    print()
    customer_mode()

def view_all_grocery1() :
    with open('grocery.txt','r') as file :
        grocery_data = file.readlines()
        print('Name of groceries:')
        for lines in grocery_data : 
            grocery = lines.strip().split("  ")[0] 
            print(grocery,end = '  ')
            print()
    print()
    admin_mode()

def update_grocery() :
    searching = input('What grocery you want to update?\n')
    with open('grocery.txt','r') as file : 
        grocery_data = file.readlines()
    for i in grocery_data :
        if searching not in i :
            continue
        else :
            x = grocery_data.index(i)
    try :   # if searching not in system run the except
        print('Update for \n',grocery_data[x])
        name = input('Name: ')
        price = input('Price(RM): ')
        exp = input('Exp Date(DD/MM/YY): ')
        spe = input('Specification: ')
        grocery_data[x] = name+'  '+price+'  '+exp+'  '+spe+'  '+'\n'
    except :
        print('This grocery is not in system')
    file = open('grocery.txt','w') 
    for i in grocery_data :
        file.write(i)
    file.close()
    admin_mode()

def delete_grocery() :
    searching = input('What grocery you want to delete?\n')     
    with open('grocery.txt','r') as file : 
        grocery_data = file.readlines()
    for i in grocery_data : 
        if searching not in i :
            continue
        else :
            x = grocery_data.index(i)
    try:       
        grocery_data[x:x+1] = []
        print('The grocery has been delete')
    except:
        print('This grocery is not in system')
    file = open('grocery.txt','w')
    for i in grocery_data :
        file.write(i)
    file.close()
    admin_mode()

def search_grocery() :
    searching = input('What grocery you want to search?\n')
    with open('grocery.txt','r') as file :
        grocery_data = file.readlines()
    for i in grocery_data :
        if searching not in i :
            continue
        else :
            x = grocery_data.index(i)
    try :
        result = grocery_data[x]
        name = result.split('  ')[0]
        price = result.split('  ')[1]
        exp = result.split('  ')[2]
        spe = result.split('  ')[3]
        print(f'----------Result----------\nName: {name}\nPrice: {price}\nExpire Date(DD/MM/YY): {exp}\nSpecification: {spe}')
    except :
        print("This grocery is not in system")
    admin_mode()

def view_customer_order() :
    with open('order.txt','r') as file :
        order_data = file.readlines()
        print('All customer order:')
        for line in order_data :
            uid = line.split('  ')[0]
            order = line.split('  ')[1]
            print(f'----------Result----------UID: {uid}\nOrder: {order}')
    print()
    admin_mode()

def search_customer_order() :
    try :
        searching = input('Please enter your uid:\n') 
        with open('order.txt','r') as file :
            order_data = file.readlines()
        for i in order_data :
            if searching not in i :
                continue
            else :
                x = order_data.index(i)
        result = order_data[x]
        order = result.split('  ')[1]
        print(f'----------Result----------\nOrder:\n{order}')
    except:
        print()
        print('There is no any order')
    admin_mode()

def customer_mode() :
    selection = input('----------Registered Customer----------\n1.View all Groceries detail\n2.Order of Groceries\n3.View own order\n4.View personal information\nChoose a service(Press any other number to exit registered customer mode)\n')
    if selection == '1' :
        view_all_grocery2()
    elif selection == '2' :
        order()
    elif selection == '3' :
        view_order()
    elif selection == '4' :
        personal_information()
    else :
        main_selection()

def view_grocery() :
    with open('grocery.txt','r') as file : 
        grocery_data = file.readlines()
    print(grocery_data)
    for i in grocery_data :
        name = i.split('  ')[0]
        price = i.split('  ')[1]
        exp = i.split('  ')[2]
        spe = i.split('  ')[3]
        print(f'---------------\nName: {name}\nPrice: {price}\nExpire Date(DD/MM/YY): {exp}\nSpecification: {spe}---------------')
        print()
    new_customer()

def view_order() :
    try :
        with open('login.txt','r') as file:
            uid = file.read()
        with open('order.txt','r') as file :
            order_data = file.readlines()
        for i in order_data :
            if uid not in i :
                continue
            else :
                x = order_data.index(i)
        result = order_data[x]
        order = result.split('  ')[1]
        print(f'----------Result----------\nOrder:\n{order}')
    except:
        print()
        print('There is no any order')
    customer_mode()

def personal_information() :
    with open('login.txt','r') as file:
        uid = file.read()
    with open('customer.txt','r') as file :
       self_data = file.readlines()
    for i in self_data : 
        if uid not in i :
            continue
        else :
            x = self_data.index(i)
    result = self_data[x]
    name = result.split('  ')[0]
    add = result.split('  ')[1]
    email = result.split('  ')[2]
    content =result.split('  ')[3]
    gender = result.split('  ')[4]
    dob = result.split('  ')[5]
    print(f'----------Result----------\nName: {name}\nAddress: {add}\nEmail ID: {email}\nContent Number: {content}\nGender: {gender}\nDate of Birth: {dob}')
    customer_mode()

def order() :
    grocery_data = data('grocery.txt',0,1)
    basket = []
    payment = []
    asking = 'y'
    while asking == 'y':
        order = input('What is the grocery that you want to order?\n')
        quantity = input('How much you want?\n')
        basket.append(order+'*'+quantity)
        x = 0
        while x < int(quantity) :
            payment.append(float(grocery_data.get(order)))
            x += 1
        asking = input('Do you want to buy other grocery? y/n\n')
    print()
    sum = 0
    for i in payment:
        sum += i
    print('All paymant is RM %.2f'%sum)
    while True:
        pay = float(input('Please enter the value to do payment\n'))
        if pay == float(sum) :
            print(f"Thanks {chr(0b001)}")
            break 
        elif pay > float(sum):
            print(f"Return RM {pay-float(sum)} Thanks {chr(0b001)}")
            break 
        else:
            print('It is not enough!')
            continue
    with open('login.txt','r') as file:
        uid = file.read()
    order_list = uid+'  '
    for i in basket:
        order_list = order_list + i + '  '
    order_list = order_list + '\n'
    with open('order.txt','a') as file : 
        file.write(order_list)
    customer_mode()

main_selection()