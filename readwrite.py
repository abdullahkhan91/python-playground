#assigns the contents of name.txt to the full_name variable 
with open('name.txt') as f:
    full_name = f.read()

with open('hello.txt', 'w') as g:
    g.write('hello, my name is ')
    g.write(full_name)
    