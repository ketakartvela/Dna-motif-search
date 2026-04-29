def profile(text,k, matrix):
    navigation={"A":0,"C":1,"G":2,"T":3}
    best_score=float("-inf")
    best_motif=None
    for i in range(len(text)-k+1):
        kmer=text[i:i+k]
        score=1
        for idx, char in enumerate(kmer):
            row=navigation[char]
            column=idx
            score*=matrix[row][column]
        if score>best_score:
            best_score=score
            best_motif=kmer
    return best_motif
with open(r"sample.input.txt","r") as f:
    lines=f.read().strip().splitlines()
text=lines[0]
k=int(lines[1])
matrix=[list(map(float,line.split())) for line in lines[2:]]
result=profile(text,k,matrix)
print(result)


          
            
