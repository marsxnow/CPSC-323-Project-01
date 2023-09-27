import re 
from tabulate import tabulate


#Lexical Analyzer
def lex(source_code):
    tokens = []
    i = 0 
    while i < len(source_code):
        #keyword
        if re.match(r"int|float|double|char|bool|void|while|for|if", source_code[i:]):
            val = re.search(r"int|float|double|char|bool|void|while|for|if", source_code[i:]).group()
            tokens.append(["keyword", val])
            i += len(val)
            continue
        #identifier
        elif re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", source_code[i:]):
            val = re.search(r"[a-zA-Z_][a-zA-Z0-9_]*", source_code[i:]).group()
            tokens.append(["identifier", val])
            i += len(val)
            continue
        #real numbers
        elif re.match(r"[0.0-9.0]+", source_code[i:]):
            val = re.search(r"[0.0-9.0]+", source_code[i:]).group()
            tokens.append(["real", val])
            i += len(val)
            continue
        #operator
        elif re.match(r"[+\-*/]", source_code[i]):
            tokens.append(["operator", source_code[i]])
            i += 1
            continue
        #separator
        elif re.match(r"[();]", source_code[i]):
            tokens.append(["separator", source_code[i]])
            i += 1
            continue
        #assignment
        elif re.match(r"[=<>]", source_code[i]):
            tokens.append(["assignment", source_code[i]])
            i += 1
            continue
        #ignore whitespace
        elif re.match(r"\s", source_code[i]):
            i += 1
            continue
        else:
            i += 1
            continue
    return tokens



def main():
    with open("source_code.txt", "r") as file:
        source_code = file.read()
    
    tokens = lex(source_code)

    with open("output.txt", "w") as file:
        for token in tokens:
            file.write(str(token) + "\n")
        
    
if __name__ == "__main__":
    main()