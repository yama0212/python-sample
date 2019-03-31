from random import randint

# 分数計算
monk_fish_team = [158, 157, 163, 157, 145]

total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total / length
variance = 0
print(mean)
for height in monk_fish_team:
    variance += (height-mean)**2

variance = variance / length
print(variance)

# range()関数
for cnt in range(10):
    print(cnt)

# if
if 2*2*2+2 == 10:
    print("2*2*2+2")
# 数値比較
if 1 == 1:
    print("1番目はTrue")
# 文字列比較
if "AUG" == "AUG":
    print("1番目はTrue")
# 文字列検索
if "GAG" in "AUGACGGAGCUU":
    print("1番目はTrue")
# リスト比較
if [1, 2, 3, 4] == [1, 2, 3, 4]:
    print("1番目はTrue")
# リスト検索
if 2 in [2, 3, 5, 7, 11]:
    print("1番目はTrue")

# else
if 2^3-2+4 == 10:
    print("式1は10")
else:
    print("式1は10にならない")

# elif
a_year = 2080
if a_year == 1993:
    print(a_year, "年、れに誕生")
elif a_year > 1993:
    print(a_year, "年、れに", a_year-1993, "歳")

# 関数
def destiny_tank(num):
    tanks = ["IV号戦車D型", "III号戦車J型", "チャーチル Mk.VII",
            "M4シャーマン", "P40重戦車", "T-34/76"]
    idx = num % len(tanks)
    return tanks[idx]

num = randint(0, 10)
tank = destiny_tank(num)
print("あなたの運命の戦車は")
print(tank)

# ディクショナリ
purple = {"ニックネーム": "れにちゃん",
        "出身地": "神奈川県",
        "キャッチフレーズ": "感電少女"}
purple["生年月日"] = "1993年6月12日"
print(purple["出身地"])

for key in purple:
    print(key, purple[key])

# SET
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8, 13}

prime_fib = prime | fib
print(prime_fib)
prime - fib
prime & fib

codon = ['ATG', 'GGC', 'TCC', 'AAG', 'TTC', 'TGG', 'GAC', 'TCC']
s_coden = set(codon)
print(len(codon), len(s_coden))

# タプル
month_names = ("January", "February", "March", "April", "May", "June", "July")
print(month_names[1])
# タプルをキーとしたディクショナリの作成
pref_capitals = {(43.06417, 141.34694): "北海道",
                (40.82444, 140.74): "青森県",
                (39.70361, 141.1525): "岩手県"}
loc = (41.768793, 140.72881)
nearest_cap = ''
nearest_dist = 10000
for key in pref_capitals:
    dist = (loc[0]-key[0])**2+(loc[1]-key[1])**2
    if nearest_dist > dist:
        nearest_dist = dist
        nearest_cap = pref_capitals[key]
print(nearest_cap)

# ifの応用
v = 30000
if v < 28400:
    print("地上に落下します")
if v >= 28400 and v < 40300:
    print("月とお友達です")
if v >= 40300 and v < 60100:
    print("惑星の仲間入りです")
if v >= 60100:
    print("アルファ・ケンタウリを目指せ")

# ループの応用
cnt = 1
while cnt <= 100:
    if cnt%3 == 0 and cnt%5 == 0:
        print("FizzBuzz")
    elif cnt%3 == 0:
        print("Fizz")
    elif cnt%5 == 0:
        print("Buzz")
    else:
        print(cnt)
    cnt = cnt + 1

# 関数にデフォルト引数を定義する
def fizzbuzz(count=100, fizzmod=3, buzzmod=5):
    for cnt in range(1, count - 1):
        if cnt%fizzmod == 0 and cnt%buzzmod == 0:
            print("FizzBuzz")
        elif cnt%fizzmod == 0:
            print("Fizz")
        elif cnt%buzzmod == 0:
            print("Buzz")
        else:
            print(cnt)
fizzbuzz()