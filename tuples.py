point_a = (1,10,6)
point_b = (5,8,6)
x_a,y_a,z_a = point_a
x_b,y_b,z_b = point_b
distance = pow((x_a - x_b) ** 2 + (y_a - y_b) ** 2 + (z_a - z_b) ** 2,0.5)
print(distance)