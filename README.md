# AutomataToolkit

AutomataToolkit es una herramienta que toma expresiones regulares desde un archivo de texto y las procesa una por una, transformándolas en Autómatas Finitos Deterministas (AFD) minimizados. A través de varios pasos, que incluyen la conversión de la expresión regular a postfix, la construcción de un Autómata Finito No Determinista (AFN), su conversión a un AFD y finalmente la minimización de este, la herramienta genera representaciones gráficas y simulaciones del autómata resultante.

## Tabla de contenidos
*   [Características](#caracter%C3%ADsticas)
*   [Instalación](#instalaci%C3%B3n)
*   [Uso](#uso)
*   [Archivos generados](#archivos-generados)
*   [Dependencias](#dependencias)

## Características
- Convierte expresiones regulares a postfix.
- Genera Autómatas Finitos No Deterministas (AFN) a partir del postfix utilizando el algoritmo de Thompson.
- Convierte AFNs a Autómatas Finitos Deterministas (AFD) mediante el algoritmo de Subconjuntos.
- Minimiza el AFD utilizando un algoritmo de minimización.
- Genera y guarda gráficos de los AFN, AFD y AFD minimizados.
- Procesa múltiples expresiones desde un archivo de texto.
- Simula el comportamiento de cada autómata con cadenas de entrada proporcionadas por el usuario.

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/AutomataToolkit.git
   cd AutomataToolkit
2. Instalar Graphviz para la generación de gráficos:
   
   - En Linux: sudo apt-get install graphviz
   - En macOS: brew install graphviz
   - En Windows: Descargar desde Graphviz website.

## Uso

1. Proporcionar un archivo con expresiones regulares:

Crea un archivo de texto (por ejemplo, expresiones.txt) donde cada línea contenga una expresión regular que desees procesar.

2. Ejecuta el programa

```bash
  python main.py
```
El programa procesará las expresiones una por una, generando un AFN, AFD y AFD minimizado para cada una.

3. Ejemplo de archivo de expresiones
```bash
  a*|b*
(a|b)c*
b+abc+
```

## Archivos generados

AutomataToolkit generará los siguientes archivos de salida en la carpeta Resultados/:

- AFNout.txt: Información sobre el AFN generado para cada expresión.
- AFDout.txt: Información sobre el AFD generado por el algoritmo de subconjuntos.
- AFDMINout.txt: Información sobre el AFD minimizado.
- PostfixOut.txt: Las expresiones convertidas a postfix.
- AFN1.png, AFD1.png, AFDMIN1.png: Imágenes del AFN, AFD y AFD minimizado, respectivamente, para cada expresión procesada.

## Dependencias

- Python 3.x
- Graphviz (para la generación de gráficos)
- Librerías Python:
  - graphviz
  - collections
  - sys

