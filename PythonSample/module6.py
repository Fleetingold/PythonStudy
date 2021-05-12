def now():
    print('2015-3-25')

f = now
f()

print(now.__name__)
print(f.__name__)