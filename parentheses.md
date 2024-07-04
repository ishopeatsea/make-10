# working out how much equivalence there is in "all possible orderings"

## all bracket configurations with digits 'abc' and operators '+' and all orderings
> note: + is order agnostic

### all possible orderings:
- abc
    - (a+b)+c
    - a+(b+c)
- acb
    - (a+c)+b
    - a+(c+b)
- bac
    - (b+a)+c
    - b+(a+c)
- bca
    - (b+c)+a
    - b+(c+a)
- cab
    - (c+a)+b
    - c+(a+b)
- cba
    - (c+b)+a
    - c+(b+a)

### equivalent orderings:

x+y = y+x for all x,y

### total unique orderings:

1. a+b+c

## all bracket configurations with digits 'abc' and operators '+×' and all orderings
> note: + and × are order agnostic

### all possible orderings:

- abc
    - +×
        - (a+b)×c
        - a+(b×c)
    - ×+
        - (a×b)+c
        - a×(b+c)
- acb
    - +×
        - (a+c)×b
        - a+(c×b)
    - ×+
        - (a×c)+b
        - a×(c+b)
- bac
    - +×
        - (b+a)×c
        - b+(a×c)
    - ×+
        - (b×a)+c
        - b×(a+c)
- bca
    - +×
        - (b+c)×a
        - b+(c×a)
    - ×+
        - (b×c)+a
        - b×(c+a)
- cab
    - +×
        - (c+a)×b
        - c+(a×b)
    - ×+
        - (c×a)+b
        - c×(a+b)
- cba
    - +×
        - (c+b)×a
        - c+(b×a)
    - ×+
        - (c×b)+a
        - c×(b+a)

### equivalent orderings:

x+y = y+x for all x,y
xy = yx for all x,y

### total unique orderings:

1) c(a+b)
2) bc+a
3) b(a+c)
4) ac+b
5) a(b+c)
6) ab+c

## all bracket configurations with digits 'abc' and operators '-' and all orderings
> note: - is left associative















all possible orderings of abcd:
- abcd
- abdc
- acbd
- acdb
- adbc
- adcb
- bacd
- badc
- bcad
- bcda
- bdac
- bdca
- cabd
- cadb
- cbad
- cbda
- cdab
- cdba
- dabc
- dacb
- dbac
- dbca
- dcab
- dcba
