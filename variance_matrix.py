rows=input("Enter the number of rows/data points")
n=int(rows)
matrix=[]
for i in range(n):
    ht=float(input(f"Enter height{i+1}:"))
    wt=float(input(f"Enter weight{i+1}:"))
    matrix.append([ht,wt])
if n<2:
    print("\n Error enter atleast two datapoints:")
else:
    sum_ht=0.0
    sum_wt=0.0
    for i in range(n):
        sum_ht +=matrix[i][0]
        sum_wt +=matrix[i][1]
    average_ht=sum_ht/n
    average_wt=sum_wt/n
    sum_sq_ht=0.0
    sum_sq_wt=0.0
    sum_hw=0.0
    for i in range(n):
        diff_ht=matrix[i][0]-average_ht
        diff_wt=matrix[i][1]-average_wt
        sum_sq_ht +=diff_ht*diff_ht
        sum_sq_wt +=diff_wt*diff_wt
        sum_hw +=diff_ht*diff_wt
    var_ht=sum_sq_ht/(n-1)
    var_wt=sum_sq_wt/(n-1)
    cov_hw=sum_hw/(n-1)
    cov_matrix=[[var_ht,cov_hw],[cov_hw,var_wt]]
    print("covariance matrix:")
    for row in cov_matrix:
        print(row)
    
