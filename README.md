# WordCount-in-Google-Corpus
Word Count del Corpus de Google (Solo 5GB de los datos) con threads 

Se tienen dos scripts principales
- WordCount.py -> que ejecuta todo con 8 threads al mismo tiempo y un joiner que va agregando los datos de estos threads a un diccionario global una vez acaben de ejecutarse.
- WordCountProcess.py -> que hace lo mismo pero con procesos.

El dataset cuenta con 32 archivos del corpus de Google, existen pocas repeticiones por palabra por lo que el trabajo será más pesado.

Los archivos de este dataset deben guardarse en una carpeta llamada Datos y los resultados se almacenarán tras ejecutar cualquier script en una carpeta llamada resultados.

Las capturas del programa se adjuntará a una carpeta llamada Capturas de ejecución.

Este trabajo fue realizado por Ricardo Manuel Lazo Vásquez para el curso de Cloud Computing UCSP.

GitHub: https://github.com/TheReverseWasp/WordCount-to-Google-Corpus

Demo: https://youtu.be/apg5lyy83Hc
