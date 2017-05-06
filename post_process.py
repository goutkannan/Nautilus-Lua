def post_process_files():
    
    FILES = ["./src/lua_src/linit.c","./include/lua/lualib.h","./src/lua_src/Makefile"]

    for files_to_modified in FILES:
        with open(files_to_modified,"r") as cfile:
            alllines=[]
            for line in cfile.readlines():
               
                if "ifndef LUA_TEST" in line:
                    line=line.replace("ifndef","ifdef")

                 

                alllines.append(line)

        with open(files_to_modified,"w") as cwf:
            cwf.writelines(alllines)


post_process_files()