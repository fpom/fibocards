from collections import defaultdict

class FiboCards (object) :
    """Fibonacci cards generator
    See: https://blogdemaths.wordpress.com/2013/01/13/un-tour-de-magie-mathematique/
    """
    def __init__ (self, stop) :
        "generate cards for numbers 0 < n < stop"
        self.path = f"cards-{stop}.tex"
        self.fibo = tuple(self._fibo(stop))
        self.card = defaultdict(list)
        for n in range(1, stop) :
            for s in self.split(n) :
                self.card[s].append(n)
    def _fibo (self, stop) :
        "generator for Fibonacci numbers"
        a, b = 1, 2
        while a < stop :
            yield a
            a, b = b, a+b
    def split (self, n) :
        "decompose n into a sum of Fibonacci numbers"
        for f in reversed(self.fibo) :
            if f <= n :
                n -= f
                yield f
            if n == 0 :
                break
    def tex (self, path=None, scale=2, colors=["red", "green", "blue"]) :
        "generate a LaTeX file for the cards"
        c = 0
        with open(path or self.path, "w") as tex :
            tex.write(r"""\documentclass[20pt]{beamer}
            \usepackage{xcolor}
            \usepackage{relsize}
            \beamertemplatenavigationsymbolsempty
            \begin{document}
            """)
            for l in self.card.values() :
                tex.write(fr"""\begin{{frame}}[t]
                \relsize{{{scale}}}
                """)
                for i, n in enumerate(l) :
                    if i :
                        tex.write(", ")
                    tex.write(fr"{{\color{{{colors[c % len(colors)]}!50!black}}{n}}}")
                    c += 1
                tex.write(r"""
                \end{frame}

                """)
            tex.write(r"""
            \end{document}
            """)

if __name__ == "__main__" :
    for stop in (30, 40, 50, 60, 80, 100) :
        FiboCards(stop).tex()

