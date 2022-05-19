local ch = require("ChestHandler")
local dp = require("Depot")
local ID = dp.getIDorRegister()
print("ID:".. tostring(math.floor(ID)))
while true do
    dp.putItemTable(ID,ch.await_item_change("back"))
end
