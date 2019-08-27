import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5])
y = np.array([4,6,4,5,6,7])
x = np.array([2,3,2,3,2,2])

plt.bar(x,y, label='data 1',
    color=['r','g','b','k','y','r'],
    yerr = 0.5, bottom=y
)
# diagram batang, yerr buat bikin nilai toleransi
plt.title('Diagram Batang')
plt.grid(True)
plt.legend()
plt.show()

## dalam 1 data, ada gabungan cra menampilkan (scatter, bar)
x = np.array([0,1,2,3,4,5])
y = np.array([4,6,4,5,6,7])
x = np.array([2,3,2,3,2,2])

plt.plot(x,y,'r--', zorder=2)
plt.bar(x,y, color='lightblue', zorder=1)
plt.scatter(x,y, label = 'Data 1',color='r',
    maker='$A$', s=200, zorder=3
)
# scatter= diagram grafik berupa titik. zorder=makin kecil angkanya, makin belakang dimunculinnya
plt.title('Diagram scatter')
plt.grid(True)
plt.legend()
plt.show()

##pie chart
import matplotlib.pyplot as plt
import numpy as np

jam = [8,8,6,2]
aktivitas = ['Ngoding','Tidur','Main games','Makan']
warna = ['r','lightpink','pink','light coral']

plt.pie(jam, labels=aktivitas, colors=warna,
    startangle=180,shadow=True,counterclock=False,
    explode=(0,.2,0,0), autopct='%1.1f%%',
    textprops={'color':'w'}
)
# explode=ngatur posisi, kalo 0 tetep. autopct=buat persentase. textprops=buat warna teksnya
plt.grid(True)
plt.legend()
plt.show()

##histogram
import matplotlib.pyplot as plt
import numpy as np

plt.figure('ini histogram', figsized=(6,6))
# figure= gunanya kalo mau bikin beberapa chart

plt.subplot(121)
# artinya ada 1 baris 2 kolom, pada figure 1
usia = [22,23,25,25,24,23,31,32,40,45,45,50,55,55,42]
kategori = [20,30,40,50,60]

plt.hist(usia,kategori, histtype='barstacked',rwidth=.1)

plt.title('histogram 1')
plt.grid(True)
plt.show()

plt.subplot(122)
# artinya ada 1 baris 2 kolom, pada figure 2
usia = [22,23,25,25,24,23,31,32,40,45,45,50,55,55,42]
kategori = [20,30,40,50,60]

plt.hist(usia,kategori, histtype='barstacked',rwidth=.1)

plt.title('histogram 2')
plt.grid(True)
plt.show()

##image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as im 

gbr = im.imread('x.png')
print(gbr.shape)
# ngonvert gambar jadi array

gbrplot=plt.imshow(gbr)
plt.show()
# ngonvert array jadi gambar

##3dplot
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure('ini 3d plot')
ax = plt.subplot(111,projection='3d')

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = x
z = np.array([x]) # 2 dimensi

ax.scatter(x,y,z, color='y',marker='*',s=300)
# bikin scatter


ax.plot_wireframe(x,y,z)
ax.set_xlabel('ini x')
ax.set_ylabel('ini y')
ax.set_zlabel('ini z')

##3dbar
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure('ini 3d plot')
ax = plt.subplot(111,projection='3d')

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = x
z = np.zeros(10)
dx = np.ones(10)
dy = np.ones(10)
dz = x
# dx= lebar batang, dy= panjang batang, dz = tinggi batang(artinya sesuai data)
ax.bar3d(x,y,z,dx,dy,dz,
    color=['r','pink','orange','y','g','lightblue','b','magenta','purple','violet']
)


ax.plot_wireframe(x,y,z)
ax.set_xlabel('ini x')
ax.set_ylabel('ini y')
ax.set_zlabel('ini z')