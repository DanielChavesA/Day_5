import numpy as np
import scipy.linalg as la
import scipy.stats as stats
import matplotlib.pyplot as plt

# a. Define matrix A
A = np.array([[1, -2, 3],
              [4, 5, 6],
              [7, 1, 9]])

# b. Define vector b
b = np.array([1, 2, 3])

# c. 
x = la.solve(A, b)
print("Solution x:", x)

# d. 
print("Check: Ax =", np.dot(A, x)) #should be the vector b

# e. 
B = np.random.rand(3, 3) 
x_B = la.solve(A, B)
print("Solution for random B:", x_B)
print("Check: Bx =", np.dot(B, x))

# f. 
eigenvalues, eigenvectors = la.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# g. 
A_inv = la.inv(A)
det_A = la.det(A)
print("Inverse of A:\n", A_inv)
print("Determinant of A:", det_A)

# h. 
norm_1 = la.norm(A, 1)  # 1-norm
norm_2 = la.norm(A, 2)  # 2-norm
norm_inf = la.norm(A, np.inf)  # Infinity norm
print("1-norm:", norm_1)
print("2-norm:", norm_2)
print("Infinity norm:", norm_inf)

# Statistics
# a.
poisson_rv = stats.poisson(mu=3)
x_poisson = np.arange(0, 10)
pdf_poisson = poisson_rv.pmf(x_poisson)
cdf_poisson = poisson_rv.cdf(x_poisson)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.bar(x_poisson, pdf_poisson)
plt.title("Poisson PMF")

plt.subplot(1, 3, 2)
plt.plot(x_poisson, cdf_poisson, marker='o')
plt.title("Poisson CDF")

plt.subplot(1, 3, 3)
plt.hist(poisson_rv.rvs(size=1000), bins=10, density=True, alpha=0.6, color='g')
plt.title("Poisson Histogram")
plt.show()

# b. 
normal_rv = stats.norm(loc=0, scale=1)
x_normal = np.linspace(-4, 4, 100)
pdf_normal = normal_rv.pdf(x_normal)
cdf_normal = normal_rv.cdf(x_normal)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(x_normal, pdf_normal)
plt.title("Normal PDF")

plt.subplot(1, 3, 2)
plt.plot(x_normal, cdf_normal)
plt.title("Normal CDF")

plt.subplot(1, 3, 3)
plt.hist(normal_rv.rvs(size=1000), bins=30, density=True, alpha=0.6, color='r')
plt.title("Normal Histogram")
plt.show()

# c. Test if two sets of independent random data come from the same distribution
sample1 = stats.norm.rvs(size=1000)
sample2 = stats.norm.rvs(size=1000)
t_stat, p_value = stats.ttest_ind(sample1, sample2)
print("T-test statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("The two samples are significantly different.")
else:
    print("The two samples likely come from the same distribution.")
