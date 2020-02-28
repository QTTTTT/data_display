import re
import numpy as np
import matplotlib.pyplot as plt
import h5py


text = open("/Users/mac/Desktop/ca1_step1_input_data.txt")

#处理字符
line1 = text.readline()
#print(line1)
line2 = text.readline()
#print(line2)
line1 = line1.replace("#","")
line1 = line1.replace(" ","")
line1 = line1.replace("\n","")
line1 = line1.replace("(s)","")
line2 = line2.replace("\n","")
line2 = line2.replace("\t","")
line2 = line2.replace(" ","")

var_names = re.split(';|,', line1)
var_numbers = re.split(';|,', line2)
print(var_names)
print(var_numbers)


#字符串转数字
var_new_num = []
for var_number in var_numbers:
  if('.' in var_number):
    # print(var_number)
    var_new_num.append(float(var_number))
    # print(float(var_number))

  else :
    var_new_num.append(int(var_number))
    # int(var_number)
    
#print(var_new_num)
#dict1=dict(zip(var_names,var_new_num))

#键值对配对
for name,value in zip(var_names,var_new_num):
  exec(f"{name} = {value}")
print(time_steps, time_step, radius, v_variance, N_particles)

#读取文件step
data = []
linelist = []
line_new = text.readline()
while line_new != '' :
  if('# time' in line_new) :
    # print(line_new)
    data.append(linelist)
    linelist=[]
    line_new = text.readline()

  if('# x' in line_new):
    line_new = text.readline()
  if(line_new == "\n"):
    line_new = text.readline()

  else :
    line_new = line_new.replace("\n","")
    line_new = line_new.replace("\t","")
    line_new = line_new.replace(" ","")
    var_numbers = re.split(';|,', line_new)
    var_tmp = []
    for var_number in var_numbers:
      if('.' in var_number):
        var_tmp.append(float(var_number))
      else :
        var_tmp.append(int(var_number))
    linelist.append(var_tmp)
    # linelist.append(line_new)
    line_new = text.readline()
# print(data)
data.append(linelist)

data = list(filter(None, data))


print(len(data), len(data[0]), len(data[0][0]), type(data[0][0][0]))
# print(data[0])
#ndarray
data = np.array(data)
print(type(data))
print(data.dtype)
print(data.shape)

R = data[0:, 0:, 0:2]
V = data[0:, 0:, 2:4]
R = np.swapaxes(R, 1, 2)
V = np.swapaxes(V, 1, 2)
print(R.shape)
print(V.shape)
print(type(R))

plt.figure(figsize=(8,8))
plt.scatter(R[0][0][:],R[0][1][:])
plt.axis([-1,1,-1,1])
plt.show()

with h5py.File("ca1_step1_input_data.hdf5", "w") as f:
    f.create_dataset("R", data=R)
    f.create_dataset("V", data=V)
    f.attrs['time_steps'] = time_steps
    f.attrs['time_step'] = time_step
    f.attrs['radius'] = radius
    f.attrs['v_variance'] = v_variance
    f.attrs['N_particles'] = N_particles