#Nome: Álef Miguel de Oliveira Gil Santiago
#RGM: 29881595

class ListaDisciplina:

    def __init__(self,codigo,nomeDis,frequencia,nota):
        
        self.codigo = codigo
        self.nomeDis = nomeDis
        self.frequencia = frequencia
        self.nota = nota
        self.proximoDis = None

        def getCodigo(self):
            return self.codigo
        
        def setCodigo(self,codigo):
            self.codigo = codigo

        def getNomeDis(self):
            return self.nomeDisciplina
        
        def setNomeDis(self,nome):
            self.nomeDisciplina = nome
        
        def getFrequencia(self):
            return self.frequencia
        
        def setfrequencia(self,frequencia):
            self.frequencia = frequencia
        
        def getNota(self):
            return self.nota
        
        def setNota(self,nota):
            self.nota = nota

        def getProximoDis(self):
            return self.proximo
        
        def setProximoDis(self,proximo):
            self.proximo = proximo

    def mostraListaDisciplina(self):
                
        return f'''
                    Codigo da Disciplina: {self.codigo}
                    Nome da Disiplina: {self.nomeDis}
                    Frequencia aluno: {self.frequencia}
                    Nota: {self.nota}'''   

class ListaLigadaDisciplina:

    def __init__(self):
        self.inicio = None
    
    def insereDisciplinaInicio(self,codigo,nomeDis,frequencia,nota):
        
        no = ListaDisciplina(codigo,nomeDis,frequencia,nota)
        no.proximoDis = self.inicio
        self.inicio = no
    
    def removeDisciplinaInicio(self):
        
        aux = self.inicio
        if aux:
            self.inicio = aux.getProximoDis()

    def existeDisciplina(self,x):
        
        p = self.inicio
        encontrou = False

        while p and not encontrou:
            if x == p.getCodigo():
                encontrou=True
            p = p.getProximoDis()

        return print(encontrou)


    def mostraLista(self):

        atual = self.inicio

        while atual:
            print(f'''
                    Codigo da Disciplina: {getCodigo()}
                    Nome da Disiplina: {getNomeDis()}
                    Frequencia aluno: {getFrequencia()}
                    Nota: {getNota()}''')
            
            atual=atual.getProximo()


    def contaNoLista(self):
        
        atual=self.inicio
        cont=0
        
        while atual:
            cont=cont+1
            atual=atual.getProximoDis()

        print(f'Tamanho da lista: {cont}')


    def insereUltimo(self,codigo,nomeDis,frequencia,nota):
        
        atual=self.inicio
        if not atual:
            self.insereInicio(codigo,nomeDis,frequencia,nota)
            return
        
        while atual.getProximoDis():
            atual = atual.getProximoDis()
        no = ListaDisciplina(codigo,nomeDis,frequencia,nota)
        atual.setProximo(no)

    def removeUltimo(self):
        
        p = None
        q = self.inicio
        
        if not q:
            print(f'lista vazia')
            return

        while q.getProximo():
            
            p = q
            q = q.getProximoDis()

        if p == None:
            self.inicio = None

        else:
            p.setProximo(None)


    def insereDepois(self,p,codigo,nomeDis,frequencia,nota):
        no = ListaDisciplina(codigo,nomeDis,frequencia,nota)
        no.setProximo(p.getProximo())
        p.setProximo(no)

    def removeDepois(self,p):
        aux = p.getProximoDis()
        p.setProximoDis(aux.getProximoDis())


    def insereOrdenado(self,x,codigo,nomeDis,frequencia,nota):
        
        p = self.inicio
        if not p or x < p.getCodigo():
            self.insereInicio(codigo,nomeDis,frequencia,nota)
            return
        q = p

        while q and q.getInfo() < x :
            p=q
            q=q.getProximoDis()

        if not q or q.getCodigo() > x :
            self.insereDepois(p,codigo,nomeDis,frequencia,nota)
        else:
            print(f'Elemento anteriormente cadastrado')

    def removeOrdenado(self,x,codigo,nomeDis,frequencia,nota):
        p = self.inicio
        if not p:
            print(f'lista vazia')
            return

        if p.getCodigo() == x:
            self.removeInicio()
            return

        q = p
        while q and q.getInfo() < x:
            p = q
            q = q.getProximoDis()

        if q and q.getInfo() == x:
            self.removeDepois(p)
        else:
            print(f'elemento nao encontrado')
    
    def obtemListaDisciplina(self,rgm):
      
      p = self.inicio
      
      while p:
      
        if p.getRgm() == rgm:
          return p.disciplina
        
        p = p.proximo

      return None

    def cadastraDisciplina(self,rgm,codigo,nomeDisciplina,frequencia,nota):
      l = self.obtemListaDisciplina(rgm)
      
      if l:
        l.insereDisciplina(codigo,nomeDisciplina,frequencia,nota)
      
      else:
        print('Aluno nao encontrado')
    
    

