strings = ["mohadeseh", "zahra", "reyhaneh", "fereshteh" ,"abolfazl","mona"]

string_remove = "mona"
i = 0
x = 0
while i < len(strings):
    if strings[i] == string_remove :
        strings.remove(strings[i]) 
        x = x+1
        break
    else:
        i += 1
print(x)
print(strings)
