#bit flag
# a番目のフラグが立っている 1 << a-1
a = 3
print(bin(1 << a-1))
# 複数のフラグ管理 | で結合
a = 3
b = 5
c = 9
flag = 1 << a-1 | 1 << b-1  | 1 << c-1
# flag |= 1 << i-1, i番目のフラグを立てる
#マスクでまとめてフラグを立てる
flag |= 100010100
# フラグを消す時は
flag &= ~(1 << a-1)

print(bin(flag))

if(1<<a-1 & flag):
    # or if (1 & flag >> a-1)
    print(a)
if(1<<b-1 & flag):
    print(b)
if(1 & flag>>c-1):
    print(c)


flag = 0b11010001
#マスクによる複数フラグの削除
mask = 0b11100111
flag &= ~mask

#マスクでフラグを立てる
flag |= mask

# mask部分のみの情報をとる
print(flag & mask)

# いずれかのフラグ
bool(flag & mask)

#マスク全てでフラグが立っているか
bool((flag & mask) == mask)

