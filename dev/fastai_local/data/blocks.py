#AUTOGENERATED! DO NOT EDIT! File to edit: dev/_07_data_blocks.ipynb (unless otherwise specified).

__all__ = ['TfmList']

class TfmList():
    def __init__(self, ttfms, tfm=noop):
        self.activ,self.ttfms = False,[Transforms(tfm) for tfm in listify(ttfms)]

    def __call__(self, o, **kwargs):
        if self.activ: return self.activ(o, **kwargs)
        return [t(o, **kwargs) for t in self.ttfms]

    def decode(self, o, **kwargs): return [t.decode(p, **kwargs) for p,t in zip(o,self.ttfms)]

    def setup(self, o):
        for tfm in self.ttfms:
            self.activ = tfm
            tfm.setup(o)
        self.activ=None

    def show(self, o, **kwargs): return show_xs(o, self.ttfms, **kwargs)
    def __repr__(self): return f'TfmList({self.ttfms})'

    @property
    def xt(self): return self.ttfms[0]
    @property
    def yt(self): return self.ttfms[1]