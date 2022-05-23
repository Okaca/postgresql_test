# postgresql_test

Çalışma :

 

Uygulama Çalışması:
 

Obje :

 

Name string

Lastname string

Adres string

Birthday date

Latitude decimal (18,16)

Longtidude decimal (18,16)
 

 

Yukarıdaki modele göre random veri üretip bir api üzerine json olarak bu gönderebilen python uygulamasının yazılması. Uygulama kapatılıncaya kadar veri üretiminin ve api call işleminin devam etmesi gerekmektedir.

 

API Çalışması
Uygulama üzerinden gelen json nesnesini postgre veritabanı kullanılarak bir objeye yazılmasının sağlanması.

 

 

Kısacası bir uygulama ile random veri üretip json nesenesi oluşturup yazmış olduğunuz API üzerine bu veriyi göndermenizi ve gönderdiğiniz veriyi API tarafından DB üzerindeki objeye kayıt edilmesi bekleniyor.


app.py : Flask API kurulumu

postRandomData.py : localhost üzerine API açık olduğu sürece (HEAD gönderildiği zaman request statusü 200 döndüğü sürece) ürettiği random datayı gönderen fonksiyon

db.py : oluştutulan Postgresql DB

getData.py : API üzerine en son düşen random datayı çekip db.py ile oluşturulan ilgili columnlara dizen fonksiyon
