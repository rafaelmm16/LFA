# -*- coding: utf-8 -*-

import sys
from abc import ABC, abstractmethod
class Analisador(ABC):
        
    def __init__(self):
        
        self.NOME_DEFAULT_ARQUIVO_ENTRADA = 'entrada.txt'
        self.tokens = {
            
            
            'INT': ['0','1','2','3','4','5','6','7','8','9','<INT>'], 
            'APAR': ['(', '<APAR>'],
            'FPAR': [')','<FPAR>'],
            'ACHAVE': ['{', '<ACHAVE>'],
            'FCHAVE': ['}', '<FCHAVE>'],
            'ACOL': ['[', '<ACOL>'],
            'FCOL': [']', '<FCOL>'],
            'OPER': ['+', '-', '*', '/', '<OPER>' ],
            'IDENT': ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z', '<IDENT>'],
            'EOF': ''
        }
    
    @abstractmethod
    def Analisador(self, _nomeArquivoEntrada):
        self.nomeArquivoEntrada = self._nomeArquivoEntrada
    
    def Analisador(self):
        self.nomeArquivoEntrada = self.NOME_DEFAULT_ARQUIVO_ENTRADA

class AnalisadorLexico(Analisador):
    
    def __init__(self,_nomeArquivoEntrada):
        super().__init__()
        self.proxCaractere = ''
        self.linha = 1
        self.posicao = -1
        self.tokenReconhecido = ''
        self.s = []
        self.entrada = ''
        try:
            self.file = open(_nomeArquivoEntrada, "r")
            self.entrada = self.file.read()
            self.file.close()
            self.leProxCaractere()
            
        except:
            print("Erro na leitura do arquivo" + _nomeArquivoEntrada)
    
    
    def leProxCaractere(self):
        
        try: 
           
            self.posicao += 1  
            self.proxCaractere = self.entrada[self.posicao]
            
            
        except IndexError:
            
            self.proxCaractere = '<EXIT>'
            
    def proxCaractereIs(self, s):
        
        if self.proxCaractere in s:
            return True
        else:
            return False
    
class MyAnalisadorLexico(AnalisadorLexico):
    
    def __init__(self,_nomeArquivoEntrada):
         super().__init__(_nomeArquivoEntrada)
         
    def s0(self):
        if(self.proxCaractereIs(self.tokens['INT'])): 
            self.leProxCaractere()
            self.s1()
        
        elif(self.proxCaractereIs(self.tokens['APAR'])): 
            self.leProxCaractere()
            self.s2()
        
        elif(self.proxCaractereIs(self.tokens['FPAR'])): 
            self.leProxCaractere()
            self.s3()
        
        elif(self.proxCaractereIs(self.tokens['ACHAVE'])): 
            self.leProxCaractere()
            self.s4()
            
        elif(self.proxCaractereIs(self.tokens['FCHAVE'])): 
            self.leProxCaractere()
            self.s5()
            
        elif(self.proxCaractereIs(self.tokens['ACOL'])): 
            self.leProxCaractere()
            self.s6()
            
        elif(self.proxCaractereIs(self.tokens['FCOL'])): 
            self.leProxCaractere()
            self.s7()
            
        elif(self.proxCaractereIs(self.tokens['OPER'])): 
            self.leProxCaractere()
            self.s8()
        
        elif(self.proxCaractereIs(self.tokens['EOF'])): 
            self.leProxCaractere()
            self.s10()

        elif(self.proxCaractereIs(self.tokens['IDENT'])): 
            self.leProxCaractere()
            self.s9()
        
        else:
            if(self.proxCaractere == '<EXIT>'):
               sys.exit() 
               
            print('\nErro léxico: caractere encontrado:'+self.proxCaractere)
            print('era(m) esperados(s):')
            print(self.tokens)
            
            self.leProxCaractere()
            
            self.s0()
            
    def s1(self):
        
        self.tokenReconhecido = '<INT>'  
        
        if(self.proxCaractereIs(self.tokens['INT'])):
            self.leProxCaractere()
            self.s1()
   
    def s2(self):
        
        self.tokenReconhecido = '<APAR>'
        
        if(self.proxCaractereIs(self.tokens['APAR'])):
          
            self.leProxCaractere()
            self.s2()
    
    def s3(self):
        
        self.tokenReconhecido = '<FPAR>'
        
        if(self.proxCaractereIs(self.tokens['FPAR'])):
            
            self.leProxCaractere()
            self.s3()
            
    def s4(self):
        
        self.tokenReconhecido = '<ACHAVE>'
        
        if(self.proxCaractereIs(self.tokens['ACHAVE'])):
            
            self.leProxCaractere()
            self.s4()
            
    def s5(self):
        
        self.tokenReconhecido = '<FCHAVE>'
        
        if(self.proxCaractereIs(self.tokens['FCHAVE'])):
            
            self.leProxCaractere()
            self.s5()
            
    def s6(self):
        
        self.tokenReconhecido = '<ACOL>'
        
        if(self.proxCaractereIs(self.tokens['ACOL'])):
            
            self.leProxCaractere()
            self.s6()
            
    def s7(self):
        
        self.tokenReconhecido = '<FCOL>'
        
        if(self.proxCaractereIs(self.tokens['FCOL'])):
            
            self.leProxCaractere()
            self.s7()
            
    def s8(self):
        
        self.tokenReconhecido = '<OPER>'  
        
        if(self.proxCaractereIs(self.tokens['OPER'])):
            self.leProxCaractere()
            self.s8()

    def s9(self):
        
        self.tokenReconhecido = '<IDENT>'  
        
        if(self.proxCaractereIs(self.tokens['IDENT'])):
            self.leProxCaractere()
            self.s9()   
            
    def s10(self):
        
        self.tokenReconhecido = ''  
        

            
