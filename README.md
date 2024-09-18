# AutoClickPattern

Questo script Python esegue uno screenshot del tuo schermo ogni 5 secondi e cerca un'immagine specifica all'interno dello screenshot. Se l'immagine viene trovata, il mouse viene spostato al centro della posizione dell'immagine e viene effettuato un clic.

## Funzionalità

- Esegue screenshot periodici.
- Cerca un'immagine di riferimento all'interno dello screenshot.
- Clicca automaticamente al centro dell'immagine trovata.
- Restituisce la confidenza massima anche quando non trova l'immagine.

## Prerequisiti

### 1. Dipendenze su Ubuntu

Assicurati di avere Python 3.10 e le librerie necessarie installate:

```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip scrot
```

- `scrot` è necessario per gli screenshot con `pyautogui`.
- Python 3.10 è la versione utilizzata nel progetto.

### 2. Dipendenze Python

Crea un ambiente virtuale Python e installa le dipendenze:

```bash
python3.10 -m venv env
source env/bin/activate
pip install pyautogui opencv-python pillow numpy
```

Oppure, puoi usare **Nix** per gestire l'ambiente di sviluppo (vedi la sezione [Utilizzo con Nix](#utilizzo-con-nix)).

## Come eseguire lo script

1. Inserisci l'immagine che desideri cercare nella directory del progetto. In questo caso, l'immagine deve essere chiamata `image1.png`.
2. Esegui lo script Python:

```bash
python3 autoclick.py
```

Lo script inizierà a eseguire screenshot ogni 5 secondi e cercherà l'immagine `image1.png` sullo schermo. Se viene trovata, il mouse verrà spostato al centro dell'immagine e verrà eseguito un clic.

### Modifica della soglia di confidenza

Puoi modificare la soglia di confidenza nel codice per renderlo più o meno preciso. Il valore di default è `0.8`.

```python
threshold = 0.8
```

## Utilizzo con Nix

Se preferisci usare **Nix** per la gestione delle dipendenze e dell'ambiente di sviluppo, puoi sfruttare il file `flake.nix` incluso.

### Come configurare e avviare con Nix

1. Installa **Nix** seguendo le istruzioni sul sito ufficiale: [https://nixos.org/download.html](https://nixos.org/download.html).
2. Dopo aver installato Nix, esegui il seguente comando per entrare nell'ambiente di sviluppo con tutte le dipendenze già configurate:

```bash
nix develop
```

3. Una volta dentro l'ambiente Nix, esegui lo script Python come al solito:

```bash
python3 autoclick.py
```

## Autore

Realizzato da Nebulus.

## Licenza

Questo progetto è distribuito sotto licenza MIT.
