for sample in A01_31 A01_11 A01_35 A01_23 A01_39 A01_24 A01_62 A01_27 A01_63
do
	bwa mem -R "@RG\tID:${sample}\tSM:${sample}" sacCer3.fa ${sample}.fastq > ${sample}.sam
	samtools sort -O bam -o ${sample}.bam ${sample}.sam
	samtools index ${sample}.bam
done
