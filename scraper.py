nextline = False
events = {}
tempTitle = ""
tempId = ""
tempStart = ""
tempStop = ""

with open('export.xml', encoding="UTF-8") as f:
    lines = f.readlines()
    # print(type(lines))
    # print(lines[0])
    for line in lines:
        if ("<title>" in line): 
            tempTitle = line.lstrip()[16:-12]
            tempTitle = tempTitle.replace('"', "'")
        elif ("<wp:post_id>" in line): tempId = line.lstrip()[12:-14]
        elif ("_EventStartDate" in line): nextline = True

        if (nextline):
            nextline = False
            tempStart = line.lstrip()[24,-20]

        # if ("<content:encoded>" in line): 
        #     if ("<![CDATA[[" in line): nextline = True
        #     else: print(line.lstrip())

print(len(events))
print(list(events)[0])
print(events["2602"])

with open('testdata.json', "w", encoding="UTF-8") as f:
    f.write("")

with open('testdata.json', "a", encoding="UTF-8") as f:
    f.write("[")
    for eventId, eventName in events.items():
            f.write(f'{"{"}"{eventId}":"{eventName}"{"}"}{"," if eventId != list(events)[-1] else ""}\n')
    f.write("]")
