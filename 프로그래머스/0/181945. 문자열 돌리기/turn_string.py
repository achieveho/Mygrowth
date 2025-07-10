# 첫 번째 방법
print('\n'.join(input()))


# 두 번째 방법
for i in input():
    print(i)


# 세 번째 방법
print(* [x for x in input()], sep = '\n')