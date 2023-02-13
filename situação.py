aluno = {'nome': str(input('Nome: ')),
         'media': float(input('Média: '))}
if aluno['media'] >= 6:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'
print(f'O aluno {aluno["nome"]} tem média {aluno["media"]}, por isso está {aluno["situacao"]}.')
