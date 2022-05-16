function serialize_peripheral_inventory(direction)
    local inventory = peripheral.wrap(direction)
    local l =inventory.list()
    local r = {}
    for index,item in ipairs(l) do
        if r[item.name]==nil then
            print("New Item: ".. item.name)
            r[item.name]= item.count
        else
            r[item.name] = r[item.name]+ item.count
        end
    end
    return r
end

function await_item_change(direction)
    local inventory = peripheral.wrap(direction)
    local old_list  = serialize_peripheral_inventory("back")
    while true do
        os.sleep(1)
        local new_list = serialize_peripheral_inventory("back")
        diff = {}
        for name, count in pairs(old_list) do
            diff[name]= count
        end
        for name, count in pairs(new_list) do
            if diff[name] == nil then
                diff[name] = count
            elseif not diff[name] == count then
                diff[name] = count
            else
                diff[name]=nil
            end
        end
    end
    return diff
end

return {serialize_peripheral_inventory,await_item_change}