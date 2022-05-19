function serialize_peripheral_inventory(direction)
    local inventory = peripheral.wrap(direction)
    local l =inventory.list()
    local r = {}
    for index,item in pairs(l) do
        if r[item.name]==nil then
            r[item.name]= item.count
        else
            r[item.name] = r[item.name]+ item.count
        end
    end
    return r
end

function await_item_change(direction)
    local old_list  = serialize_peripheral_inventory(direction)
    while true do
        os.sleep(1)
        local new_list = serialize_peripheral_inventory(direction)
        diff = {}
        for name, count in pairs(old_list) do
            diff[name]= count
        end
        for name, count in pairs(new_list) do
            if diff[name] == nil then
                diff[name] = count
            elseif diff[name] == count then
                diff[name]=nil
            else
                diff[name] = count
            end
        end
        local size = 0
        for name in pairs(diff) do
            if new_list[name]== nil then
                diff[name] = 0
            end
            size = size + 1
        end
        if size > 0 then
            return textutils.serialiseJSON(diff)
        end
    end
end

return {serialize_peripheral_inventory = serialize_peripheral_inventory,await_item_change = await_item_change}
