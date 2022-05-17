local ch = require("ChestHandler")
while true do
    print(textutils.serialize(ch.await_item_change("back")))
end