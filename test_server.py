from ServerModules.serverModules import *
# Testing DBQuery().getData()

print("\n==>Get Kenya details \n")
print(DBQuery("get:Kenya").getData())


print("\n==>Get Uganda details \n")
print(DBQuery("get:Uganda").getData())
