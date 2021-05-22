FROM python:2
COPY . .
ADD name_function.py /
RUN pip install pystrich
CMD [ "python", "./name_function.py"]
