# Create by Packetsss
# Personal use is allowed
# Commercial use is prohibited

num = 14

ct = 0
while num != 0:
    if num % 2 == 0:
        num /= 2
    else:
        num -= 1
    ct += 1
print(ct)
