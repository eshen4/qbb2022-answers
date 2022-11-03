#Week 8 Homework: Nanopore Sequencing and Methylation

### Part 1 -- Call and phase variant per region

medaka_variant -h:
    -h  show this help text.
    -i  input bam of reads aligned to ref. Read groups are currently ignored,
        so the bam should only contain reads from a single sample.
    -f  input fasta input reference (required).
    -r  region string(s). If providing multiple regions, wrap them in quotes.
        If not provided, will process all contigs in bam. 
    -o  output folder (default: medaka_variant).
    -s  medaka model for initial SNP calling from mixed reads prior to phasing,
        (default: r941_prom_snp_g360).
        Available: r103_min_high_g345, r103_min_high_g360, r103_prom_high_g360, 
					r103_prom_snp_g3210, r103_prom_variant_g3210, r10_min_high_g303, 
					r10_min_high_g340, r941_min_fast_g303, r941_min_high_g303, 
					r941_min_high_g330, r941_min_high_g340_rle, r941_min_high_g344, 
					r941_min_high_g351, r941_min_high_g360, r941_prom_fast_g303, 
					r941_prom_high_g303, r941_prom_high_g330, r941_prom_high_g344, 
					r941_prom_high_g360, r941_prom_snp_g303, r941_prom_snp_g322, 
					r941_prom_snp_g360, r941_prom_variant_g303, r941_prom_variant_g322, 
					r941_prom_variant_g360.
        Alternatively a .hdf file from 'medaka train'. 
    -m  medaka model for final variant calling from phased reads,
        (default: r941_prom_variant_g360).
        Available: r103_min_high_g345, r103_min_high_g360, r103_prom_high_g360, 
					r103_prom_snp_g3210, r103_prom_variant_g3210, r10_min_high_g303, 
					r10_min_high_g340, r941_min_fast_g303, r941_min_high_g303, 
					r941_min_high_g330, r941_min_high_g340_rle, r941_min_high_g344, 
					r941_min_high_g351, r941_min_high_g360, r941_prom_fast_g303, 
					r941_prom_high_g303, r941_prom_high_g330, r941_prom_high_g344, 
					r941_prom_high_g360, r941_prom_snp_g303, r941_prom_snp_g322, 
					r941_prom_snp_g360, r941_prom_variant_g303, r941_prom_variant_g322, 
					r941_prom_variant_g360.
        Alternatively a .hdf file from 'medaka train'. 
    -t  number of threads with which to create features (default: 1).
    -p  output phased vcf.
    -b  batchsize, controls memory use (default: 100).
    -d  delete intermediate files. (default: keep).
    -N  threshold for filtering indels in final VCF (default: 9)
    -P  threshold for filtering SNPs in final VCF (default: 8)
    -U  Avoid filtering of final VCF (default: do filter)
    -S  stop after initial SNP calling from mixed reads prior to phasing.
medaka_variant -i <bam>
*use default for -s and -m (r941_prom_snp_g360)*
-p: output phased vcf
	-p regions.bed chr:start-end
		chr11   1900000 2800000
		chr14   100700000       100990000
		chr15   23600000        25900000
		chr20   58800000        58912000

#####Commands used:

medaka_variant -i methylation.bam -f hg38.fa -r "chr11:1900000-2800000" -o chr11medaka_variant -p chr11regions.vcf 
medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14medaka_variant -p chr14regions.vcf 
medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15medaka_variant -p chr15regions.vcf 
 medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20medaka_variant -p chr20regions.vcf
 
### Part2 -- Mark reads with the correct haplotype tag

usage: whatshap [-h] [--version] [--debug]
                {compare,find_snv_candidates,genotype,hapcut2vcf,haplotag,phase,polyphase,split,stats,unphase}
                ...

positional arguments:
  {compare,find_snv_candidates,genotype,hapcut2vcf,haplotag,phase,polyphase,split,stats,unphase}
    compare             Compare two or more phasings
    find_snv_candidates
                        Generate candidate SNP positions.
    genotype            Genotype variants
    hapcut2vcf          Convert hapCUT output format to VCF
    haplotag            Tag reads by haplotype
    phase               Phase variants in a VCF with the WhatsHap algorithm
    polyphase           Phase variants in a polyploid VCF using a
                        clustering+threading algorithm.
    split               Split reads by haplotype.
    stats               Print phasing statistics of a single VCF file
    unphase             Remove phasing information from a VCF file

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --debug               Print debug messages

##### Commands used:

whatshap haplotag -o chr11.bam --reference hg38.fa --region chr11:1900000:2800000 --output-haplotag-list haplotagchr11 chr11medaka_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr14.bam --reference hg38.fa --region chr14:100700000:100990000 --output-haplotag-list haplotagchr14 chr14medaka_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr15.bam --reference hg38.fa --region chr15:23600000:25900000 --output-haplotag-list haplotagchr15 chr15medaka_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam

whatshap haplotag -o chr20.bam --reference hg38.fa --region chr20:58800000:58912000 --output-haplotag-list haplotagchr20 chr20medaka_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam

### Part 3 -- Split reads into two files based on their haplotype

##### Commands used:

whatshap split --output-h1 h1-chr11.bam --output-h2 h2-chr11.bam chr11.bam haplotagchr11

whatshap split --output-h1 h1-chr14.bam --output-h2 h2-chr14.bam chr14.bam haplotagchr14

whatshap split --output-h1 h1-chr15.bam --output-h2 h2-chr15.bam chr15.bam haplotagchr15

whatshap split --output-h1 h1-chr20.bam --output-h2 h2-chr20.bam chr20.bam haplotagchr20

samtools cat -o h1.bam h1-chr11.bam h1-chr14.bam h1-chr15.bam h1-chr20.bam
samtools cat -o h2.bam h2-chr11.bam h2-chr14.bam h2-chr15.bam h2-chr20.bam 
samtools index h1.bam
samtools index h2.bam

### Part 4 -- Setting up IGV

##### Commands used:
(just used the commands listed in the assignment)

### Part 5 -- Configuring IGV for differential methylation

./igv.sh h1.bam

### Part 6 -- Find and plot differentially methylated regions

I do not expect each differentially methylated region between H1 and H2 to correspond to the same haplotype. DNA methylation is highly conserved from the parent strand, so the differentially methylated regions are likely not from the same parent.
 
 
