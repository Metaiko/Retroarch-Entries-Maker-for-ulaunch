from os import listdir, makedirs
from os.path import isfile, join, exists
from shutil import copyfile, rmtree

#suppression des anciens fichier
if exists(r"output/Roms"):
    suppr = input('"output/" folder contain data from a previous session.\n'+
                  "Do you want to delete these data? (y/n) : ")
    while True:
        if suppr.lower() == "y":
            rmtree(r"output/Roms",ignore_errors=True)
            rmtree(r"output/ulaunch",ignore_errors=True)
            input("all data has been successfully deleted! Press Enter to continue...")
            break
        elif suppr.lower() == "n":
            break
        else:
            suppr = input("Error! Please, enter a valid character.\n"+
                          "Do you want to delete these data? (y/n) : ")
#création du dossier ulaunch s'il n'existe pas
if not exists(r"output/ulaunch/entries"):
    makedirs(r"output/ulaunch/entries")

Extension = {
        ".dsk":("Amstrad CPC","sdmc:/retroarch/cores/crocods_libretro_libnx.nro","Amstrad"),
        ".sna":("Amstrad CPC","sdmc:/retroarch/cores/crocods_libretro_libnx.nro","Amstrad"),
        ".kcr":("Amstrad CPC","sdmc:/retroarch/cores/crocods_libretro_libnx.nro","Amstrad"),
        ".exe":("DOS","sdmc:/retroarch/cores/dosbox_svn_libretro_libnx.nro","IBM"),
        ".com":("DOS","sdmc:/retroarch/cores/dosbox_svn_libretro_libnx.nro","IBM"),
        ".bat":("DOS","sdmc:/retroarch/cores/dosbox_svn_libretro_libnx.nro","IBM"),
        ".conf":("DOS","sdmc:/retroarch/cores/dosbox_svn_libretro_libnx.nro","IBM"),
        ".rom":("MSX","sdmc:/retroarch/cores/fmsx_libretro_libnx.nro","Microsoft"),
        ".mx1":("MSX","sdmc:/retroarch/cores/fmsx_libretro_libnx.nro","Microsoft"),
        ".mx2":("MSX","sdmc:/retroarch/cores/fmsx_libretro_libnx.nro","Microsoft"),
        ".cas":("MSX","sdmc:/retroarch/cores/fmsx_libretro_libnx.nro","Microsoft"),
        ".int":("Intellivision","sdmc:/retroarch/cores/freeintv_libretro_libnx.nro","Mattel"),
        ".nes":("NES","sdmc:/retroarch/cores/nestopia_libretro_libnx.nro","Nintendo"),
        ".fds":("NES","sdmc:/retroarch/cores/nestopia_libretro_libnx.nro","Nintendo"),
        ".smc":("SNES","sdmc:/retroarch/cores/snes9x_libretro_libnx.nro","Nintendo"),
        ".sfc":("SNES","sdmc:/retroarch/cores/snes9x_libretro_libnx.nro","Nintendo"),
        ".swc":("SNES","sdmc:/retroarch/cores/snes9x_libretro_libnx.nro","Nintendo"),
        ".gba":("GBA","sdmc:/retroarch/cores/mgba_libretro_libnx.nro","Nintendo"),
        ".gbc":("GBC","sdmc:/retroarch/cores/gearboy_libretro_libnx.nro","Nintendo"),
        ".cgb":("GBC","sdmc:/retroarch/cores/gearboy_libretro_libnx.nro","Nintendo"),
        ".sgb":("GBC","sdmc:/retroarch/cores/gearboy_libretro_libnx.nro","Nintendo"),
        ".gb":("GB","sdmc:/retroarch/cores/gearboy_libretro_libnx.nro","Nintendo"),
        ".dmg":("GB","sdmc:/retroarch/cores/gearboy_libretro_libnx.nro","Nintendo"),
        ".sms":("Master System","sdmc:/retroarch/cores/gearsystem_libretro_libnx.nro","Sega"),
        ".gg":("GameGear","sdmc:/retroarch/cores/gearsystem_libretro_libnx.nro","Sega"),
        ".sg":("Genesis","sdmc:/retroarch/cores/gearsystem_libretro_libnx.nro","Sega"),
        ".smd":("Genesis","sdmc:/retroarch/cores/genesis_plus_gx_libretro_libnx.nro","Sega"),
        ".gen":("Genesis","sdmc:/retroarch/cores/genesis_plus_gx_libretro_libnx.nro","Sega"),
        ".md":("Megadrive","sdmc:/retroarch/cores/genesis_plus_gx_libretro_libnx.nro","Sega"),
        ".chd":("MAME","sdmc:/retroarch/cores/mame2003_plus_libretro_libnx.nro","Arcade"),
        ".n64":("N64","sdmc:/retroarch/cores/mupen64plus_next_libretro_libnx.nro","Nintendo"),
        ".v64":("N64","sdmc:/retroarch/cores/mupen64plus_next_libretro_libnx.nro","Nintendo"),
        ".z64":("N64","sdmc:/retroarch/cores/mupen64plus_next_libretro_libnx.nro","Nintendo"),
        ".u1":("N64","sdmc:/retroarch/cores/mupen64plus_next_libretro_libnx.nro","Nintendo"),
        ".ndd":("N64","sdmc:/retroarch/cores/mupen64plus_next_libretro_libnx.nro","Nintendo"),
        ".bin":("PS1","sdmc:/retroarch/cores/pcsx_rearmed_libretro_libnx.nro","Sony"),
        ".img":("PS1","sdmc:/retroarch/cores/pcsx_rearmed_libretro_libnx.nro","Sony"),
        ".min":("Pokemon Mini","sdmc:/retroarch/cores/pokemini_libretro_libnx.nro","Nintendo"),
        ".a78":("Atari 7800","sdmc:/retroarch/cores/prosystem_libretro_libnx.nro","Atari"),
        ".a26":("Atari 2600","sdmc:/retroarch/cores/stella_libretro_libnx.nro","Atari"),
        ".vec":("Vectrex","sdmc:/retroarch/cores/vecx_libretro_libnx.nro","Smith Engineering"),
        ".ccd":("Saturn","sdmc:/retroarch/cores/yabause_libretro_libnx.nro","Sega"),
        ".mds":("Saturn","sdmc:/retroarch/cores/yabause_libretro_libnx.nro","Sega"),
        ".iso":("PSP","sdmc:/retroarch/cores/ppsspp_libretro_libnx.nro","Sony"),
        ".cso":("PSP","sdmc:/retroarch/cores/ppsspp_libretro_libnx.nro","Sony")
        }
