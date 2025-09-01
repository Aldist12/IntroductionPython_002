def nama_kota(kota="Yogyakarta"):
    if len(kota) < 4:
        raise ValueError("nama kota terlalu pendek.")
    
    print(f"Selamat datang di {kota}!")
