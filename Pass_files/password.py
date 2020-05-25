import string,random  
ENTRY=(
('a', '!+'),
('b', '""'),
('c', '#|'),
('d', '$('),
('e', '%&'),
('f', '&='),
('g', "'="),
('h', '(['),
('i', '),'),
('j', '*`'),
('k', '+`'),
('l', ',['),
('m', '-_'),
('n', '.>'),
('o', '/\\'),
('p', ':#'),
('q', ';*'),
('r', '<$'),
('s', '=/'),
('t', '>/'),
('u', '?_'),
('v', '@<'),
('w', '[`'),
('x', '\\%'),
('y', ']\\'),
('A', '!>'),
('B', '"\''),
('C', '#_'),
('D', '$^'),
('E', '%\\'),
('F', '&['),
('G', "'_"),
('H', '(('),
('I', ')@'),
('J', '*"'),
('K', '+"'),
('L', ',<'),
('M', '-@'),
('N', '.|'),
('O', '/='),
('P', ':<'),
('Q', ';!'),
('R', '<^'),
('S', '=?'),
('T', '>.'),
('U', '?>'),
('V', '@<'),
('W', '[:'),
('X', '\\{'),
('Y', ']-'),
('1', '"\\'),
('2', '#}'),
('3', '$<'),
('4', '%`'),
('5', '&/'),
('6', "'>"),
('7', '(.'),
('8', ')('),
)

def pass_gen(password):
    for x,y in ENTRY:
        password=password.replace(x,y)
    return password  

def pass_ext(password):
    for x,y in ENTRY:
        password=password.replace(y,x)
    return password 

if __name__ == "__main__":
    action=input('Chose your action (secure|extract) password: ')
    password = input("Input your password: ")

    if (action!='extract') and (action!='secure'):
        print(f"Invaild syntax inserted ⚠")

    elif (action == 'secure'):
        print(f"Your secure password is {pass_gen(password)}")

    
    elif (action == 'extract'):
        print(f"Your original password is {pass_ext(password)}")
        
    
    

input('Please hit enter to exit: ')
