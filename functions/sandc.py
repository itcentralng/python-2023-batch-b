def start():
    states = [
        {'name':'Kaduna', 'capital':'Kaduna'},
        {'name':'Akwa Ibom', 'capital':'Oyu'},
        {'name':'Benue', 'capital':'Makurdi'},
        {'name':'Lagos', 'capital':'Ikeja'},
        {'name':'Adamawa', 'capital':'Yola'},
    ]
    print("Welcome to the S&C Game!\n")
    name = input("Enter your name: ")
    ready = input("Are you ready to start? ")
    if ready == 'yes':
        for state in states:
            capital = input("What is the capital of "+state.get('name')+'? ')
            if capital.lower() == state.get('capital').lower():
                print('Thats correct')
            else:
                print('Thats Wrong the capital of '+state.get('name')+' is '+state.get('capital'))


start()