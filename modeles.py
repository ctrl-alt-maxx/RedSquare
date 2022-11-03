import c31Geometry2 as c31

class Rectangle:
    # Création des rectangles
    # 1. Rectangle bleu gauche
    rectangle1 = c31.Rectangle(canvasBase, c31.Vecteur(100, 100), 60, 60, remplissage="mediumblue")
    rectangle1.draw()

    # 2. Rectangle bleu superieur droit
    rectangle2 = c31.Rectangle(canvasBase, c31.Vecteur(300, 85), 60, 50, remplissage="mediumblue")
    rectangle2.draw()

    # 3. Rectangle bleu inferieur gauche 
    rectangle3 = c31.Rectangle(canvasBase, c31.Vecteur(85, 350), 30, 60, remplissage="mediumblue")
    rectangle3.draw()

    # 4. Rectangle bleu infereieur droit 
    rectangle4 = c31.Rectangle(canvasBase, c31.Vecteur(355, 340), 100, 20, remplissage="mediumblue")
    rectangle4.draw()