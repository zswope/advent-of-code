def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [0] * (len(s) + 1)  # dp[i] will store the number of ways to construct s[:i]
    dp[0] = 1  # There's one way to construct an empty string: do nothing.

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] > 0 and s[j:i] in word_set:
                dp[i] += dp[j]

    return dp[len(s)]

star1 = 0
star2 = 0
import os
data = open(os.path.basename(__file__).split('.')[0]+'.txt','r').read()
# data = """
# r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb
# """
data = [line.strip() for line in data.split('\n\n') if line.strip()]

# extract data
available = data[0].split(', ')
patterns = data[1].split('\n')

wordBreakRet = [wordBreak(pattern, available) for pattern in patterns]
star1 = sum(map(bool,wordBreakRet))
star2 = sum(wordBreakRet)

print('star1:',star1)
print('star2:',star2)
