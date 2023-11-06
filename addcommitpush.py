import os

message=input("enter message hear")

print('git status')
os.system('git status')
print('add file')
os.system('git add -A')
os.system('git commit -m "message"')
os.system('git push')
print('upload successful')