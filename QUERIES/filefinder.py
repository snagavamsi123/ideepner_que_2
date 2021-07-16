import os

def find_files(filename, search_path):
   result = []
   count=1
   for root, dir, files in os.walk(search_path):
      for ind_dir in dir:
          ind_dir = ind_dir.lower()
          filename = filename.lower()
          if filename in ind_dir:
             #result.append(os.path.+join(root, filename))
             print(os.path.join(root, filename))
             print(10*'#'+ str(count)+ 10*'#')
             count+=1
   #return result

print(find_files("ideep","C:/Users"))
