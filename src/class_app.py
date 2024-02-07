class IFruta:
    def rot(self):
        '''Bananinhas and fruits rotten :('''


class Fruta(IFruta):
    def __init__(self, color: str | None = None, prices: list[float] = None) -> None:
        self.color = color or None
        self.prices = prices or []
    def rot(self):
        print('im sad')


bananinha = Fruta(color='Yellow')
surpresa = Fruta()

bananinha.prices.append(2.99)

print(bananinha.prices)
print(surpresa.rot())