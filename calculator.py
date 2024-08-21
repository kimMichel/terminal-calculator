# Simple terminal application

a = input('defines a: ')
b = input('defines b: ')

print('1 - sum')
print('2 - minus')
print('3 - multiply')
print('4 - divide')

operation = input('select the operation: ')

if operation == '1':
    result = int(a) + int(b)
    print('Result: ' + str(result))

if operation == '2':
    result = int(a) - int(b)
    print('Result: ' + str(result))

if operation == '3':
    result = int(a) * int(b)
    print('Result: ' + str(result))

if operation == '4':
    result = int(a) / int(b)
    print('Result: ' + str(result))