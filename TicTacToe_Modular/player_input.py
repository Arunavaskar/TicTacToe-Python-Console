def player_input(*args):
    playerone_marker,playertwo_marker,playerone_position,playertwo_position = args
    B = {1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",7: "g",8: "h",9: "i"}
    blank_B = {1: "            ",2: "            ",3: "            ",4: "            ",5: "            ",6: "            ",7: "            ",8: "            ",9: "            "}
    for key, value in B.items():
        if key == playerone_position:
            #blank_B[key] = "      "+marker+"     "
            if value == playertwo_marker:
                continue
            else:
                blank_B[key] = "      "+playerone_marker+"     "
                
#def player_two_input(*args):
    #playerone_marker,playertwo_marker,playerone_position,playertwo_position = args
    #B = {1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",7: "g",8: "h",9: "i"}
    #blank_B = {1: "            ",2: "            ",3: "            ",4: "            ",5: "            ",6: "            ",7: "            ",8: "            ",9: "            "}
    for key, value in B.items():
        if key == playertwo_position:
            #blank_B[key] = "      "+marker+"     "
            if value == playerone_marker:
                continue
            else:
                blank_B[key] = "      "+playertwo_marker+"     "