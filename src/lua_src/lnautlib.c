#include <nautilus/naut_types.h> 
#include <nautilus/libccompat.h>
#include <nautilus/math.h>
#define lmathlib_c
#define LUA_LIB
#include "lua/lua.h"
#include "lua/lauxlib.h"
#include "lua/lualib.h"
#include "lua/luaconf.h"






static const luaL_Reg nautlib[] = { 

{NULL, NULL}
};
LUAMOD_API int luaopen_naut (lua_State *L) {
          luaL_newlib(L, nautlib);
          return 1;
}