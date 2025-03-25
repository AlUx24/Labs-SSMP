import re

s = "TheOldSeaDogAtTheAdmiralBenbow"
result = re.findall(r'[A-Z][a-z]*', s)
print(' '.join(result))

# Вхідні дані:
# TheOldSeaDogAtTheAdmiralBenbow
#
# Вихідні дані:
# The Old Sea Dog At The Admiral Benbow
