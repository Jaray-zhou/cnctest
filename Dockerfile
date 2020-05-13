FROM python
MAINTAINER Jaray Zhou
ADD . /python3-app/cnctest
WORKDIR /python3-app/cnctest
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["test.py"]
