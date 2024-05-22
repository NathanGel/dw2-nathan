@echo
REM Build de Docker Image
docker build -t demo-site-image . 

REM Stop en verwijder de bestaande container 
docker stop demo-site-container
docker rm demo-site-container

REM nieuwe container op poort 81
docker run -d -p 81:81 --name demo-site-container demo-site-image