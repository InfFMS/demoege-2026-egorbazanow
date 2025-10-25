#9 задание( не знаю почему он нормально не выводит)
ans = 0
for line in open('DEMO_9.ods'):
    nums = list(map(int, line.split(',')))
    tr = set(x for x in nums if nums.count(x) == 3)
    single = set(x for x in nums if nums.count(x) == 1)
    if len(tr) == 1 and len(single) == 4 and sum(single) / len(single) <= tr.pop():
       ans = sum(nums)
print(ans)