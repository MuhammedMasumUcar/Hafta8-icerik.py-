def unlu_bul(a):
  kelime_sayac=0
  harf_sayac=0
  cumle=a.split(" ")
  cumlesayac=0
  paragrafcumle=a.split(".")
  for cumlesayisi in paragrafcumle:
   cumlesayac+=1
  for kelime in cumle:
    kelime_sayac+=1
    for harf in kelime:
      if(harf=="a" or harf=="e" or harf=="ı" or harf=="i" or harf=="ö" or harf=="o" or harf=="ü" or harf=="u" or harf=="ı"):
        harf_sayac+=1
  print("Paragraftaki Cümle Sayısı",cumlesayac-1)
  print("Kelime Sayısı : ",kelime_sayac)
  print("Ünlü Harf Sayısı : ",harf_sayac)
unlu_bul("Güneş sabah erken saatlerde doğdu ve gökyüzünü altın sarısına boyadı. Kuşlar neşeyle ötmeye başladı. İnsanlar yavaş yavaş uyanıyor, yeni bir güne hazırlanıyordu. Kahveciler dükkanlarını açarken mis gibi kahve kokusu sokaklara yayılıyordu. Çocuklar okula gitmek için evlerinden çıkıyordu. Herkesin yüzünde hafif bir telaş ve heyecan vardı. Şehir, sabahın enerjisiyle canlanıyordu. Parkta yürüyüş yapan insanlar güne zinde başlamanın keyfini çıkarıyordu. Hava serin ama güneşliydi, bu da günü daha güzel hale getiriyordu. Herkes kendi hayatına dair yeni bir sayfa açmak ister gibiydi.")