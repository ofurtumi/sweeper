nextline = False
events = {}
tempTitle = ""
tempId = ""
tempStart = ""
asdf = ""

with open('export.xml', encoding="UTF-8") as f:
    lines = f.readlines()
    # print(type(lines))
    # print(lines[0])
    for line in lines:
        if ("<title>" in line): 
            tempTitle = line.lstrip()[16:-12]
            tempTitle = tempTitle.replace('"', "'")
        elif ("<wp:post_id>" in line): tempId = line.lstrip()[12:-14]

        if (nextline):
            nextline = False
            tempStart = line.lstrip()[24:-20]
            tempStart = f"{tempStart[5:7]}-{tempStart[8:10]}-{tempStart[0:4]}"
            # print("asdf: " + asdf + " " + tempTitle)
            events[tempId] = [tempTitle, tempStart]

        if ("_EventStartDateUTC" in line): nextline = True


        # if ("<content:encoded>" in line): 
        #     if ("<![CDATA[[" in line): nextline = True
        #     else: print(line.lstrip())

print(len(events))
print(list(events)[0])
# print(events)

with open('testdata2.json', "w", encoding="UTF-8") as f:
    f.write("")

with open('testdata2.json', "a", encoding="UTF-8") as f:
    f.write("[\n")
    for eventId, other in events.items():
            f.write(f'{"{"}"id":"{eventId}","title":"{other[0]}", "start":"{other[1]}"{"}"}{"," if eventId != list(events)[-1] else ""}\n')
    f.write("]")
