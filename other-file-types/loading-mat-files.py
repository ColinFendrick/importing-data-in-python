import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('../_datasets/albeck_gene_expression.mat')

print(type(mat))
