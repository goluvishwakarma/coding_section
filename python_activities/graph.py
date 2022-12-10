import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()
# @title String fields

# text = 'value'  # @param {type:"string"}
# dropdown = '1st option'  # @param ["1st option", "2nd option", "3rd option"]
# text_and_dropdown = 'value'  # @param ["1st option", "2nd option", "3rd option"] {allow-input: true}
#
# print(text)
# print(dropdown)
# print(text_and_dropdown)
#
# # @title Raw fields
#
# raw_input = None  # @param {type:"raw"}
# raw_dropdown = raw_input  # @param [1, "raw_input", "False", "'string'"] {type:"raw"}

print(raw_input)
print(raw_dropdown)