game_path = input(r"Enter your roms directory: ")
cpt = 0
nb_file = 0

#nombre de fichiers dans le dossier sélectionné :
for element in listdir(game_path):
    if isfile(join(game_path, element)):
        for val in Extension.keys():
            if val in element:
                nb_file += 1
                break
for file in listdir(game_path):
    if isfile(join(game_path, file)):
        #reset des variables
        name = ""
        platform = ""
        #détermine la plateforme en fonction de l'extension et retire l'extension du fichier
        ext = "."+file.split(".")[-1]
        name = file.replace(ext,"")
        if ext in Extension:
            rom_info = Extension[ext]
            platform = rom_info[0]
            nro_path = rom_info[1]
            author = rom_info[2]
        else:
            print(file+" isn't a rom file!")
            continue
        new_file_name = file.split("-",1)[-1].replace(" ","_")
        cpt+=1
        #création du dossier des roms et des icones s'ils n'existent pas
        if not exists(r"output/Roms/"+platform+"/Icons"):
            makedirs(r"output/Roms/"+platform+"/Icons")
        #récupère et renomme l'image associée à la rom
        if exists(game_path+"/Icons/"+str(cpt)+".png"):
            copyfile(game_path+"/Icons/"+str(cpt)+".png",
                     r"output/Roms/"+platform+"/Icons/"+new_file_name+
                     ".png")
        else:
            print("Error! "+str(cpt)+".png not found in the Icons directory!"+
                  " Please, check ReadMe.txt!")
        #copier la rom dans dans le dossier output
        copyfile(game_path+"/"+file,"output/Roms/"+
                 platform+"/"+new_file_name)
        #création de l'entrée du jeu
        entry = open(r"output/ulaunch/entries/"+name+".json","w+")
        entry.write('{\n'+
                      '  "madeby": "Retroarch_Entry_Maker",\n'+
                      '  "type": 2,\n'+
                      '  "nro_path": "'+nro_path+'",\n'+
                      '  "nro_argv": "sdmc:/Roms/'+platform+'/'+new_file_name+'",\n'+
                      '  "name": "'+name.split("-",1)[-1]+'",\n'+
                      '  "author": "'+author+'",\n'+
                      '  "version": "'+platform+'",\n'+
                      '  "icon": "sdmc:/Roms/'+platform+'/Icons/'+new_file_name+'.png",\n'+
                      '  "folder": "'+platform+'"\n'+
                      '}')
        entry.close()
        print(str(cpt)+"/"+str(nb_file))
print(input("Done!"))
