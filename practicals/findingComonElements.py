Rahulguest = input().split()
Priyaguest = input().split()

commonguest = set(Rahulguest) & set(Priyaguest)

sortedcommon = sorted(commonguest)

print(sortedcommon)