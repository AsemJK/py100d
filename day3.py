print("""
            .;;;, .;;;,                   .;;;, .;;;,
       .;;;,;;;;;,;;;;;,.;;;,       .;;;.,;;;;;,;;;;;,;;;.
      ;;;;xXXxXXxXXxXXxXXx;;;. .,. .;;;xXXxXXxXXxXXxXX;;;;;
  .,,.`xXX'             `xXXx,;;;;;,xXXx'            `XXx;;,,.
 ;;;;xXX'                  `xXXx;xXXx'                 `XXx;;;;
 `;;XX'                       `XXX'                      `XX;;'
,;;,XX                         `X'                        XX,;;,
;;;;XX,                                                  ,XX;;;;
 ``.;XX,                                                ,XX;,''
   ;;;;XX,                                            ,XX;;;;
    ```.;XX,                                        ,XX;,'''
       ;;;;XX,                                    ,XX;;;;
        ```,;XX,                                ,XX;,'''
            ;;;;XX,                          ,XX;;;;
             ````,;XX,                    ,XX;, '''
                 ;;;;;XX,              ,XX;;;;
                  `````,;XX,        ,XX;,''''
                       ;;;;;XX,  ,XX;;;;;
                        `````;;XX;;'''''
                             `;;;;'

""")
direction = input("Please Enter direction,(Left or Right ?)")
if(direction.lower() == "left"):
    print("Game Over")
    exit()
elif(direction.lower() == "right"):
    swimwait = input("Do you want to swim or wait?")
    if(swimwait.lower() == "swim"):
        print("Game Over")
        exit()
    elif(swimwait.lower() == "wait"):
        doorcolor = input("Which color door do you want to enter?")
        if(doorcolor.lower() == "red"):
            print("Game Over")
            exit()
        elif(doorcolor.lower() == "blue"):
            print("Game Over")
            exit()
        elif(doorcolor.lower() == "yellow"):
            print("You Win")
            exit()
        else:
            print("You Entered Wrong Color")
            exit()
    else:
        print("You Entered Wrong Option")
        exit()
else:
    print("You Entered Wrong Direction")
    exit()
