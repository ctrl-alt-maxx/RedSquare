from controlleurs import MenuController, JeuController

if __name__ == "__main__" :
    askToQuit = False
    while not askToQuit :
        controler = MenuController()
        choix = controler.start()
        if choix == "Facile" :
            controler = JeuController()
            controler.start()
        if choix == "Moyen" :
            controler = JeuController()
            controler.start()
        if choix == "Difficile" :
            controler = JeuController()
            controler.start()
        elif choix == "Quitter" :
            askToQuit = True