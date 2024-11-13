#再帰的解法
# dp[S] 全体集合{0, 1, ..., n-1}の部分集合Sについて、その中のその中の
# The main idea is that you use bit for representing S by bit {1,0,1,...}
# , the bit indicates the element is included in S or not.
# N桁のbitとSが一対一対応