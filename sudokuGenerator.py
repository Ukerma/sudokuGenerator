import random

def seviyeMenu():
    """
    Kullanıcıya sudoku seviyesini seçebilmesi için ekrana bir menü yazdırır.
    """
    print("╔══╣ SUDOKU SEVIYELERI ╠══╗")
    print("║    » 1· Kolay           ║")
    print("║    » 2· Orta            ║")
    print("║    » 3· Zor             ║")
    print("╚═════════════════════════╝\n")


def tahtaOlustur(zorluk):
    """
    Sudoku tahtasını oluşturan ana fonksiyondur.\n
    Random kütüphanesinin eklenmesi gerekir --> import random\n
    İçerisinde sudokuCoz ve sayiSil adında iki yardımcı fonksiyonu çağırarak sudoku tahtasını oluşturur.
    """
    def sudokuCoz(tahta):
        """
        Sudoku tahtasını çözmek için kullanılır.\n
        İlk olarak, boslukBul fonksiyonunu çağırarak boş bir hücre bulur. Eğer boş bir hücre yoksa, sudoku çözülmüştür ve True değerini döndürür.\n
        Boş bir hücre bulunduğunda, bu hücreye 1'den 9'a kadar olan sayıları karışık bir sırayla yerleştirir.\n
        Her sayıyı yerleştirmeden önce, uygunMu fonksiyonu ile bu sayının o satır, sütun ve 3x3'lük küçük kare içinde daha önce kullanılıp kullanılmadığını kontrol eder.\n
        Eğer bu sayı geçerliyse, o sayıyı yerleştirir ve kendisini tekrar ederek sudoku çözümünü devam ettirir.\n
        Eğer bir sayı uygun değilse, bir önceki adıma dönüp farklı bir sayı denemeyi sürdürür.\n
        Eğer sudoku çözülemezse, False değeri döndürür.
        """           
        def boslukBul(tahta):
            """
            Sudoku tahtasında boş bir hücre bulmak için kullanılır.\n
            İki döngü kullanarak tahtayı dolaşır ve ilk boş hücreyi bulduğunda bu hücrenin indisini döndürür.\n
            Eğer boş hücre bulunamazsa None döndürür.
            """
            for satir in range(9):
                for sutun in range(9):
                    if tahta[satir][sutun] == 0:
                        return (satir, sutun)
            return None

        def uygunMu(tahta, satir, sutun, sayi): 
            """
            Belirtilen satır, sütun ve sayının sudoku kurallarına uygun olup olmadığını kontrol eder.\n
            Aynı satırda, sütunda veya 3x3'lük küçük kare içinde aynı sayı bulunuyorsa False döndürür.\n
            Aksi takdirde, sayının kullanılabilir olduğunu belirten True döndürür.
            """
            # tahta: 9x9'luk bir Sudoku tahtasını temsil eden bir liste.
            # satir: Yerleştirilecek sayının bulunduğu satırın indeksi.
            # sutun: Yerleştirilecek sayının bulunduğu sütunun indeksi.
            # sayi: Yerleştirilmek istenen sayı.

            for i in range(9):
                if tahta[satir][i] == sayi or tahta[i][sutun] == sayi or tahta[3 * (satir // 3) + i // 3][3 * (sutun // 3) + i % 3] == sayi:
                    return False
            return True

        bos = boslukBul(tahta)
        if not bos:
            return True

        satir, sutun = bos
        sayilar = list(range(1, 10))
        random.shuffle(sayilar)

        for sayi in sayilar:
            if uygunMu(tahta, satir, sutun, sayi):
                tahta[satir][sutun] = sayi
                if sudokuCoz(tahta):
                    return True
                tahta[satir][sutun] = 0
        return False

    def sayiSil(tahta, silinecekSayi):
        """
        Seçilen sayı kadar rastgele hücreyi silerek sudoku tahtasını oluşturur.\n
        İlk olarak, tüm hücrelerin indislerini içeren bir liste oluşturur ve bu listeyi karıştırır.\n
        Karıştırılmış liste üzerinden belirtilen sayıda hücreyi silecek şekilde tahtayı günceller.\n
        Silinen hücreler, geçici bir tahta üzerinde çözülerek sudoku tahtasının geçerliliği kontrol edilir.\n
        Eğer çözülemezse, silinen hücreler geri eklenir.
        """
        pozisyonlar = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(pozisyonlar)
        for pozisyon in pozisyonlar[:silinecekSayi]:
            temp = tahta[pozisyon[0]][pozisyon[1]]
            tahta[pozisyon[0]][pozisyon[1]] = 0
            geciciTahta = [list(satir) for satir in tahta]
            if not sudokuCoz(geciciTahta):
                tahta[pozisyon[0]][pozisyon[1]] = temp

    tahta = [[0] * 9 for ignored in range(9)]
    sudokuCoz(tahta)
    kolaySilinecek = random.randint(22,25)
    ortaSilinecek = random.randint(28,32)
    zorSilinecek = random.randint(41,44)
    if zorluk == "1":
        sayiSil(tahta, kolaySilinecek)
    elif zorluk == "2":
        sayiSil(tahta, ortaSilinecek)
    elif zorluk == "3":
        sayiSil(tahta, zorSilinecek)
    return tahta


def tahtayiYazdir(tahta):   
    """
    Bu fonksiyon, sudoku tahtasını ekrana yazdırmak için kullanılır.\n
    İki döngü kullanarak, satır ve sütunları dolaşır.\n
    Satırın her üçüncü elemanı ve sütunun her üçüncü elemanından sonra birer dikey çizgi ekleyerek sudoku tahtasının bölümlerini belirtir.\n
    Boşlukları ve sayıları uygun biçimde ekrana yazdırır.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("════════════╬═════════════╬════════════")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("║", end=" ")
            print("", tahta[i][j], end="  ")
        print()


def dosyayaYaz(tahta, dosya_adı="sudoku.txt"):
    """
    Sudoku tahtasını seçilen zorluk seviyesine bağlı olarak dosyaya yazan bir fonksiyondur.\n
    dosya_adı argümanı, tahtanın kaydedileceği dosyanın adını belirtir. Bu da zorluk seviyesine göre değişir.\n
    """
    with open(dosya_adı, "a", encoding="utf-8") as dosya:
        dosya.write("═════════╦═════════╦═════════\n")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                dosya.write("═════════╬═════════╬═════════\n")
            
            dosya.write("  ")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    dosya.write(" ║  ")
                dosya.write(f"{tahta[i][j]:^2}")  
            dosya.write(" \n")

            if i == 8:
                dosya.write("═════════╩═════════╩═════════\n\n")

    print(f"» Sudoku şablonu {dosya_adı} dosyasına kaydedildi.")


######### ANA PROGRAM ##########


seviyeMenu() 
zorluk = -1
while zorluk not in ["1", "2", "3"]:
    zorluk = input("» Sudoku seviyesini secin: ")
    print()
    if zorluk not in ["1", "2", "3"]:
        print("» Geçersiz seviye seçimi, tekrar seçim yapın.\n")
        seviyeMenu()
sudokuTahta = tahtaOlustur(zorluk)
print("════════════╦═════════════╦════════════")
tahtayiYazdir(sudokuTahta)
print("════════════╩═════════════╩════════════")

while True:
    kaydet = input("» Tahtayı kaydetmek ister misiniz? (Evet/Hayır): ").strip().lower()

    if kaydet == "evet":
        dosya_adı = ""
        if zorluk == "1":
            dosya_adı = "kolay.txt"
        elif zorluk == "2":
            dosya_adı = "orta.txt"
        elif zorluk == "3":
            dosya_adı = "zor.txt"
        
        dosyayaYaz(sudokuTahta, dosya_adı)
        break
    elif kaydet == "hayır":
        print("Tahta kaydedilmedi. Programdan Çıkılıyor. . .")
        break
    else:
        print("» Geçersiz cevap. Lütfen 'Evet' veya 'Hayır' olarak cevap verin.")