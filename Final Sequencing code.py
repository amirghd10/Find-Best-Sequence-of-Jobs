import itertools

X = int(input("Enter the number of jobs==> "))

process_times = []
due_dates = []
for i in range(X):
    processtime = int(input(f"Enter processing time of job {i+1}==> "))
    process_times.append(processtime)
for i in range(X):
    duedate = int(input(f"Enter Due date of Job {i+1}==> "))
    due_dates.append(duedate)


x = list(zip(process_times, due_dates))
"""
X=6
x = [(10,15),(3,6),(4,9),(8,23),(10,20),(6,30)]
"""
duedue = []
for i in x:
    duedue.append(i[1])

c = []
s = []


permutations = list(itertools.permutations(x))
perms_list = [list(k) for k in permutations]

for elt in perms_list:  
    for z in elt:        
        c.append(z[0])
        ch = [c[x:x+X] for x in range(0, len(c), X)]

c2 = []
for elt in perms_list:
    for z in elt:
        c2.append(z[1])
        ch2 = [c2[x:x+X] for x in range(0, len(c2), X)]

lastone = []
def completion_time(perms_list):
    dd = []
    for elt in perms_list:
        if len(dd)>0:
            dd.append(dd[-1]+elt)
        else:
            dd.append(elt)
    return dd
for i in ch:
    lastone.append(completion_time(i))

ii = [j for i in ch2 for j in i]
jj = [j for i in lastone for j in i]

lateness = [x1 - x2 for (x1, x2) in zip(jj, ii)]
late = [lateness[x:x+X] for x in range(0, len(lateness), X)]

Lj= []

"""for i in range(len(perms_list)):
    k = []
    for j in ch2[i]:
        k.append(duedue.index(j))
    print("JOBS:             ", k)
    print("DUE DATES:        ", ch2[i])
    print("COMPLETION TIMES: ", lastone[i])
    print("LATENESSES:       ", late[i])
    print("Lmax:             ", max(late[i]))
    print("SUM OF LATENESSES ", sum(late[i]))
    print("AVERAGE LATENESS: ", round(sum(late[i])/X, 2))
    Lj.append(max(late[i]))
    count += 1
    print("Counter: ", count)
    print("*********")
    """
def calcs(perms_list):
    count = 0
    for i in range(len(perms_list)):

        k = []
        for j in ch2[i]:
            k.append(duedue.index(j))
        print("JOBS:             ", k)
        print("DUE DATES:        ", ch2[i])
        print("COMPLETION TIMES: ", lastone[i])
        print("LATENESSES:       ", late[i])
        print("Lmax:             ", max(late[i]))
        print("SUM OF LATENESSES ", sum(late[i]))
        print("AVERAGE LATENESS: ", round(sum(late[i])/X, 2))
        Lj.append((max(late[i]),k))
        count += 1
        print("Counter:          ", count)
        print("*********")

print(calcs(perms_list))

print(min(Lj))

"""near = min(Lj)*0.1 + min(Lj)
o = []

def find(lss):
    
    for j in lss:
        o.append(duedue.index(j))
    
for i in Lj:
    if i < near:      
        print(i)"""


print(input("Press Enter to End > "))