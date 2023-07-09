n,m=map(int, input().split())
truth_man = set(list((map(int, input().split())))[1:]) #진실을 아는 진실맨들 집합
party_people=[] #파티 참여자들
for _ in range(m):
    party_people.append(set(list((map(int, input().split())))[1:]))


for i in party_people: #파티 참여자들 중에서
    if i & truth_man: #진실맨 구성원이 있다면
        truth = truth.union(i) #해당 파티 참여자는 모두 진실맨이 됨

lie=0
for i in party_people:
    if i & truth_man:
        continue
    else:
        lie+=1
print(lie)