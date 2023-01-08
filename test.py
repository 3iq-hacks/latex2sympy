from latex2sympy2 import latex2sympyStr


def main():
    testList = [
        r"0",
        r"1",
        r"5-3",
        r"x^2",
        r"2x",
        r"a \cdot b",
        r"a \div b",
        r"a^2 + b^2 = c^2",
        r"\artanh(a)",
        r"\operatorname{ceil}(b)",
        r"\operatorname{arcsinh}(a)",
        r"\operatorname{arccosh}(a)",
        r"\operatorname{arctanh}(a)",
        r"\operatorname{arsinh}(a)",
        r"\operatorname{arcosh}(a)",
        r"\operatorname{artanh}(a)",
        r"\operatorname{gcd}(a, b)",
        r"\operatorname{lcm}(a, b)",
        r"\operatorname{gcd}(a,b)",
        r"\operatorname{lcm}(a,b)",
        r"\operatorname{floor}(a)",
        r"\frac{d}{dx} x",
        r"||x||",
        r"\int^b_a x dx",
        r"\ln x",
        r"aX^2 + bX + c",
        r'(4a)X^2 + (4a + 2b)X + (a + b + c)',
        "5!7!",
        "x < y", 
        r'a - b - c - d',
        "T(X) = a = b = 2x+1",
        r"\mathbb{R}^N",
        r'''
    \begin{pmatrix}
        1 & 2 & 3 \\ 
        4 & 5 & 6 \\
        7 & 8 & 9 \\ 
    \end{pmatrix}
''',
 r"a * b + c * d + e * c * d",
 r'''\lim_{n\to3} \exp(-(n+1)^n)''',
 r'''+d*3''',
 r"\sum_{n=1}^{\infty} 2^{-n} = 1",
 r'''(n*(n + 1) + n + 2 + 3 + 4 + 5)''',
 r"T(X) = 2X + 1 = 1(1) + 2(X) + 0(X^2)"
    ]
    for tex in testList:
        math = latex2sympyStr(tex)
        print(tex, math)

main()