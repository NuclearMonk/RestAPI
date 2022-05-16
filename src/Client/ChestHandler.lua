local chest = peripheral.wrap("back")
local l =chest.list()
local r = {}
for index,item in ipairs(l) do
    if r[item.name]==nil then
        print("New Item: ".. item.name)
        r[item.name]= item.count
    else
        r[item.name] = r[item.name]+ item.count
    end
    
        
end
print(textutils.serializeJSON(r))