class AnalisadorSintatico(Analisador):            
       
    def __init__(self, _nomeArquivoEntrada):
        self.t = []
        self.A = MyAnalisadorLexico(_nomeArquivoEntrada)
        super().__init__()
        self.leProxToken()
    
    def leProxToken(self):
        self.A.s0()
        
    def reconhece(self, t):
        
        if  self.A.tokenReconhecido in t:
            self.leProxToken()
        else:
            print('\nErro Sintático: token encontrado:' +  self.A.tokenReconhecido)
            print('era(m) esperados(s):' , end = '')
            print(t)
            
    def proxTokenIs(self, t):
        
        if self.A.tokenReconhecido in t:
            return True
        else:
            return False

class MyAnalisadorSintatico(AnalisadorSintatico):            
    def __init__(self,_nomeArquivoEntrada):
         
         self.A = AnalisadorSintatico(_nomeArquivoEntrada)
         
         super().__init__(_nomeArquivoEntrada)
    def inicio(self):
        self.corpo()
    
    def corpo(self):
        
        if (self.proxTokenIs(self.A.tokens['EOF'])):
            print('\nAnalise Sintática: Concluída')
        else:
            print('\nErro Sintático: token encontrado:'+  self.A.tokenReconhecido)
            print('era(m) esperados(s): ',end='')
            
            

    def exp(self):
        
        if (self.proxTokenIs(self.tokens['INT'])):
            self.leProxToken()
            if (self.proxTokenIs(self.tokens['OPER'])):
                self.leProxToken()
                self.exp()
        elif (self.proxTokenIs(self.tokens['INT'])):
            self.leProxToken()
        elif (self.proxTokenIs(self.tokens['VAZIO'])):
            self.leProxToken()
            
        else:
            print('\nErro Sintático: token encontrado:'+  self.A.tokenReconhecido)
            print('era(m) esperados(s):', end = '')
            print( self.t)

    def bloco(self):
        self.exp()

    
    
    def cmdSwitchCase(self):
        self.reconhece(self.tokens['INT'])
        self.bloco()


#Main
A = MyAnalisadorLexico('file.txt')

while True:
     A.s0()
     print(A.tokenReconhecido, end='')

     if A.proxCaractere == '<EXIT>':
         break

 

tst = MyAnalisadorSintatico('file.txt')
tst.inicio()
print('Analise concluída com sucesso')
