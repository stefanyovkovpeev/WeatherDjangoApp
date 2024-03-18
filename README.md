A django weather app that has a generation of the weather conditions in 5 random cities in the world and avarages derived from that.Also a search bar for individual searches and a comparison page for the last ten saved results in the database.
The generate button generates random cities. And the refresh button refreshes the weather and uploads it in a database to be shown and compared on the comparison page.
Contact me for a .env file

has also its own docker image, contact me for an api key for openweathermap.com
docker run -d -p 8000:8000 -e "API=key" stefpeev/djangoweatherapp:latest

Django Приложение за времето, което има генериране на метеорологичните условия в 5 произволни града в света и средни стойности между тях. Също така лента за търсене за индивидуални търсения и страница за сравнение 
на 5те града за последните десет запазени резултата в базата данни.
Бутонът Generate генерира произволни градове. А бутонът refresh, опреснява времето и го качва в база данни, за да бъде показано и сравнено на страницата за сравнение.
Свържете се с мен за .env файл

също има свой собствен докер image, свържете се с мен за api ключ за openweathermap.com
docker run -d -p 8000:8000 -e "API=key" stefpeev/djangoweatherapp:latest
