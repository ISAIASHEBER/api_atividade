from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=29)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Galleani')
    for p in pessoa:
        print(p)
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()