class ListaAluno:
    
    def __init__(self,rgm,nome,endereco,curso):
            self.rgm = rgm
            self.nome = nome
            self.endereco = endereco
            self.curso = curso
            self.proximo = None
            self.disciplina = ListaLigadaDisciplina()
    
    def getRgm(self):
        return self.rgm

    def setRgm(self,rgm):
        self.rgm = rgm

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome = nome

    def getEndereco(self):
        return self.endereco

    def setEndereco(self,endereco):
        self.endereco = endereco

    def getCurso(self):
        return self.curso

    def setCurso(self,curso):
        self.curso = curso

    def getProximo(self):
        return self.proximo

    def setProximo(self,proximo):
        self.proximo = proximo

class ListaLigadaAluno:

    def __init__(self):
        self.inicio = None

    def insereInicio(self,rgm,nome,endereco,curso):
        
        no = ListaAluno(rgm,nome,endereco,curso)
        no.proximo = self.inicio
        self.inicio = no

    def removeInicio(self):
        
        aux = self.inicio
        if aux:
            self.inicio = aux.getProximo()

    def existeElemento(self,x):
        
        p = self.inicio
        encontrou = False
        while p and not encontrou:
            if x == p.getRgm():
                encontrou = True
            p = p.getProximo()


        return print(encontrou)
    
    def mostraLista(self):
        
        atual = self.inicio
        
        while atual:
            print(f'''
                    **********************************              
                    RGM: {atual.getRgm()}
                    Nome: {atual.getNome()}
                    Endereco: {atual.getEndereco()}
                    Curso: {atual.getCurso()}
                    ''')
            
            lista_Disciplina = self.obtemListaDisciplina(atual.getRgm())
            if lista_Disciplina:
                disciplina = lista_Disciplina.inicio
                while disciplina:
                    print(f'''
                    {disciplina.mostraListaDisciplina()}
                    ***************************
                    ''')
                    break

            atual = atual.getProximo()  

    def contaAlunosLista(self):
        
        atual = self.inicio
        cont = 0
        while atual:
            cont = cont+1
            atual = atual.getProximo()

        return print(f'Quantidade de alunos cadastrados: {cont}')


    def insereUltimo(self,rgm,nome,endereco,curso):
        
        atual = self.inicio
        if not atual:
            self.insereInicio(rgm,nome,endereco,curso)
            return
        
        while atual.getProximo():
            atual = atual.getProximo()
        
        no = ListaAluno(rgm,nome,endereco,curso)
        atual.setProximo(no)

    def removeUltimo(self):
        
        p = None
        q = self.inicio
        
        if not q:
            print(f'lista vazia')
            return

        while q.getProximo():
            p = q
            q = q.getProximo()

        if p == None:
            self.inicio = None
        
        else:
            p.setProximo(None)

    def insereDepois(self,p,rgm,nome,endereco,curso):
        
        no = ListaAluno(rgm,nome,endereco,curso)
        no.setProximo(p.getProximo())
        p.setProximo(no)

    def removeDepois(self,p):
        
        aux = p.getProximo()
        p.setProximo(aux.getProximo())


    def insereOrdenado(self,rgm,nome,endereco,curso):
        
        p = self.inicio
        if not p or rgm < p.getRgm():
            self.insereInicio(rgm,nome,endereco,curso)
            return
        q = p

        while q and q.getRgm() < rgm:
            p = q
            q = q.getProximo()

        if not q or q.getRgm() > rgm:
            self.insereDepois(p,rgm,nome,endereco,curso)
        
        else:
            print(f'Elemento anteriormente cadastrado')

    def removeOrdenado(self,rgm):
        
        p = self.inicio
        
        if not p:
            print(f'lista vazia')
            return

        if p.getRgm() == rgm:
            self.removeInicio()
            return

        q = p
        
        while q and q.getRgm() < rgm:
            p = q
            q = q.getProximo()

        if q and q.getRgm() == rgm:
            self.removeDepois(p)
        
        else:
            print(f'elemento nao encontrado')

    def obtemListaDisciplina(self,rgm):
      
      p = self.inicio
      
      while p:
      
        if p.getRgm() == rgm:
          return p.disciplina
        
        p = p.proximo

      return None

    def cadastraDisciplina(self,rgm,codigo,nomeDisciplina,frequencia,nota):
      l = self.obtemListaDisciplina(rgm)
      
      if l:
        l.insereDisciplina(codigo,nomeDisciplina,frequencia,nota)
      
      else:
        print('Aluno nao encontrado')


lista = ListaLigadaAluno()
lista.insereInicio(1213,'Alef', 'Maximo marson, 3329','Computacao')
lista.cadastraDisciplina(1213,12,'Computacao',50,6)
lista.insereInicio(1414,'Brunno','Franca','Engenharia')
lista.cadastraDisciplina(1414,15,'Matematica',62,9)
lista.insereInicio(1555,'Pedro', 'Elidio Duque', 'Matematica')
lista.cadastraDisciplina(1555,77,'Calculos',50,10)
#lista.removeInicio()
lista.mostraLista()
print('*'*50)
lista.existeElemento(1414)
print('*'*50)
lista.contaAlunosLista()
print('*'*50)
#lista.insereUltimo(1318,'Joao','Jk limeira','Medicina')
#lista.cadastraDisciplina(1318,88,'Anatomia',98,8)