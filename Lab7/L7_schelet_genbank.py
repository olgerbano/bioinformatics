import string

def extractDNA(fin, fout):
    # TODO: de extras adn (de la 'ORIGIN' pana la '//') si de scris  in format fasta
    #pass
    fisier_in = open(fin,'r');
    fisier_out = open(fout,'w');
    ok = 0;
    for line in fisier_in.readlines():
        if(line.strip() =="ORIGIN"):
            ok = 1;
            continue;
        if(line.strip() == "//"):
            ok = 0;
        if(ok == 1):
            line = line.lstrip();
            
            SS = line[line.find(' ')+1:].replace(" ","")
            if len(SS) == 61:
                fisier_out.write(str(SS));
            else:
                fisier_out.write(SS[:SS.find('\n')]);
            
    fisier_in.close();
    fisier_out.close();

def compl(str): 
    # intoarce secventa de adn complementara lui str
    # TODO: de testat
    tb = str.maketrans('ATCG', 'TAGC') # tabela de translatie
    return str.translate(tb)[::-1] # face traslatarea efectiva si inversarea secv

def complement(str,fADN):
    #trateaza complement
    
    #sari dupa sirul "complement (" si elimina ultima ")"
    str = str[len('complement('):-1] 
    
    if str[0] in '123456789':
        # extragere capete
        index = str.find('.')
        a = int(str[:index]) - 1
        b = int(str[index+2:]) - 1
        return compl(extractGeneFromFile(a,b,fADN))
    elif str[0] == 'j':
        return compl(join(str,fADN))
    
    return False
    
def join(str, fADN):
    #trateaza join
    # TODO: elimina cuvantul "join(" si ultima ")"
    # TODO: concatenarea secventelor genei
    # HINT: folositi functiile split si strip
    str = str[len('join('):-1];
    if str[0] in '123456789':
    	index = str.find('.');
    	a = int(str[:index]) - 1;
    	b = int(str[index+2:]) - 1;
    	extracted = extractGeneFromFile(a,b,fADN).strip().split();
    	return "".join(extracted)

def extractGeneFromFile(a,b,fADN):
    # TODO: de extras o gena de la pozitia a la b din fisierul fADN (sequences.adn)
    #sunt 60 de caractere pe fiecare linie, pe ultima linie pot fi mai putine
    #se trece peste prima linie - vezi format fasta
    #import mmap
    #filein = open(fADN,'r');
    #s = mmap.mmap(filein.fileno(),0,access = mmap.ACCESS_READ)
    #return str(s[a:b]);

    SSS = "";
    fisier_in = open(fADN,'r');
    for line in fisier_in:
        SSS += line.strip();
    return str(SSS[a:b]);    
    #print(SSS[a:b]);

def extractGene(str, fADN):
    str = str.strip()
    str = str.replace('<', '')
    str = str.replace('>', '')
    
    if str[0] in '123456789':
        # extragere capete
        index = str.find('.')
        a = int(str[:index]) - 1
        b = int(str[index+2:]) - 1
        return extractGeneFromFile(a,b,fADN)
    
    elif str[0] == 'c':
        return complement(str, fADN)
    elif str[0] == 'j':
        return join(str, fADN)
    
    return False

def readGenes(fgenbank, fADN, fout):
    f = open(fgenbank,'r')
    g = open(fout,'w')
    
    data = f.readline()
    while 'ORIGIN' not in data:
        if data[5:9] == 'gene':
            g.write(extractGene(data[21:], fADN) + '\n')
        data = f.readline()
    g.close()
    f.close()
    
if __name__ == '__main__':
    extractDNA('exemplu.gb', 'sequence.adn')
    readGenes('exemplu.gb', 'sequence.adn', 'sequence.genes')