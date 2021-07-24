# pvp-backend
Package Volume Prediction Backend


## How to run

First, copy the model and tokenizer files from https://drive.google.com/drive/u/1/folders/1EqoXd99F12-Em43C2C4K-FbrgH94EFkr to your working copy.
Then, configure it in the src/.env file

### Local
```bash
pip install --user -r requirements.txt
cd src
uvicorn main:app --reload 
```


### Docker
```bash
docker build -t pvp-backend .
docker run -ti --rm -p 8080:80 pvp-backend
```
