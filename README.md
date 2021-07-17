# pvp-backend
Package Volume Prediction Backend


## How to run
```bash
pip install --user -r requirements.txt
cd src
uvicorn main:app --reload 
```


## How to run with docker
```bash
docker build -t pvp-backend .
docker run -ti --rm -p 8080:80 pvp-backend
```
