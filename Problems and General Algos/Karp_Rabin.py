# Karp Rabin algorithm for pattern matching in a document
# Author - rudrjit1729

# Base for hash value = size of alphabet -> |ASCII| = 256
a = 256 

def search(pat, txt, m):
    '''
    pat -> pattern
    txt -> text
    m -> size of table
    '''
    M = len(pat)
    N = len(txt)
    p = 0 # Hash value for pattern
    t = 0 # Hash value for text
    h = 1

    # The value of h would be "pow(d, M - 1) % m"
    for i in range(M - 1):
        h = (h * a) % m
    
    # Calculate hash value of pattern and first window of text
    for i in range(M):
        p = (a * p + ord(pat[i])) % m
        t = (a * t + ord(txt[i])) % m
    
    # Slide the pattern over text one by one 
    for i in range(N-M+1):
        # If hash values of current window and pattern matches
        # then check for the characters one by one
        if p == t:
            # Checking characters
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
            j += 1
            if j == M:
                print("Pattern found at index ", str(i))
        
        # Calculate hash value for next window of text: 
        # Remove leading character, add trailing character
        if i < N - M:
            t = (a * (t - ord(txt[i])*h) + ord(txt[i+M])) % m

            # T might be -ve, in that case add base value to it
            if t < 0:
                t += m

def main():
    txt = input("Enter text : ")
    pat = input("Enter pattern : ")
    m = 101 # A prime Number - size of the table 
    search(pat, txt, m) 

if __name__ == "__main__":
    main()
            
