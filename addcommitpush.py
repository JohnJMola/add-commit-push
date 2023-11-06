import os


print('git status')
os.system('git status')
print('add file')
os.system('git add -A')
os.system('git commit -m "upload"')
os.system('git push')
print('upload successful')