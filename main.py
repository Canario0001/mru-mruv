#!/usr/bin/env python3
err = None
from math import sqrt

class Mru:
    def __init__(self, v, t, s, so, ds):
        # v → velocidade
        # t → tempo
        # s → posição final
        # so → posição inicial
        # ds → deslocamento (variação da posição)
        self.v = v
        self.t = t
        self.s = s
        self.so = so
        self.ds = ds

    @classmethod
    def lista(cls):
        print('\n\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
        print('v: Velocidade (m/s)\nt: Tempo (s)\ns: Posição final (m)\nso: Posição inicial (m)\nds: Deslocamento (ΔS) (m)')

    @classmethod
    def anotar(cls, nome, resultado):
        texto = f'Resultados\n\nVelocidade: {resultado["v"]} m/s\nTempo: {resultado["t"]} s\nPosição final: {resultado["s"]} m\nPosição inicial: {resultado["so"]} m\nDeslocamento: {resultado["ds"]} m'
        with open(f'{nome}.txt', 'w') as f: f.write(texto)

    def solve(self): # calcula tudo de uma vez
        for _ in range(2):
            self._ve()
            self._te()
            self._sf()
            self._sini()
            self._des()

        result = {
            'v': self.v,
            't': self.t,
            's': self.s,
            'so': self.so,
            'ds': self.ds
        }

        return result

    def _ve(self):
        if not self.v:
            try:
                self.v = (self.s - self.so) / self.t
            except (ValueError, TypeError):
                try:
                    self.v = self.ds / self.t
                except (ValueError, TypeError):
                    self.v = err

    def _te(self):
        if not self.t:
            try:
                self.t = (self.s - self.so)/self.v
            except (ValueError, TypeError):
                try:
                    self.t = self.ds / self.v
                except (ValueError, TypeError):
                    self.t = err
    
    def _sf(self):
        if not self.s:
            try:
                self.s = self.so + self.v * self.t
            except (ValueError, TypeError):
                try:
                    self.s = self.ds + self.so
                except (ValueError, TypeError):
                    self.s = err

    def _sini(self):
        if not self.so:
            try:
                self.so = self.s - (self.v * self.t)
            except (ValueError, TypeError):
                try:
                    self.so = self.s - self.ds
                except (ValueError, TypeError):
                    self.so = err

    def _des(self):
        if not self.ds:
            try:
                self.ds = self.s - self.so
            except (ValueError, TypeError):
                try:
                    self.ds = self.v * self.t
                except (ValueError, TypeError):
                    self.ds = err

class Mruv:
    def __init__(self, a, dv, t, v, vo, s, so, ds):
        # a → aceleração
        # dv → variação da velocidade
        # t → tempo
        # v → velocidade final
        # vo → velocidade inicial
        # s → posição final
        # so → posição inicial
        # ds → deslocamento (variação da posição)
        self.a = a
        self.dv = dv
        self.t = t
        self.v = v
        self.vo = vo
        self.s = s
        self.so = so
        self.ds = ds

    @classmethod
    def lista(cls):
        print('\n\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
        print('a: Aceleração (m/s²)\ndv: Variação da velocidade (ΔV) (m/s)\nt: Tempo \nv: Velocidade final (m/s)\nvo: Velocidade inicial (m/s)\ns: Posição final (m)\nso: Posição inicial (m)\nds: Deslocamento (ΔS) (m)')

    @classmethod
    def anotar(cls, nome, resultado):
        texto = f'Resultados\n\nAceleração: {resultado["a"]} m/s²\nVariação da velocidade: {resultado["dv"]} m/s\nTempo: {resultado["t"]} s\nVelocidade final: {resultado["v"]} m/s\nVelocidade inicial: {resultado["vo"]} m/s\nPosição final: {resultado["s"]} m\nPosição inicial: {resultado["so"]} m\nDeslocamento: {resultado["ds"]} m'
        with open(f'{nome}.txt', 'w') as f: f.write(texto)
    
    def solve(self): # calcula tudo
        for _ in range(2):
            self._ac()
            self._dev()
            self._te()
            self._vf()
            self._vi()
            self._sf()
            self._sini()
            self._des()

        result = {
            'a': self.a,
            'dv': self.dv,
            't': self.t,
            'v': self.v,
            'vo': self.vo,
            's': self.s,
            'so': self.so,
            'ds': self.ds
        }

        return result

    def _ac(self):
        if not self.a:
            try:
                self.a = self.ds / self.t
            except (ValueError, TypeError):
                try:
                    self.a = (self.v - self.vo) / self.t
                except (ValueError, TypeError):
                    try:
                        self.a = 2 * ( (self.s - self.so) / self.t - self.v) / self.t
                    except (ValueError, TypeError):
                        try:
                            self.a = 2 * (self.ds / self.t - self.v) / self.t
                        except (ValueError, TypeError):
                            try:
                                self.a = ( (self.v + self.vo) * (self.v - self.vo) ) / (2 * (self.s - self.so) )
                            except (ValueError, TypeError):
                                try:
                                    self.a = ( (self.v + self.vo) * (self.v - self.vo) ) / (2 * self.ds )
                                except (ValueError, TypeError):
                                    self.a = err
    
    def _dev(self):
        if not self.dv:
            try:
                self.dv = self.v - self.vo
            except (ValueError, TypeError):
                try:
                    self.dv = self.a * self.t
                except (ValueError, TypeError):
                    self.dv = err
    
    def _te(self):
        if not self.t:
            try:
                self.t = self.dv / self.a
            except (ValueError, TypeError):
                try:
                    self.t = (self.v - self.vo) / self.a
                except (ValueError, TypeError):
                    self.t = err
    
    def _vf(self):
        if not self.v:
            try:
                self.v = self.vo + self.a * self.t
            except (ValueError, TypeError):
                try:
                    self.v = sqrt(self.vo ** 2 + 2 * self.a * self.ds)
                except (ValueError, TypeError):
                    try:
                        self.v = sqrt(self.vo ** 2 + 2 * self.a * (self.s - self.so))
                    except (ValueError, TypeError):
                        try:
                            self.v = self.dv + self.vo
                        except (ValueError, TypeError):
                            self.v = err
    
    def _vi(self):
        if not self.vo:
            try:
                self.vo = self.v - self.a * self.t
            except (ValueError, TypeError):
                try:
                    self.vo = (self.ds / self.t) - ( (self.a - self.t)/2 )
                except (ValueError, TypeError):
                    try:
                        self.vo = ((self.s - self.so) / self.t) - ( (self.a - self.t)/2 )
                    except (ValueError, TypeError):
                        try:
                            self.vo = sqrt(self.v ** 2 - 2 * self.a * self.ds)
                        except (ValueError, TypeError):
                            try:
                                self.vo = sqrt(self.v ** 2 - 2 * self.a * (self.s - self.so))
                            except (ValueError, TypeError):
                                try:
                                    self.vo = self.v - self.dv
                                except (ValueError, TypeError):
                                    self.vo = err
    
    def _sf(self):
        if not self.s:
            try:
                self.s = self.so + self.vo * self.t + (self.a * self.t)/2
            except (ValueError, TypeError):
                try:
                    self.s = ((self.v + self.vo) * (self.v - self.vo) / (2 * self.a)) - self.so
                except (ValueError, TypeError):
                    try:
                        self.s = self.ds + self.so
                    except (ValueError, TypeError):
                        self.s = err
    
    def _sini(self):
        if not self.so:
            try:
                self.so = self.s - self.vo * self.t - (self.a * (self.t ** 2))/2
            except (ValueError, TypeError):
                try:
                    self.so = - ((self.v + self.vo) * (self.v + self.vo) / (2 * self.a)) + self.s
                except (ValueError, TypeError):
                    try:
                        self.so = self.ds - self.s
                    except (ValueError, TypeError):
                        self.so = err
    
    def _des(self):
        try:
            self.ds = self.vo * self.t + (self.a * (self.t ** 2))/2
        except (ValueError, TypeError):
            try:
                self.ds = ((self.v + self.vo) * (self.v - self.vo)) / (2 * self.a)
            except (ValueError, TypeError):
                try:
                    self.ds = self.s - self.so
                except (ValueError, TypeError):
                    self.ds = err

def header(num):
    print('┅'*num)

def u():
    print()
    header(50)
    print('  Calculadora de Movimento Retilíneo Uniforme!')
    header(50)
    
    print('\nDeseja ver a lista de abreviações ou quer começar agora?\n')
    print('[0] - Ver a lista de abreviações\n[1] - Começar sem ver a lista\n')
    
    choice = int(input('>>> '))
    if choice == 0: Mru.lista()
    elif choice == 1: pass
    else: print('Insira um valor válido. Tente novamente.'); quit()

    v = None; t = None; s = None; so = None; ds = None
    print('\nDigite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.')
    while True:
        # comp → composto
        comp = input('>>> ').strip().lower()

        if comp == 'q': break

        if comp.startswith('so'):
            _, so = comp.split(':')
            so = float(so)

        elif comp.startswith('s'):
            _, s = comp.split(':')
            s = float(s)

        elif comp.startswith('v'):
            _, v = comp.split(':')
            v = float(v)

        elif comp.startswith('t'):
            _, t = comp.split(':')
            t = float(t)

        elif comp.startswith('ds'):
            _, ds = comp.split(':')
            ds = float(ds)

        else: print('Digite uma informação válida!')

    matemaquina = Mru(v, t, s, so, ds)
    resultado = matemaquina.solve()
    print('\n')
    header(35)
    print('  Resultados')
    header(35)
    print('')
    print(f'  Velocidade: {resultado["v"]} m/s')
    print(f'  Tempo: {resultado["t"]} s')
    print(f'  Posição inicial: {resultado["so"]} m')
    print(f'  Posição final: {resultado["s"]} m')
    print(f'  Deslocamento (ΔS): {resultado["ds"]} m')

    print('\n\nVocê quer escrever os resultados num arquivo de texto?\n\n[0] - Sim\n[1] - Não\n')
    choice = int(input('>>> ').strip())
    if choice == 0:
        print('\nQual será o nome do arquivo?\n')
        nome = input('>>> ').strip()
        Mru.anotar(nome, resultado)
        print(f'\nResultados salvos no arquivo {nome}.txt!')
    elif choice == 1: pass
    else: print('Opção inválida. Operação cancelada.')

    print('\nObrigado por usar!\nFeito por: Canário')

def uv():
    print()
    header(65)
    print('  Calculadora de Movimento Retilíneo Uniformemente Variado!')
    header(65)
    
    print('\nDeseja ver a lista de abreviações ou quer começar agora?\n')
    print('[0] - Ver a lista de abreviações\n[1] - Começar sem ver a lista\n')
    
    choice = int(input('>>> '))
    if choice == 0: Mruv.lista()
    elif choice == 1: pass
    else: print('Insira um valor válido. Tente novamente.'); quit()

    a = None; dv = None; t = None; v = None; vo = None; s = None; so = None; ds = None
    print('\nDigite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.')
    while True:
        # comp → composto
        comp = input('>>> ').strip().lower()

        if comp == 'q': break

        if comp.startswith('a'):
            _, a = comp.split(':')
            a = float(a)

        elif comp.startswith('dv'):
            _, dv = comp.split(':')
            dv = float(dv)

        elif comp.startswith('t'):
            _, t = comp.split(':')
            t = float(t)

        elif comp.startswith('vo'):
            _, vo = comp.split(':')
            vo = float(vo)

        elif comp.startswith('v'):
            _, v = comp.split(':')
            v = float(v)

        elif comp.startswith('so'):
            _, so = comp.split(':')
            so = float(so)

        elif comp.startswith('s'):
            _, s = comp.split(':')
            s = float(s)

        elif comp.startswith('ds'):
            _, ds = comp.split(':')
            ds = float(ds)

        else: print('Digite uma informação válida!')

    matemaquina = Mruv(a, dv, t, v, vo, s, so, ds)
    resultado = matemaquina.solve()
    print('\n')
    header(35)
    print('  Resultados')
    header(35)
    print()
    print(f'  Aceleração: {resultado["a"]} m/s²')
    print(f'  Variação da velocidade (ΔS): {resultado["dv"]} m/s')
    print(f'  Tempo: {resultado["t"]} s')
    print(f'  Velocidade final: {resultado["v"]} m/s')
    print(f'  Velocidade inicial: {resultado["vo"]} m/s')
    print(f'  Posição final: {resultado["so"]} m')
    print(f'  Posição inicial: {resultado["s"]} m')
    print(f'  Deslocamento (ΔS): {resultado["ds"]} m')

    print('\n\nVocê quer escrever os resultados num arquivo de texto?\n\n[0] - Sim\n[1] - Não\n')
    choice = int(input('>>> ').strip())
    if choice == 0:
        print('\nQual será o nome do arquivo?\n')
        nome = input('>>> ').strip()
        Mruv.anotar(nome, resultado)
        print(f'\nResultados salvos no arquivo {nome}.txt!')
    elif choice == 1: pass
    else: print('Opção inválida. Operação cancelada.')

    print('\nObrigado por usar!\nFeito por: Canário')

def main():
    print('Você quer usar a calculadora de MRU ou MRUV?\n')
    print('[0] - MRU\n[1] - MRUV\n')
    op = int(input('>>> '))
    if op == 0: u()
    elif op == 1: uv()
    else: print('Insira um valor válido.')

if __name__ == '__main__':
    main()