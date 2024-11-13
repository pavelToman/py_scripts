a = [
    ('aaa', '111', {
        'ch': 'AAA',
    }),
    ('bbb', '222', {
        'ch': 'BBB',
    }),
    ('ccc', '333', {
        'ch': 'CCC',
    }),
]

b = [x for (x, *y) in a]  # ['aaa', 'bbb', 'ccc']
c = [y for (x, *y) in a]  # [['111', {'ch': 'AAA'}], ['222', {'ch': 'BBB'}], ['333', {'ch': 'CCC'}]]
print(b)
print(c)

