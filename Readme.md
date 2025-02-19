# Weather App

a weather app made whit flask to learn flask
```
docker build -t weather_app:1 .       
```
```
docker run -p 8080:8080  weather_app:1
```



```
docker run -p 8080:8080 -v $(pwd)/data:/app/data weather_app:1
``` 

rajout de dans le code pour voir les log avec un volume docker :

DATA_DIR = "/app/data"
os.makedirs(DATA_DIR, exist_ok=True) 