import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Store_all = []
with open("1qlz.pdb") as protein:
    for lines in protein:
        if "ATOM   " in lines:
            lines = lines.split()
            #'ATOM', '1', 'N', 'LEU', 'A', '125', '4.329', '-12.012', '2.376', '1.00', '0.00', 'N'
            Store_all.append(map(float, lines[6:9]))



x,y,z = zip(*Store_all)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z, "x")
ax.axis("off")

plt.show()