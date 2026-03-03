"""
Hatalı İşler Excel Okuma Testi
ExcelReader ile Hatalı İşler dosyasını test et
"""

from src.core.excel_reader import ExcelReader

def test_hatali_isler():
    """Hatalı İşler Excel'ini test et"""
    print("\n" + "="*60)
    print("HATALI ISLER EXCEL TESTI")
    print("="*60)
    
    reader = ExcelReader()
    file_path = "data/excel/SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(ARALIK_2024).xlsx"
    
    print(f"\nDosya: {file_path}")
    
    # Excel bilgilerini al
    info = reader.get_excel_info(file_path)
    print(f"\nExcel Bilgileri:")
    print(f"  - Dosya adi: {info.get('dosya_adi')}")
    print(f"  - Sheet sayisi: {info.get('sheet_sayisi')}")
    print(f"  - Sheet isimleri: {info.get('sheet_isimleri')}")
    print(f"  - Boyut: {info.get('boyut_mb', 0):.2f} MB")
    
    # Tum sheet'leri oku
    df = reader.read_hatali_isler(file_path)
    
    print(f"\n[BASARILI] Toplam {len(df)} satir okundu")
    print(f"Kolonlar: {list(df.columns)}")
    
    # Benzersiz ekipleri al
    ekipler = reader.get_unique_ekipler(df)
    print(f"\nBenzersiz ekip sayisi: {len(ekipler)}")
    print(f"Ekipler: {ekipler[:5]}...")  # Ilk 5 ekip
    
    # Ilk 3 satiri goster
    print("\nIlk 3 satir:")
    print(df.head(3).to_string())
    
    # Veri tipi kontrolu
    print(f"\nVeri Tipleri:")
    print(df.dtypes)
    
    print("\n" + "="*60)
    print("TEST TAMAMLANDI - BASARILI")
    print("="*60 + "\n")
    
    return df

if __name__ == "__main__":
    df = test_hatali_isler()