
def reverse(file_r,file_w):
    f1 = open(file_r,'r+')
    f2 = open(file_w,'w+')
    text = f1.read()
    text_w = text[::-1]
    f2.write(text_w)
    f1.close()
    f2.close()

f1 = 'ip.txt'
f2 = 'op.txt'
reverse(f1,f2)
