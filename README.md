# Dokumentation 
## Wichtige Variablen
```isAlive```       gibt an, ob der Spieler lebt, und ob das Spiel weiterlaufen soll.  
```foodCords```     die Position, auf der der einzusammelnde Punkt liegt.  
```snake```         ein Array, welches die Koordinaten der einzelnden Schlangenelemente beinhaltet. snake[0] ist der Kopf der Schlange.  
```playerDirection```    Die Richtung in die sich die Schlange beim nächsten Zug bewegt.  
```gameField```          Ein 2D-Array, welches das Spielfeld darstellt.
```ateFood```            Zeigt, ob im letzten Zug ein Punkt gesammelt wurde.
```head_position```      Die Position des Kopfs.  
  
## Wichtige Klassen
> [!CAUTION]
> Da ich mich inmitten des Programmierens die Art und Weise meines Vorgehens geändert habe,
> werden einige Klassen oder Teile davon nicht verwendet.
### Direction
Speichert eine Richtung
### Coordinates
Zwei Integer, die Koordinaten darstellen
### GameFieldObject
Ein Feld auf der Spielfläche.
Enthält seine eigenen Koordinaten, welchem Typ es entspricht, und, wenn nötig, eine Richtung.
### GameFieldObjectType
Bestimmt, was ein GameFieldObject enthält.
## Funktionen  
### ```main()```
Der Kern des Programms. Diese Funktion hat verschiedene Aufgaben:
 - Das Zeichnen der Grafik. Die gespeicherten Koordinaten aus ```gameField``` werden im Fenster als Quadrate mit verschiedenen Farben gezeichnet.  
 - Die Geschwindigkeit der Schlange anpassen, indem die Zeit zwischen den Aufrufen von ```update_game_logic``` verkürzt wird.  
 - Prüfen, ob die Schlange einen Punkt gesammelt hat. Wenn ja, wird ```new_food``` aufgerufen, um einen neuen Punkt zu generieren, und der Score/die Schlangenläng wird um 1 inkrementiert.  
 - 
### ```handle_input()```
Diese Funktion verarbeitet Eingaben, und setzt ```playerDirection``` auf die Eingabe des Nutzers.
### ```update_game_logic()```
Diese Funktion bewegt die Schlange auf dem Feld.
Ausserdem prüft sie, ob die Schlange die Wand trifft. Wenn ja, wird ```alive``` = False gesetzt.
### ```new_food()```
Generiert zwei zufällige Zahlen, erstellt daraus ein Coordinate-Objekt, und prüft, ob dieses NICHT mit der Schlange kollidiert.
Ist das der Fall, wird ```foodCords``` auf das Coordinate-Objekt gesetzt.
Sonst wird das Generieren so lange wiederholt, bis die Stelle frei ist.
