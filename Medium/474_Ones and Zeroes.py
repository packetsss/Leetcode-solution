# Create by Packetsss
# Personal use is allowed
# Commercial use is prohibited

import numpy as np

def findMaxForm(S, M, N):
    dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    for s in S:
        zeros = s.count("0")
        ones = len(s) - zeros
        # print(f"Zeros: {zeros}, Ones: {ones}")
        for i in range(M, zeros - 1, -1):
            for j in range(N, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                # print(f"Zeros: {zeros}, Ones: {ones}")
                # print(f"i: {i}, j: {j}\n{np.array(dp)}")
    return dp[M][N]


findMaxForm(["10", "0001", "111001", "1", "0"], 4, 3)
