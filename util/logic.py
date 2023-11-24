# .LOGIC
# q0] SCAN (0,q0), (1,q1), (1,accept)
# q1] SCAN (0,q0), (1,q2)
# q2] SCAN (0,q0), (1,q1), (1,accept)

# .LOGIC
# A] SCAN RIGHT (0,A), (1,B), (#,accept)
# B] SCAN LEFT (0,C), (1,reject)
# C] SCAN RIGHT (1,A)

# .DATA
# STACK S1
# .LOGIC
# A] WRITE(S1) (#,B)
# B] SCAN (0,C), (1,D)
# C] WRITE(S1) (#,B)
# D] READ(S1) (#,E)
# E] SCAN (1,D), (#,F)
# F] READ(S1) (#,accept)