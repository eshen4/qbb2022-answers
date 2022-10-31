#!/usr/bin/env python

import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#python load_data.py analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed test.png

#python load_data.py matrix/ddCTCF_full.6400.matrix matrix/dCTCF_full.6400.matrix matrix/6400_bins.bed matrix/dCTCF_full.40000.matrix full.png

def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = np.copy(mat)
    for i in range(N):
        bg = np.mean(mat[np.arange(i, N), np.arange(N - i)])
        mat2[np.arange(i, N), np.arange(N - i)] -= bg
        if i > 0:
            mat2[np.arange(N - i), np.arange(i, N)] -= bg
    return mat2

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = np.where(mat[1:-1, 1:-1] == 0)
    nmat = np.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat
    
def main():
    # in1_fname should be ddCTCF
    # in2_fname should be dCTCF
    # bin_fname should be bed file with bin locations
    
    in1_fname, in2_fname, bin_fname, in3_fname, out_fname = sys.argv[1:6]
    data1 = np.loadtxt(in1_fname, dtype=np.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    data2 = np.loadtxt(in2_fname, dtype=np.dtype([
        ('F1', int), ('F2', int), ('score', float)]))
    frags = np.loadtxt(bin_fname, dtype=np.dtype([
        ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
    data3 = np.loadtxt(in3_fname, dtype=np.dtype([
        ('F1', int), ('F2', int), ('score', float)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][np.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][np.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1

#making data the desired bin range
    binrange = np.where((data1['F1'] >= start_bin) & (data1['F2'] < end_bin))
    filterdata_1 = data1[binrange]
#log transform the filtered data
    filterdata_1['score'] = np.log(filterdata_1['score'])
    minimum = np.amin(filterdata_1['score'])
    truescore = filterdata_1['score'] - minimum
    filterdata_1['score'] = truescore
    filterdata_1['F1'] = filterdata_1['F1'] - start_bin
    filterdata_1['F2'] = filterdata_1['F2'] - start_bin
    #print(filterdata_1['score'])
    #fulldata = len(filterdata_1['score'])
    mat1 = np.zeros((end_bin - start_bin + 1, end_bin - start_bin + 1))
    #print(len(filterdata_1))
    #exit()
    mat1[filterdata_1['F1'], filterdata_1['F2']] = filterdata_1['score']
    mat1[filterdata_1['F2'], filterdata_1['F1']] = filterdata_1['score']
    
    binrange_2 = np.where((data2['F1'] >= start_bin) & (data2['F2'] < end_bin))
    filterdata_2 = data2[binrange_2]
#log transform the filtered data
    filterdata_2['score'] = np.log(filterdata_2['score'])
    minimum_2 = np.amin(filterdata_2['score'])
    truescore_2 = filterdata_2['score'] - minimum_2
    filterdata_2['score'] = truescore_2
    filterdata_2['F1'] = filterdata_2['F1'] - start_bin
    filterdata_2['F2'] = filterdata_2['F2'] - start_bin
    #i dont know how to do anything
    #print(filterdata_1['score'])
    #fulldata = len(filterdata_1['score'])
    mat2 = np.zeros((end_bin - start_bin + 1, end_bin - start_bin + 1))
    #print(len(filterdata_1))
    #exit()       
    mat2[filterdata_2['F1'], filterdata_2['F2']] = filterdata_2['score']
    mat2[filterdata_2['F2'], filterdata_2['F1']] = filterdata_2['score']
    #print(mat)
   # print(mat1)
    #print(mat2)
   # exit()                                  
    fig, ax = plt.subplots(3)
    max1 = np.amax(mat1)
    max2 = np.amax(mat2)
    absmax = max(max1, max2)
    ax[0].imshow(mat1, cmap = "magma", vmax = absmax)
    ax[0].set_title("ddCTCF")
    ax[1].imshow(mat2, cmap = "magma", vmax = absmax)
    ax[1].set_title("dCTCF")
    ax[2].imshow((smooth_matrix(remove_dd_bg(mat2))-smooth_matrix(remove_dd_bg(mat1))), 
                    cmap='seismic', norm=colors.CenteredNorm())
    ax[2].set_title("difference plot")
    plt.tight_layout()
    #plt.show()
    plt.savefig("part2_heatmaps")
    plt.close()
    exit()
    binrange3 = np.where((data3['F1'] >= 54878) & (data3['F2'] < 54951))
    filterdata_3 = data3[binrange3]
#log transform the filtered data
    filterdata_3['score'] = np.log(filterdata_3['score'])
    minimum3 = np.amin(filterdata_3['score'])
    truescore3 = filterdata_3['score'] - minimum3
    filterdata_3['score'] = truescore3
    column_min = filterdata_3['F1'][0]
    filterdata_3['F1'] = filterdata_3['F1'] - column_min
    filterdata_3['F2'] = filterdata_3['F2'] - column_min 
    #print(filterdata_3)
    #exit()
    insulation = []
    mat3 = np.zeros((54951 - 54878 + 1, 54951 - 54878 + 1))
    mat3[filterdata_3['F1'], filterdata_3['F2']] = filterdata_3['score']
    mat3[filterdata_3['F2'], filterdata_3['F1']] = filterdata_3['score']
    for i in range(5,54951 - 54878 + 1 ):
        insulation.append(np.mean(mat3[(i - 5):i, i:(i + 5)]))
    nucleotide = np.linspace(10400000, 13400000, len(insulation))
   
    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].axis('off')
    plt.margins(x=0)
    ax[1].set_xlim(10400000, 13400000)
    plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=1.0,
                    top=1.0,
                    wspace=0.4,
                    hspace=0.0)
    ax[0].imshow(mat3, cmap = "magma")
    ax[0].set_title("ddCTCF 40000")
    ax[1].scatter(nucleotide, insulation)
    ax[1].set_title("insulation scores")
    plt.tight_layout()
    plt.savefig("ddCTCF_40000_insulation_scores.png")
    plt.close()

    
if __name__ == "__main__":
    main()
