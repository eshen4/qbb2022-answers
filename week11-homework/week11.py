#!/usr/bin/env python

import sys
import scanpy as sc

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()

sc.tl.pca(adata, n_comps=None, zero_center=True, svd_solver='arpack',
        random_state=0, return_info=False, use_highly_variable=None, dtype='float32',
        copy=False, chunked=False, chunk_size=None)
sc.pl.pca(adata, save="unfilteredpca.png")


sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

sc.tl.pca(adata, n_comps=None, zero_center=True, svd_solver='arpack',
        random_state=0, return_info=False, use_highly_variable=None, dtype='float32',
        copy=False, chunked=False, chunk_size=None)
sc.pl.pca(adata, save="filteredpca.png")

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.leiden(adata)
sc.tl.tsne(adata)
sc.pl.tsne(adata, color="leiden", save="leiden.png")
sc.tl.umap(adata, maxiter=1000)
sc.pl.umap(adata, color="leiden", save="leiden.png")

sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save="ttest.png")

sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False, save="logreg.png")

#make list of gene names
#parse through gene names and pick out some?
genelist = adata.var.index
for i in range(0, len(genelist), 5):
    sc.pl.tsne(adata, color=genelist[i], show=True)

sc.pl.tsne(adata, color=["Ndnf", "Tyrobp", "Rgs5", "Sox17", "Hbb-bt", "Lhx6"], save="support.png")
#Ndnf=bipolar cells, Tyrobp=macrophage, Rgs5=smooth muscle cells, Hbb-bt=Neutrophils, Sox17=Adipocytes, Lhx6=inhibitory neurons

marker_dict = {
            "0": "",
            "1": "Inhibitory neuron",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": "",
            "10": "",
            "11": "",
            "12": "",
            "13": "",
            "14": "",
            "15": "",
            "16": "Neutrophils",
            "17": "",
            "18": "",
            "19": "",
            "20": "",
            "21": "Adipocytes",
            "22": "Bipolar",
            "23": "",
            "24": "Smooth muscle",
            "25": "Macrophage",
            "26": "",
            "27": ""
            }
            
adata.obs['cell type'] = adata.obs['leiden'].map(marker_dict).astype('category')
sc.pl.tsne(adata, color='cell type', legend_loc='on data', save="labeled.png")