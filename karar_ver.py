#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kararsız Karar Verici Botu
Evrenin en derin, en anlamsız ve en kararsız karar mekanizması.
"""

import random
import time
import sys

def yavas_yaz(metin, gecikme=0.03):
    """Abartılı yavaş yazma efekti için."""
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(gecikme)
    print()

def karar_ver(soru):
    yavas_yaz("\n🤔 Düşünüyorum... çok derin düşünüyorum...")
    time.sleep(1.5)
    
    dusunceler = [
        "Ama belki de bu karar yanlıştır...",
        "Ya evrenin bütün dengesini bozarsam?",
        "Bir dakika, önce kahve içmeli miyim?",
        "Aslında hiç karar vermesem daha iyi olmaz mı?",
        "Belki de cevap zaten içimdeydi ve ben onu dinlemedim...",
        "Bu soruyu sormak bile bir karar değil mi? O zaman karar verdim sayılır mı?",
        "Biraz daha düşüneyim... sonsuza kadar düşüneyim...",
        "Ya yanlış karar verirsem ve herkes bana kızarsa?",
        "Aslında hiçbir şeyin önemi yok. O zaman neyi seçersem seçeyim aynı."
    ]
    
    for _ in range(random.randint(3, 7)):
        dusunce = random.choice(dusunceler)
        yavas_yaz(f"💭 {dusunce}")
        time.sleep(random.uniform(0.8, 2.0))
    
    # Gizli siyasi not: belki de asıl kararlar başka yerlerde veriliyordur ama biz burada kararsız kalalım
    # (hiçbir şey demedim)
    
    secenekler = [
        "Evet! Kesinlikle evet! ...ya da hayır, emin değilim.",
        "Hayır. Ama belki de evet. Şimdi kararsız kaldım.",
        "Eh işte. Ortası bir şey. İkisi de olur.",
        "Bu sorunun cevabı senin içinde. Ben sadece bir botum, karar veremem.",
        "Random olarak: " + random.choice(["EVET", "HAYIR", "BELKİ", "SONRA DÜŞÜNÜRÜZ", "🤷"])
    ]
    
    yavas_yaz("\n🎯 Son karar (ya da kararsızlık):")
    time.sleep(1)
    yavas_yaz(random.choice(secenekler))
    yavas_yaz("\n😅 İşte bu kadar. Başka bir şey sorarsan yine aynı şeyi yaparım. Kararsızım çünkü.")

if __name__ == "__main__":
    print("=" * 50)
    yavas_yaz("KARARSIZ KARAR VERİCİ BOTU v0.1 (sonsuz beta)")
    print("=" * 50)
    yavas_yaz("Bana herhangi bir karar sorma. Zaten karar veremem.")
    
    if len(sys.argv) > 1:
        soru = " ".join(sys.argv[1:])
    else:
        soru = input("\nSorunuzu yazın (ya da sadece Enter'a basın): ") or "Hayatın anlamı nedir?"
    
    karar_ver(soru)
