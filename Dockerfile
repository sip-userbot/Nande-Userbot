FROM nandeuserbotfile/nandeuserbot:python202

COPY . .

RUN pip install -r requirements.txt

CMD ["bash","start.sh"]
