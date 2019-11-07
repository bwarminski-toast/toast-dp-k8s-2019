FROM python

ADD ./program.py .

CMD [ "python3", "program.py" ]