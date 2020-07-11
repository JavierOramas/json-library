from dirsync import sync
import  os
import sys
import datetime
# import Extended

def make_commit(target_path):
    #abrir consola en targuet??
    os.system('cd '+ target_path)
    os.system('git add *')
    os.system('git commit -m "'+str(datetime.datetime.now())+'"')
    # try:
    #     os.system('git push origin master')

def make_sync(commit, source_path, target_path):
    
    # if not exists(source_path):
    #     print("The source path does not exits")
    #     return 
    
    os.makedirs(target_path,exist_ok=True)
    sync(source_path, target_path, 'sync') 
    
    make_commit(target_path)

if __name__ == '__main__':
    
    commit = bool(sys.argv[1])
    source = sys.argv[2]
    target = sys.argv[3]
    make_sync(commit,source,target)
