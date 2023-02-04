total = count = average = more = less = 0
awnser = 'YES'
while awnser in 'YESyes':
    number = int(input('Type a number: '))
    total += number
    count += 1
    awnser = str(input('Wanna keep going? [YES or NO]: ')).upper().strip()[0]
    if count == 1:
        more = less = number
    else:
        if number > more:
            more = number
        if number < less:
            less = number
average = total / count
print('It´s over')
print(f'''Total sum = {total}
Average = {average:.1f}
Biggest = {more} 
Smaller = {less}''')

