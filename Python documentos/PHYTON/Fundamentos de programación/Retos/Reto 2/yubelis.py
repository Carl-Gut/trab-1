import math
v_cant_zonas=int(input("Cuantas zonas desea analizar?: "))
if v_cant_zonas>0:
    i=1
    totalant=0
    totaltipoa=0
    totaltipob=0
    totaltipoc=0
    totaltipod=0
    totaltipoe=0
    while i<=v_cant_zonas:
        v1_area_zona=float(input("Area: "))
        v2_ant_ins=int(input("Antenas instaladas: "))
        v3_tipo=input("Tipo antena: ")
        if v1_area_zona>0 and v2_ant_ins>=0:
            if v3_tipo=="a":
                res=math.ceil((v1_area_zona-(v2_ant_ins*3000))/800)
                totaltipoa+=res
            elif v3_tipo=="b":
                res=math.ceil((v1_area_zona-(v2_ant_ins*3000))/52900)
                totaltipob+=res
            elif v3_tipo=="c":
                res=math.ceil((v1_area_zona-(v2_ant_ins*3000))/7500)
                totaltipoc+=res
            elif v3_tipo=="d":
                res=math.ceil((v1_area_zona-(v2_ant_ins*3000))/35600)
                totaltipod+=res
            elif v3_tipo=="e":  
                res=math.ceil((v1_area_zona-(v2_ant_ins*3000))/49800)
                totaltipoe+=res
            else:
                res=0
        else:
            res=0
        totalant=totalant+res
        i=i+1
else:
    res=0

if res<=0:
    res=0
    print(res)
    print("a " + "0.00%")
    print("b " + "0.00%")
    print("c " + "0.00%")
    print("d " + "0.00%")
    print("e " + "0.00%")
else:
    print(math.ceil(totalant))
    porcentajea=float(totaltipoa*100)/totalant
    porcentajeb=float(totaltipob*100)/totalant
    porcentajec=float(totaltipoc*100)/totalant
    porcentajed=float(totaltipod*100)/totalant
    porcentajee=float(totaltipoe*100)/totalant
    print("a {:.2f}".format(porcentajea)+"%")
    print("b {:.2f}".format(porcentajeb)+"%")
    print("c {:.2f}".format(porcentajec)+"%")
    print("d {:.2f}".format(porcentajed)+"%")
    print("e {:.2f}".format(porcentajee)+"%")
