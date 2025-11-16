NUM = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'ninteen']
DECINE = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety']
BASI = (
    (1e9, 'billion'),
    (1e6, 'million'),
    (1e3, 'thousand'),
    (1e2, 'hundred'),
)

def say(num):
    res = []
    if not 0 <= num < 1e12:
        raise ValueError('input out of range')
    if num == 0:
        return NUM[num]

    for base, name in BASI:
        if num >= base:
            res.append(say(int(num // base)))
            res.append(name)
            num = int(num % base)

    out = ''
    if num >= 20:
        out += DECINE[num // 10]
        num = int(num % 10)
        if num:
            out += '-'
    if num and num < 20:
        out += NUM[num]
    if out:
        res.append(out)

    return ' '.join(res)
