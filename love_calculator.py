print('Welcome to the love calculator!')
lover_name1=input('Enter your name:')
lover_name2=input('Enter second name:')
combine_name=lover_name1+lover_name2
combine_name=combine_name.upper()
L=0
O=0
V=0
E=0
for c in combine_name:
    if c=='L':
        L+=1
    if c=='O':
        O+=1
    if c=='V':
        V+=1
    if c=='E':
        E+=1
first_part=L+O
second_part=V+E
score=(first_part*10)+second_part
if score>100:
    score=100
print('Your love score is: '+str(score)+'%')