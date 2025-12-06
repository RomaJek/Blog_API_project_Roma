# 1. Base Image: Python 3.9 din jenil (slim) versiyasin alamiz
FROM python:3.10-slim


# 2. Python ortaliq ozgeriwshileri (optimizaciya)
#  .pyc fayllardi jazbaw ushin (diskke jaziwdi azaytadi)
ENV PYTHONDONTWRITEBYTECODE 1

# Loglardi buferlemey, tikkeley terminalga shigariw ushin
ENV PYTHONUNBUFFERED 1


# 3. Jumis papkasi: Konteyner ishindegi /app papkasinda isleydi
WORKDIR /app


# 4. Kitapxanalardi ornatiw
# Daslep tek requirements.txt faylin koshiremiz (Keshlew ushin paydali)
COPY requirements.txt .
# pip di janalap, kitapxanalardi ornatamiz
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Kodti koshiriw
# Qalgan barliq fayllardi konteynerge koshiremiz 
COPY . .
RUN python manage.py migrate
RUN pip install gunicorn
# 6. Iske tusiriw buyrigi 
# Serverde runserver EMES, Gunicorn isletiw kerek
# config - bul sizin joybarinizdin settings.py turgan papka ati
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]


