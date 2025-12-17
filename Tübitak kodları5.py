class AkilliTarimSistemi:
    def __init__(self):
        self.bolgeler = {
            "Antalya": {
                "ETo_aylik": [52.4, 54.6, 81.5, 102.3, 133.3, 171.6, 204.6, 190.3, 153.9, 107.9, 66.3, 50.2],
                "Peff_aylik": [147.3, 132.6, 85.02, 44.23, 26.29, 8.48, 5.35, 2.29, 12.35, 62.47, 113.8, 143.3],
            },
            "Şanlıurfa": {
                "ETo_aylik": [35.8, 45.2, 82.1, 125.4, 175.6, 215.8, 236.2, 208.4, 148.9, 95.7, 55.3, 35.1],
                "Peff_aylik": [73.15, 64.86, 63.01, 47.01, 28.74, 3.08, 2.29, 2.69, 1.30, 30.81, 39.70, 74.89],
            },
            "İzmir": {
                "ETo_aylik": [48.2, 55.1, 82.4, 108.7, 142.5, 172.8, 195.3, 178.6, 135.8, 95.4, 62.8, 42.5],
                "Peff_aylik": [104.2, 83.39, 67.06, 41.33, 22.62, 9.74, 7.41, 3.48, 14.54, 37.70, 74.96, 115.5],
            },
            "Konya": {
                "ETo_aylik": [30.2, 35.8, 65.4, 95.1, 140.2, 180.5, 210.8, 185.3, 120.7, 75.4, 45.1, 25.3],
                "Peff_aylik": [36.39, 30.36, 27.47, 30.09, 45.24, 21.88, 7.41, 7.80, 11.19, 30.09, 30.81, 40.99],
            },
            "Erzurum": {
                "ETo_aylik": [25.1, 30.8, 52.4, 85.7, 125.9, 165.2, 185.6, 168.9, 115.4, 70.8, 40.2, 22.7],
                "Peff_aylik": [20.57, 24.28, 27.84, 47.76, 60.52, 44.48, 25.83, 17.58, 20.29, 42.44, 34.72, 20.57],
            },
            "İstanbul": {
                "ETo_aylik": [32.8, 38.5, 58.2, 78.9, 108.4, 138.2, 152.7, 138.9, 98.7, 68.9, 46.3, 30.5],
                "Peff_aylik": [95.10, 62.16, 61.38, 40.90, 33.04, 29.46, 26.75, 39.18, 46.00, 74.17, 83.32, 103.54],
            },
            "Samsun": {
                "ETo_aylik": [35.3, 35.8, 43.7, 57.0, 83.1, 114.9, 135.2, 124.9, 85.2, 54.3, 41.1, 37.2],
                "Peff_aylik": [55.3, 46.0, 50.8, 55.5, 44.9, 41.9, 27.4, 32.2, 45.7, 73.2, 76.5, 71.3],
            }
        }

        self.bitkiler = {
            "Buğday": {
                "Kc_aylik": [0.30, 0.30, 1.15, 1.15, 1.15, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                "Ky": 1.15, "Zr": 1.25, "p": 0.55,
                "tuz_toleransi": "Yüksek", "ECe_esik": 6.0,
            },
            "Domates": {
                "Kc_aylik": [0.60, 0.80, 1.15, 1.05, 1.05, 0.90, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80],
                "Ky": 1.05, "Zr": 1.10, "p": 0.40,
                "tuz_toleransi": "Orta", "ECe_esik": 2.5,
            },
            "Pamuk": {
                "Kc_aylik": [0.35, 0.70, 1.15, 1.15, 1.15, 0.75, 0.40, 0.40, 0.40, 0.40, 0.40, 0.40],
                "Ky": 0.85, "Zr": 1.35, "p": 0.65,
                "tuz_toleransi": "Yüksek", "ECe_esik": 7.7,
            },
            "Patates": {
                "Kc_aylik": [0.45, 1.10, 1.10, 1.10, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75],
                "Ky": 1.1, "Zr": 0.5, "p": 0.35,
                "tuz_toleransi": "Düşük", "ECe_esik": 1.7,
            },
            "Biber": {
                "Kc_aylik": [0.60, 1.15, 1.15, 1.15, 1.15, 0.90, 0.80, 0.80, 0.80, 0.80, 0.80, 0.80],
                "Ky": 1.1, "Zr": 0.75, "p": 0.30,
                "tuz_toleransi": "Düşük", "ECe_esik": 1.5,
            }
        }

        self.toprak_verileri = {
            "Kum": {"theta_FC": 0.12, "theta_WP": 0.045},
            "Kumlu Tın": {"theta_FC": 0.23, "theta_WP": 0.11},
            "Tın": {"theta_FC": 0.25, "theta_WP": 0.12},
            "Siltli Tın": {"theta_FC": 0.29, "theta_WP": 0.15},
            "Kil": {"theta_FC": 0.36, "theta_WP": 0.22}
        }

        self.tuz_tavsiyeleri = {
            "Düşük Tuzluluk (EC < 2 dS/m)": {
                "Sulama": [
                    "Bitki su alımında problem beklenmez; düzenli sulama yeterlidir",
                    "Aşırı sulamadan kaçınılmalıdır; düşük tuzlulukta bile mineral birikimi artabilir"
                ],
                "Toprak Yönetimi": [
                    "Organik madde uygulamaları toprak yapısını iyileştirir"
                ],
                "Gübreleme": [
                    "Dengeli gübreleme önerilir; potasyum klorür (KCl) aşırı kullanılmamalıdır"
                ],
                "Bitki Seçimi": [
                    "Tüm bitkiler güvenle yetiştirilebilir; tuza hassas türlerde bile risk düşüktür"
                ]
            },
            "Orta Tuzluluk (2-4 dS/m)": {
                "Sulama": [
                    "Sulama aralıkları kısaltılabilir; toprağın kuruması tuz stresini artırır",
                    "Damlama sulama tuz birikimini azaltır"
                ],
                "Toprak Yönetimi": [
                    "Organik madde artırılmalıdır; tuz tamponlama kapasitesi yükselir",
                    "Gerekirse alçı (CaSO4) uygulanabilir"
                ],
                "Gübreleme": [
                    "Klor içeren gübrelerden kaçınılmalıdır"
                ],
                "Bitki Seçimi": [
                    "Orta tuzluluğa dayanıklı bitkiler önerilir"
                ]
            },
            "Yüksek Tuzluluk (4-8 dS/m)": {
                "Sulama": [
                    "Sulama sıklığı artırılmalıdır; kök bölgesinde tuz konsantrasyonu yükselmemelidir",
                    "Yıkama sulaması (leaching) gereklidir"
                ],
                "Toprak Yönetimi": [
                    "Alçı uygulaması sodik yapıyı iyileştirir",
                    "Derin sürüm önerilmez; tuzlu alt katman yüzeye çıkabilir"
                ],
                "Gübreleme": [
                    "Amonyum nitrat ve fosforlu gübreler tercih edilebilir"
                ],
                "Bitki Seçimi": [
                    "Tuz toleransı yüksek bitkiler ekilmelidir (arpa, pamuk, çavdar vb.)"
                ]
            }
        }

    def bolge_secimi(self):
        print("\nBölgeler:")
        for i, bolge in enumerate(self.bolgeler, 1):
            print(f"{i}. {bolge}")
        secim = int(input("Bölge seçin: ")) - 1
        return list(self.bolgeler.keys())[secim]

    def bitki_secimi(self):
        print("\nBitkiler:")
        for i, bitki in enumerate(self.bitkiler, 1):
            print(f"{i}. {bitki}")
        secim = int(input("Bitki seçin: ")) - 1
        return list(self.bitkiler.keys())[secim]

    def toprak_secimi(self):
        print("\nToprak Tipleri:")
        for i, toprak in enumerate(self.toprak_verileri, 1):
            print(f"{i}. {toprak}")
        secim = int(input("Toprak tipi seçin: ")) - 1
        return list(self.toprak_verileri.keys())[secim]

    def hesapla_TAW(self, toprak, Zr):
        t = self.toprak_verileri[toprak]
        return 1000 * (t["theta_FC"] - t["theta_WP"]) * Zr

    def hesapla_RAW(self, TAW, p):
        return TAW * p

    def hesapla_ETc(self, ETo, Kc):
        return ETo * Kc

    def hesapla_Ks(self, Dr, RAW, TAW):
        if Dr <= RAW:
            return 1.0

        denom = (TAW - RAW)
        if denom <= 0:
            return 0.1

        Ks = (TAW - Dr) / denom
        return max(0.1, min(1.0, Ks))

    def hesapla_ETa(self, ETc, Ks):
        return ETc * Ks

    def verim_hesapla(self, ETa, ETc, Ky):
        if ETc <= 0:
            return 0.0, 100.0

        Gercek_Maksimum_Verim_Orani = 1.0 - Ky * (1.0 - (ETa / ETc))
        Gercek_Maksimum_Verim_Orani = max(0.0, min(1.0, Gercek_Maksimum_Verim_Orani))
        Nispi_Verim_Yuzdesi = Gercek_Maksimum_Verim_Orani * 100.0
        Verim_Kaybi_Yuzdesi = 100.0 - Nispi_Verim_Yuzdesi
        return Nispi_Verim_Yuzdesi, Verim_Kaybi_Yuzdesi

    def aylik_su_dengesi_hesapla(self, bolge, bitki, toprak):
        bolge_veri = self.bolgeler[bolge]
        bitki_veri = self.bitkiler[bitki]

        ETo_aylik = bolge_veri["ETo_aylik"]
        Peff_aylik = bolge_veri["Peff_aylik"]
        Kc_aylik = bitki_veri["Kc_aylik"]

        TAW = self.hesapla_TAW(toprak, bitki_veri["Zr"])
        RAW = self.hesapla_RAW(TAW, bitki_veri["p"])

        Dr_baslangic = 0.0
        ay_sonuclari = []

        for ay in range(12):
            ETc = self.hesapla_ETc(ETo_aylik[ay], Kc_aylik[ay])
            Peff = Peff_aylik[ay]

            IWR = max(0, ETc - Peff)

            Ks = self.hesapla_Ks(Dr_baslangic, RAW, TAW)
            ETa = self.hesapla_ETa(ETc, Ks)

            Dr_ara = Dr_baslangic - Peff + ETa

            DP = 0.0
            if Dr_ara < 0:
                DP = abs(Dr_ara)
                Dr_son = 0.0
            elif Dr_ara > TAW:
                Dr_son = TAW
            else:
                Dr_son = Dr_ara

            ay_sonuclari.append({
                'ay': ay + 1,
                'ETc': ETc,
                'ETa': ETa,
                'Ks': Ks,
                'Dr': Dr_son,
                'Peff': Peff,
                'DP': DP,
                'ETo': ETo_aylik[ay],
                'Kc': Kc_aylik[ay],
                'IWR': IWR
            })

            Dr_baslangic = Dr_son

        return ay_sonuclari, TAW, RAW

    def tuz_tavsiyeleri_goster(self, bitki):
        bitki_veri = self.bitkiler[bitki]
        tuz_toleransi = bitki_veri["tuz_toleransi"]
        ECe_esik = bitki_veri["ECe_esik"]

        print(f"\nTUZLULUK YÖNETİMİ TAVSİYELERİ")
        print(f"Seçilen Bitki: {bitki}")
        print(f"Bitki Tuz Toleransı: {tuz_toleransi} (ECe Eşik Değeri: {ECe_esik} dS/m)")
        print("=" * 50)

        if tuz_toleransi == "Yüksek":
            gosterilecek_siniflar = ["Düşük Tuzluluk (EC < 2 dS/m)", "Orta Tuzluluk (2-4 dS/m)",
                                     "Yüksek Tuzluluk (4-8 dS/m)"]
        elif tuz_toleransi == "Orta":
            gosterilecek_siniflar = ["Düşük Tuzluluk (EC < 2 dS/m)", "Orta Tuzluluk (2-4 dS/m)"]
        else:
            gosterilecek_siniflar = ["Düşük Tuzluluk (EC < 2 dS/m)"]

        for sinif in gosterilecek_siniflar:
            if sinif in self.tuz_tavsiyeleri:
                print(f"\n{sinif}:")
                for kategori, maddeler in self.tuz_tavsiyeleri[sinif].items():
                    print(f"   {kategori}:")
                    for madde in maddeler:
                        print(f"      * {madde}")

    def calistir(self):
        print("\nAKILLI TARIM SİMÜLASYONU (Peff kullanılarak)")
        print("=" * 50)

        bolge = self.bolge_secimi()
        bitki = self.bitki_secimi()
        toprak = self.toprak_secimi()

        print(f"\nSEÇİLEN PARAMETRELER:")
        print(f"   Bölge: {bolge}")
        print(f"   Bitki: {bitki}")
        print(f"   Toprak: {toprak}")

        print(f"\nHESAPLAMALAR YAPILIYOR...")
        su_dengesi, TAW, RAW = self.aylik_su_dengesi_hesapla(bolge, bitki, toprak)

        ETc_total = sum([a['ETc'] for a in su_dengesi])
        ETa_total = sum([a['ETa'] for a in su_dengesi])
        IWR_total = sum([a['IWR'] for a in su_dengesi])
        Dr_final = su_dengesi[-1]['Dr']

        nispi_verim, verim_kaybi = self.verim_hesapla(ETa_total, ETc_total, self.bitkiler[bitki]["Ky"])

        print(f"\n===== YILLIK SONUÇLAR =====")
        print(f"Bölge: {bolge}")
        print(f"Bitki: {bitki}")
        print(f"Toprak: {toprak}")
        print(f"TAW: {TAW:.1f} mm")
        print(f"RAW: {RAW:.1f} mm")
        print(f"ETc (Toplam): {ETc_total:.1f} mm/yıl")
        print(f"ETa (Toplam): {ETa_total:.1f} mm/yıl")
        print(f"IWR (Net Sulama): {IWR_total:.1f} mm/yıl")
        print(f"Dr (Son): {Dr_final:.1f} mm")
        print(f"Verim (%): {nispi_verim:.1f}%")
        print(f"Verim Kaybı (%): {verim_kaybi:.1f}%")

        print(f"\n===== AYLIK DETAYLAR =====")
        for ay in su_dengesi:
            print(f"AY {ay['ay']}:")
            print(f"  ETo (Referans): {ay['ETo']:5.1f} mm")
            print(f"  Kc (Bitki Kats.): {ay['Kc']:4.2f}")
            print(f"  ETc (Bitki İht.): {ay['ETc']:5.1f} mm")
            print(f"  ETa (Gerçek Tük.): {ay['ETa']:5.1f} mm")
            print(f"   Ks (Stres): {ay['Ks']:4.2f}")
            print(f"   Etkin Yağış (Peff): {ay['Peff']:6.1f} mm")
            print(f"   IWR (Net Sulama): {ay['IWR']:6.1f} mm")
            print(f"   Dr (Su Açığı): {ay['Dr']:5.1f} mm")
            if ay['DP'] > 0:
                print(f"   Derin Sızma (DP): {ay['DP']:5.1f} mm")
            print("   " + "-" * 30)

        self.tuz_tavsiyeleri_goster(bitki)

        print(f"\nGENEL TAVSİYELER:")
        if verim_kaybi > 20:
            print(f"   YÜKSEK VERİM KAYBI: Sulama programını gözden geçirin")
        if Dr_final > RAW:
            print(f"   SU STRESİ: Bitki su açığı yaşıyor, sulama gerekli")
        if nispi_verim > 90:
            print(f"   OPTİMUM SU YÖNETİMİ: Verim kaybı minimal")

        print(f"\nSIMÜLASYON TAMAMLANDI")


if __name__ == "__main__":
    sistem = AkilliTarimSistemi()
    sistem.calistir()