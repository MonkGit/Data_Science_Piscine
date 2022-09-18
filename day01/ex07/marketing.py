import sys

def call_center():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    # participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    call_center = list(set(clients) - set(recipients))
    return(call_center)
  

def potential_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    
    potential_clients = list(set(participants) - set(clients))
    return (potential_clients)

def  loyalty_program():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
  
    
    loyalty_program = list(set(clients) - set(participants))
    return (loyalty_program)

def marketing(task):
    if task == 'call_center':
        print(call_center())
    elif task == 'potential_clients':
        print(potential_clients())
    elif task == 'loyalty_program':
        print(loyalty_program())
    else:
        raise Exception('Wrong task') 


if __name__ == '__main__':
    if len(sys.argv) == 2:
        marketing(sys.argv[1])
    else:
        raise Exception('Wrong argument')