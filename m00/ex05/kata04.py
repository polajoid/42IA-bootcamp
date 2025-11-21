kata = (0, 4, 132.42222, 10000, 12345.67)
temp = "module_{:02d}, ex_{:02d} : {:02.02f}, {:02.02e}, {:02.02e}"
print(temp.format(*kata))
