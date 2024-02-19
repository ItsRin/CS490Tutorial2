import numpy as np
import matplotlib.pyplot as plt

# Activity I: Loading the Denial-of-Service.csv file and checking entries
data_table = np.genfromtxt('Denial-of-Service.csv', dtype=None, delimiter=',', names=True, encoding='utf-8-sig')
print('The header is', data_table.dtype.names)

# Activity II: Creating a subset based on conditions (label = 0, port number = 2, flows = 3)
crude_subset_malign = []
for each_attack in data_table:
    if each_attack['label'] == 0 and each_attack['port_no'] == 2 and each_attack['flows'] == 3:
        crude_subset_malign.append(each_attack)

# Activity III: Creating a subset using a semi-fancy way with conditions (label = 0, port number = 2, flows = 3)
from collections import Counter
truth_array_malign = [(each_attack['label'] == 0 and each_attack['port_no'] == 2 and each_attack['flows'] == 3) for each_attack in data_table]
print(dict(Counter(truth_array_malign)))

# Activity IV: Creating a subset with numpy.where() where dt = 11335 and label = 1
good_subset = data_table[np.where((data_table['dt'] == 11335) & (data_table['label'] == 1))]
print('Number of rows in this subset:', len(good_subset))

# ASSESSMENT TASK-II: Graphing 1D Data
# Creating a subset where the label is not equal to 1 and port num is not equal to 3
not_attack_subset = data_table[np.where((data_table['label'] != 1) & (data_table['port_no'] != 3))]

# Generating a histogram of the (rx bytes - tx kbps) color distribution for these attacks
fig = plt.figure()
plt.hist(not_attack_subset['rx_bytes'] - not_attack_subset['tx_kbps'], bins=5)
plt.show()  # This will display the plot.

# Refining the Histogram Figure Visualization
fig = plt.figure()
plt.hist(not_attack_subset['rx_bytes'] - not_attack_subset['tx_kbps'], bins=50, color='red', histtype='step', label='no attack')
plt.xlabel('(rx_bytes - tx_kbps) color')
plt.show()

# Final tweaks for a more professional histogram figure
fig = plt.figure(figsize=(8, 6))
plt.hist(not_attack_subset['rx_bytes'] - not_attack_subset['tx_kbps'], bins=50, color='blue', histtype='step', label='no attack')
plt.yticks([10, 20, 30, 40, 50], fontsize=28)
plt.xlabel('(rx_bytes - tx_kbps) color', fontsize=28)
plt.ylabel('Number', fontsize=28)
plt.legend(loc=1, fontsize=18)
# Save the figure before showing it to prevent a blank image
plt.tight_layout()  # Compact layout for the figure.
plt.savefig('no_attack.png', format='png', bbox_inches='tight')  # Saves figure to an output image file.
plt.show()  # Now display the plot.
