# 1. 거스름돈 문제: 500,100,50,10원으로 거스름돈을 남겨줄 수 있을 때, 가장 적은 개수의 동전으로 거스름돈을 남겨주려면 동전이 몇개 필요한가?
change = int(input(">> "))
coin = [500,100,50,10]  # 거스름돈 동전 리스트
num = 0
for i in coin:
  num += change//i  # 500,100,50,10원 순으로 나누어 몫을 num에 더함
  change %= i
print(num)