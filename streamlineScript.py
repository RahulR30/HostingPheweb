from pathlib import Path
import subprocess
import pheweb

pathlist = Path('/Users/rahulrao/Library/CloudStorage/GoogleDrive-genetics@usc.edu/Shared drives/AllayeeLab/Rahul-PheWeb').glob('*')

for path in pathlist:
    # because path is object not string
    filepath = str(path)
    # specify the filepath and the strings to be searched and replaced
    # open the file and read its contents
    print(filepath)
    with open(filepath, 'r') as file:
        filedata = file.read()

    # replace the old string with the new string
    filedata = filedata.replace('SNP', 'variant_id')
    filedata = filedata.replace('CHR', 'chrom')
    filedata = filedata.replace('BP', 'pos')
    filedata = filedata.replace('effect_allele_frequency','maf')
    filedata = filedata.replace('effect_allele', 'ref')
    filedata = filedata.replace('Allele1', 'ref')
    filedata = filedata.replace('other_allele','alt')
    filedata = filedata.replace('Allele2', 'alt')
    filedata = filedata.replace('BETA', 'beta')
    filedata = filedata.replace('SE','sebeta')
    filedata = filedata.replace('N','n')
    filedata = filedata.replace('P-value','p.value')

    # write the modified data back to the file
    with open(filepath[:-4] + "Edited.tsv" + "", 'w') as file:
        file.write(filedata)
    with open ("/Users/rahulrao/Library/Mobile Documents/com~apple~CloudDocs/Programming/Projects/phewebDatabase/phenolist.tsv", 'r') as file:
        filedata = file.read()
    filedata +=  filepath + ", " + "\n" 
    with open ("/Users/rahulrao/Library/Mobile Documents/com~apple~CloudDocs/Programming/Projects/phewebDatabase/phenolist.tsv", 'w') as file:
        file.write(filedata)

    
