#!/usr/bin/env python3
err = 'Não foi possível encontrar'

class Mru:
    def __init__(self, v, t, s, so, ds):
        # v → velocidade
        # t → tempo
        # s → posição final
        # so → posição inicial
        # ds → distância (variação da posição)
        self.v = v
        self.t = t
        self.s = s
        self.so = so
        self.ds = ds

    @classmethod
    def lista(cls):
        print('\n\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
        print('v: Velocidade\nt: Tempo\ns: Posição final\nso: Posição inicial\nds: Distância (ΔS)')

    @classmethod
    def anotar(cls, nome, resultado):
        texto = f'Resultados\n\nVelocidade: {resultado["v"]} m/s\nTempo: {resultado["t"]} s\nPosição final: {resultado["s"]} m\nPosição inicial: {resultado["so"]} m\nDistância (ΔS): {resultado["ds"]} m'
        with open(f'{nome}.txt', 'w') as f: f.write(texto)

    def solve(self): # calcula tudo de uma vez
        for _ in range(2):
            self._ve()
            self._te()
            self._sf()
            self._sini()

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
                self.v = (self.s - self.so)/self.t
            except (ValueError, TypeError):
                self.v = err

    def _te(self):
        if not self.t:
            try:
                self.t = (self.s - self.so)/self.v
            except (ValueError, TypeError):
                self.t = err
    
    def _sf(self):
        if not self.s:
            try:
                self.s = self.so + self.v * self.t
            except (ValueError, TypeError):
                self.s = err

    def _sini(self):
        if not self.so:
            try:
                self.so = self.s - (self.v * self.t)
            except (ValueError, TypeError):
                self.so = err

    def _des(self):
        ...

class Mruv:
    def __init__(self):
        pass

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

        elif comp.startswith('so'):
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
    print(f'  Posição inicial: {resultado["s"]} m')
    print(f'  Posição final: {resultado["so"]} m')
    print(f'  Distância (ΔS): {resultado["ds"]} m')

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
    ...

def main():
    print('Você quer usar a calculadora de MRU ou MRUV?\n')
    print('[0] - MRU\n[1] - MRUV\n')
    op = int(input('>>> '))
    if op == 0: u()
    elif op == 1: uv()
    else: print('Insira um valor válido.')


if __name__ == '__main__':
    main()