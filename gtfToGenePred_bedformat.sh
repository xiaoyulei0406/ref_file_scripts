# get geneName and cooreponding exon information
gtfToGenePred -genePredExt -geneNameAsName2 /rsrch6/scratch/hema_bio-Malignan/adp_shukla/cyu/ref_lib/GRCh38/gencode.v40.annotation.gtf tmp

# get special columns
awk -v OFS="\\t" '{{print $2,$4,$5,$1,"0",$3,$6,$7,"0",$8,$9,$10}}' tmp > tmp1

# remove the last comma from column 11 and 12
awk 'BEGIN {FS=OFS="\t"} {gsub(/,$/, "", $11); gsub(/,$/, "", $12)}1' \
tmp1 > \
/rsrch6/scratch/hema_bio-Malignan/adp_shukla/cyu/ref_lib/GRCh38/gencode.v40.annotation.gtfToGenePred.bed

rm tmp
rm tmp1
