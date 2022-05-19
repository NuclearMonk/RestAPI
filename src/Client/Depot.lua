function register()
    local myURL = "http://localhost:5000/depots/"
    body = textutils.serialiseJSON({location ={x= 1,y = 1,z = 1}})
    headers = {[ "Content-Type" ] = "application/json"}
    http.request({url=myURL,method="POST",headers=headers, body=body})
    local event, url, response
    repeat
        event, url, response = os.pullEvent("http_success")
    until url == myURL
    code, text = response.getResponseCode()
    if not code == 200 then
        print(code,text)
        return -1
    end
    local responseTable = textutils.unserialiseJSON(response.readAll())
    saveIDToFile(responseTable['id'])
    return tonumber(responseTable['id'])
end

function unregister(id)
    local myURL = "http://localhost:5000/depot/" .. tostring(math.floor(id) .."/")
    http.request({url=myURL,method="DELETE"})
    local event, url, response
    repeat
        event, url, response = os.pullEvent("http_success")
    until url == myURL
    fs.delete("ID")
end

function readIDFromFile()
    local Handle = fs.open("ID", "r")
    if Handle == nil then 
        return -1
    end
    local IDString = Handle.read(l)
    Handle.close()
    return tonumber(IDString,10)
end

function saveIDToFile(id)
    local Handle = fs.open("ID", "w")
    if Handle == nil then return end
    Handle.write(tonumber(id))
    Handle.close()
end

function putItemTable(id,items)
    local myURL = "http://localhost:5000/depot/" .. tostring(math.floor(id).."/")
    headers = {[ "Content-Type" ] = "application/json"}
    print(body)
    http.request({url=myURL,method="PUT",headers=headers, body=items})
    local event, url, response
    repeat
        event, url, response = os.pullEvent("http_success")
    until url == myURL
    if not response.getResponseCode()== 200 then
        print("error:".. response.getResponseCode())
    end
end

function getIDorRegister()
    local ID = readIDFromFile()
        if ID == -1 then
            ID = register()
    end
    return ID
end

return {getIDorRegister= getIDorRegister, putItemTable=putItemTable,}

