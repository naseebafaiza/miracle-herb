import numpy as np


dealer_a_wins = np.array([34, 34, 88, 80, 40, 45, 55, 55, 35, 49])
dealer_b_wins = np.array([56, 90, 42, 46, 48, 35, 46, 45, 29, 49])
dealer_c_wins = np.array([30, 32, 36, 42, 43, 36, 45, 45, 48, 45])

# Pearson correlation coefficient
correlation_ab = np.corrcoef(dealer_a_wins, dealer_b_wins)[0, 1]
correlation_ac = np.corrcoef(dealer_a_wins, dealer_c_wins)[0, 1]
correlation_bc = np.corrcoef(dealer_b_wins, dealer_c_wins)[0, 1]

print("Dealer A and Dealer B:", correlation_ab)
print("Dealer A and Dealer C:", correlation_ac)
print("Dealer B and Dealer C:", correlation_bc)
