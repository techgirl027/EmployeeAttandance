# crm app

Bu kafe restoran xodimlarini boshqarish uchun web ilova

## ishga tushirish

Virtual muhit yaratamiz

```bash
  python -m venv env
```

Virtual muhitni aktivlashtiramiz

- windows

```bash
    env\Scripts\activate
```

- linux/mac

```bash
    source env/bin/activate
```

Kerakli kutubxonalar o'rnatamiz

```bash
    pip install -r requirements.txt
```

Migratsiyalarni amalga oshiramiz

```bash
    python manage.py migrate
```

Dasturni ishga tushiramiz

```bash
    python manage.py runserver
```

Dastur ishga tushdi uni browserda `http.//127.0.0.1:8000` ochish mumkin
