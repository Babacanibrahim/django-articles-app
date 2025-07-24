# Django Articles App

Bu proje, Django framework kullanılarak geliştirilmiş basit bir makale uygulamasıdır.  
Kullanıcılar makale ekleyebilir, listeleyebilir ve detaylarını görüntüleyebilir.

---

## Özellikler

- Makale oluşturma, düzenleme ve silme  
- Makalelerin listelenmesi  
- Basit ve kullanıcı dostu arayüz

---

## Kurulum

1. Python ve pip'in yüklü olduğundan emin olun.  
2. Proje klasöründe sanal ortam oluşturun ve aktif edin:

   ```bash
   python -m venv venv
   # Windows:
   source venv/Scripts/activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. Gerekli paketleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. Veritabanı migrasyonlarını uygulayın:

   ```bash
   python manage.py migrate
   ```

5. Sunucuyu başlatın:

   ```bash
   python manage.py runserver
   ```

---

## Kullanım

Tarayıcınızda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) adresine giderek uygulamayı kullanabilirsiniz.

---

## Katkıda Bulunma

Projeye katkıda bulunmak isterseniz, lütfen bir issue açın veya pull request gönderin.

---

## Lisans

MIT Lisansı © 2025