def get_moves(moves):
    move_list = []
    for move in moves:
        if (move.find("div", {"class": "movename"}) != None):
            name = move.find("div", {"class": "movename"})
            startup = move.find("div", {"class": "startup"})
            totalframes = move.find("div", {"class": "totalframes"})
            landinglag = move.find("div", {"class": "landinglag"})
            basedamage = move.find("div", {"class": "basedamage"})
            shieldlag = move.find("div", {"class": "shieldlag"})
            shieldstun = move.find("div", {"class": "shieldstun"})
            advantage = move.find("div", {"class": "advantage"})
            activeframes = move.find("div", {"class": "activeframes"})

            # print(name)

            if(name.text.strip() != 'Stats'):
                move_entry = {"name": name.text.strip() if name is not None else " ",
                'startup': startup.text.strip() if startup is not None else " ",
                'totalframes' : totalframes.text.strip() if totalframes is not None else " ",
                'landinglag':landinglag.text.strip() if landinglag is not None else " ",
                'basedamage':basedamage.text.strip() if basedamage is not None else " ",
                'shieldlag':shieldlag.text.strip() if shieldlag is not None else " ",
                'shieldstun':shieldstun.text.strip() if shieldstun is not None else " ",
                'advantage':advantage.text.strip() if advantage is not None else " ",
                'activeframes':activeframes.text.strip() if activeframes is not None else " "}
            else:
                stats = move.find_all("div")
                # print(stats)
                name = stats[0]
                weight = stats[1]
                gravity = stats[2]
                walkSpeed = stats[3]
                runSpeed = stats[4]
                initDash = stats[5]
                airSpeed = stats[6]
                airAccel = stats[7]
                SH_FH_SHFF_FHFF = stats[8]
                fallSpeed = stats[9]
                oos1 = stats[10]
                oos2 = stats[11]
                oos3 = stats[12]
                shieldGrab = stats[13]
                shieldDrop = stats[14]
                jumpSquat = stats[15]

                move_entry = {"name": name.text.strip() if name is not None else " ",
                'weight': weight.text.strip() if weight is not None else " ",
                'gravity' : gravity.text.strip() if gravity is not None else " ",
                'walkSpeed':walkSpeed.text.strip() if walkSpeed is not None else " ",
                'runSpeed':runSpeed.text.strip() if runSpeed is not None else " ",
                'initDash':initDash.text.strip() if initDash is not None else " ",
                'airSpeed':airSpeed.text.strip() if airSpeed is not None else " ",
                'airAccel':airAccel.text.strip() if airAccel is not None else " ",
                'SH_FH_SHFF_FHFF':SH_FH_SHFF_FHFF.text.strip() if SH_FH_SHFF_FHFF is not None else " ",
                'fallSpeed':fallSpeed.text.strip() if fallSpeed is not None else " ",
                'oos1':oos1.text.strip() if oos1 is not None else " ",
                'oos2':oos2.text.strip() if oos2 is not None else " ",
                'oos3':oos3.text.strip() if oos3 is not None else " ",
                'shieldGrab':shieldGrab.text.strip() if shieldGrab is not None else " ",
                'shieldDrop':shieldDrop.text.strip() if shieldDrop is not None else " ",
                'jumpSquat':jumpSquat.text.strip() if jumpSquat is not None else " "}
            move_list.append(move_entry)
    return move_list