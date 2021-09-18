# Yemek Tarifleri Bot'u

Yalnız maddələrinizi yazın və bu bot dərhal uyğun reseptləri tapır!

Bu teleqram botu, artıq mətbəxinizdə olan maddələrdən istifadə edərək Azərbaycan dilində asan reseptlər tövsiyə edir.

İstifadəçi mesajının və mətnimizin nə qədər "yaxın" olduğunu müəyyən etmək üçün mətn oxşarlığı metodundan istifadə etdim. Böyük fikir, sənədləri xüsusiyyətlərin vektorları olaraq təqdim etməyimiz və bu xüsusiyyətlər arasındakı məsafəni ölçərək sənədləri müqayisə etməyimizdir. Bir neçə oxşarlıq üsulunu sınadım, amma bəzi təcrübələrdən sonra Kosinus oxşarlıq metodunu seçdim. Bir verilənlər bazası olaraq, dadli.az veb saytını (2400 + alıcı) tamamilə qırmışam. Məlumat qovluğunda bütün məlumat toplusunu tapa bilərsiniz.

Riyazi cəhətdən Kosinoloji oxşarlıq, aralarındakı bucağın kosinusunu ölçən daxili bir məhsul məkanının iki sıfır olmayan vektoru arasındakı oxşarlıq ölçüsüdür. 0 ° kosinusu 1 -dir və (0, π] radian aralığında olan hər hansı bir bucaq üçün 1 -dən azdır. Bu, böyüklüyün deyil, oriyentasiyanın hökmüdür: eyni istiqamətə malik iki vektorun kosinüs oxşarlığı 1 -dir. , bir -birinə nisbətən 90 ° yönümlü iki vektorun oxşarlığı 0, diametrinin əksinə olan iki vektorun böyüklüyündən asılı olmayaraq -1 oxşarlığı var.

## Məlumat bazasının quruluşu belədir:

__ad -__ _ Yeməyin adı_

__terkibi -__ _ Yeməyin tərkib hissələri_

__hazirlanmasi -__ _Necə edilir_

__img_url -__ _ Yemək görüntüsü_

__label -__ _The type of meal_

__yemek_id -__ _unique identifier of each meal_


## How To Use

İstifadəçi əlində olan maddələri yazanda Keras tərəfindən verilən ```text to word sequence()``` funksiyasından istifadə edərək onu sözlər siyahısına bölürük. Tərəfindən
Varsayılan olaraq, bu funksiya avtomatik olaraq 3 şeyi yerinə yetirir:

- [x] Sözləri məkana görə bölür.

- [y] Durğu işarələrini süzür.

- [z] Mətni kiçik hərflərə çevirir (lower=True).


## S

Arqumentləri funksiyaya ötürərək bu standartlardan hər hansı birini dəyişə bilərsiniz.

İstifadəçi mesajını sözlər siyahısına böldükdən sonra oxşarlıq funksiyamız onu __terkibi__ xüsusiyyəti ilə müqayisə edir və ən oxşar yeməyi təyin edir. Sonra teleqram botumuz bu yeməyin adını, "necə hazırlanacağını" və şəkli istifadəçiyə göndərir. Cavab nümunəsi aşağıda verilmişdir:

![](https://github.com/NijatZeynalov/Easy-Recipes-bot/blob/master/example%20answers/example1.jpeg)

Or

![](https://github.com/NijatZeynalov/Easy-Recipes-bot/blob/master/example%20answers/example2.jpeg)


Hal -hazırda bot mətn oxşarlığı metodundan ötəri bəzən səhv cavablar verə bilər, buna görə də onu istehsala vermədim. Bu layihə davam etdiriləcək, tez -tez cümlə oxşarlığını hesablamağın ən populyar yollarını müqayisə edirəm və necə işlədiklərini araşdırıram.


## Thanks: Nijat for als / Bot rewrite is telethon lab
