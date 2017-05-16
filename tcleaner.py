import re

# read source file:
src_file = open("tc_imput.txt","r")
text = src_file.read()
print "-tcleaner-"
print "______________"
print "original text:"
print text
print "______________"
clean = re.sub('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', text, flags=re.MULTILINE)
# write output file:
out_file = open("tc_output.txt","w")
out_file.write(clean)
print "cleaned text:"
print clean
print "______________"
out_file.close()
print    
print "done."