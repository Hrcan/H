import pandas as pd
import os
import sys

# UTF-8 encoding için
sys.stdout.reconfigure(encoding='utf-8')

def analyze_excel_file(file_path):
    """Excel dosyasindaki tum sheet'leri ve basliklari analiz eder"""
    print(f"\n{'='*80}")
    print(f"DOSYA: {os.path.basename(file_path)}")
    print(f"{'='*80}\n")
    
    try:
        # Excel dosyasini ac
        excel_file = pd.ExcelFile(file_path)
        
        print(f"Toplam Sheet Sayisi: {len(excel_file.sheet_names)}\n")
        
        # Her sheet'i analiz et
        for idx, sheet_name in enumerate(excel_file.sheet_names, 1):
            print(f"{'-'*80}")
            print(f"SHEET {idx}: {sheet_name}")
            print(f"{'-'*80}")
            
            # Ilk satiri oku (basliklar)
            df = pd.read_excel(file_path, sheet_name=sheet_name, nrows=0)
            columns = df.columns.tolist()
            
            print(f"Kolon Sayisi: {len(columns)}\n")
            
            # Kolonlari listele
            for col_idx, col_name in enumerate(columns):
                excel_col = chr(65 + col_idx) if col_idx < 26 else f"{chr(65 + col_idx//26 - 1)}{chr(65 + col_idx%26)}"
                print(f"  {excel_col}1: {col_name}")
            
            print()
    
    except Exception as e:
        print(f"HATA: {str(e)}")

# Excel dosyalarını analiz et
print("\n" + "="*80)
print("EXCEL DOSYALARI ANALİZİ")
print("="*80)

# Hatalı Biten İşler - ARALIK
analyze_excel_file("data/excel/SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(ARALIK_2024).xlsx")

# Hatalı Biten İşler - KASIM
analyze_excel_file("data/excel/SAO_Ana_Sistemler_Hatalı_Biten_İsler_Raporu_(KASIM_2024).xlsx")

# Uzun Süren İşler - ARALIK
analyze_excel_file("data/excel/SAO_Sistem_Operasyon_Uzun_Süren_İşler(ARALIK_2024).xlsx")

print("\n" + "="*80)
print("ANALİZ TAMAMLANDI")
print("="*80 + "\n")