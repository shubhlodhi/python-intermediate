from collections import Counter

# team mamber sets 

def smallest_set(start, end, c):
    d = {}
    d[start - 1] = []
    for i in range(start, end + 1):
        d[i] = []
        prev_len = len(d[i-1])
        new_lists = c[i] - prev_len
        if new_lists > 0:
            d[i] = [1]*new_lists
        if prev_len > 0:
            num_appends = min(prev_len, new_lists + prev_len)
            d[i-1].sort()
            d[i] += [x+1 for x in d[i-1][:num_appends]]
            d[i-1] = d[i-1][num_appends:]
    ans = d[end][0]
    for i in range(start, end + 1):
        if len(d[i]) > 0:
            ans = min(ans, min(d[i]))
            if ans == 1:
                return 1
            
    return ans

def find_lowest_range(l, n):
    c = Counter(l)
    i = 0
    mini = n
    while i < len(l):
        end = i
        while end < n and (l[i] == l[end] or (l[end] - l[end - 1]) <= 1):
            end += 1
        end -= 1
        if end == i:
            return 1
        mini = min(mini, smallest_set(l[i], l[end], c))
        if mini == 1:
            return 1
        i = end + 1
    return mini

t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    if l[0] == 0:
        print(0)
        continue
    n = l[3]    
    l = sorted(l[1:])
    print(find_lowest_range(l, n))

#     For two strings A and B, we define the similarity of the strings to be the length of the longest prefix common to both strings. For example, the similarity of strings "abc" and "abd" is 2, while the similarity of strings "aaa" and "aaab" is 3.

# Calculate the sum of similarities of a string S with each of it's suffixes.

# Input Format

# The first line contains the number of test cases t.
# Each of the next t lines contains a string to process, .

# Constraints

#  is composed of characters in the range ascii[a-z]
# Output Format

# Output t lines, each containing the answer for the corresponding test case.

# Sample Input

# 2
# ababaa  
# aa
# Sample Output

# 11  
# 3
# Explanation

# For the first case, the suffixes of the string are "ababaa", "babaa", "abaa", "baa", "aa" and "a". The similarities of these strings with the string "ababaa" are 6,0,3,0,1, & 1 respectively. Thus, the answer is 6 + 0 + 3 + 0 + 1 + 1 = 11.

# For the second case, the answer is 2 + 1 = 3.
def z(w, T):
    T.append(len(w))
    l = r = 0
    for i in range(1, len(w)):
        k = 0
        if i < r:
            k = min(r-i, T[i-l])
        while i+k<len(w) and w[i+k] == w[k]:
            k += 1
        T.append(k)
        if i+k > r:
            l = i
            r = i+k

N = int(input())
for i in range(N):
    curr = input()
    count = 0
    T = []
    z(curr, T)
    for j in range(len(T)):
        count += T[j]
    print(count)