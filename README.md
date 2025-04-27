Classes:
  Button: botões retangulares que recebem as variaveis (self,ponto1,ponto2,cor,win,text)
  
Funções:
  Button.clicar(self,point):Avalia se o ponto onde se clicou esta dentro do retangulo/botão atráves da expressão (point.getX() <= self.ponto2.getX() or point.getX()<=self.ponto1.getX()) and
  (point.getY() <= self.ponto1.getY() or point.getY()<=self.ponto2.getY())

Varáveis:
  Boato 1,2,3: botões para iniciar as iterações
  x,y : largura e altura da janela respetivamente
  win: Janela
  xmed,ymed: coordenadas do centro dos botoões onde aparece o texto
  
