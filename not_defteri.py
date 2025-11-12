def not_defteri():
    while True:
        print("   NOT DEFTERİ")
        print("1:notları listele")
        print("2:not ekle")
        print("3:notları sil")
        print("4.çıkış")

        secim=int(input("seçiminizi yapın:"))

        if secim==1:
            print("Notlar:")
            try:
                with open("notlar.txt","r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("henüz not eklenmemiş")

        elif secim==2:
            not_metni=input("notunuzu girin:")
            with open("notlar.txt","a") as file:
                file.write(not_metni+"\n")
            print("not başarıyla kaydedildi")

        elif secim==3:
            print("notlarınız siliniyor")
            try:
                with open("notlar.txt","w") as file:                
                    pass  
                print("notlar silindi")
            except FileNotFoundError:
                print("henüz not eklenmemiş")

        else:
            print("sistemden çıkılıyor")
            break
not_defteri()
