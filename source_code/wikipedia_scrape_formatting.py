# This is a script which given a file of nominees and winners for a given Academy Awards ceremony will format the data into excel-compatible rows
#TODO: pull the data direct from a Wikipedia URL

# set data files
source_file = "K:/source_code/code_practice/neural_network/2018oscars.txt"
target_file = "K:/source_code/code_practice/neural_network/2018formatted.txt"
year = "2018"

source = open(source_file,"r")
lines = source.readlines()
new = open(target_file, "w+")

cat = ""
for l in lines:
    # separate out nominees from their films
    x = l.split(" – ")
    # if it couldn't be separated then it is a category title
    if len(x) == 1:
        cat = x[0].replace("\n","")
    else:
        # managing the idiosyncrasies of Wikipedia formatting
        if "as" in l or cat == "Best Director":
            y = x[1].split(" as ")
            new.write(y[0].replace("\n","") + "\t" + year +  "\t" + cat + "\t" + x[0] + "\n") 
        else:
            new.write(x[0] + "\t" + year + "\t" + cat + "\t" + x[1])

new.close()
source.close()
