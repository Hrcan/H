"""
Test: Bağımlılıkların Doğru Yüklendiğini Kontrol Et
Proje: Excel Veri Görüntüleme Uygulaması
Versiyon: 0.1.0
"""

import sys


def test_python_version():
    """Python versiyonunun 3.8 veya üzeri olduğunu test et"""
    assert sys.version_info >= (3, 8), "Python 3.8 veya üzeri gerekli"
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


def test_pyqt5_import():
    """PyQt5'in import edildiğini test et"""
    try:
        from PyQt5 import QtWidgets, QtCore
        print("✅ PyQt5 import edildi")
        assert True
    except ImportError as e:
        assert False, f"PyQt5 import edilemedi: {e}"


def test_pandas_import():
    """Pandas'ın import edildiğini test et"""
    try:
        import pandas as pd
        version = pd.__version__
        print(f"✅ Pandas {version} import edildi")
        assert version >= "2.0.0"
    except ImportError as e:
        assert False, f"Pandas import edilemedi: {e}"


def test_openpyxl_import():
    """Openpyxl'in import edildiğini test et"""
    try:
        import openpyxl
        version = openpyxl.__version__
        print(f"✅ Openpyxl {version} import edildi")
        assert version >= "3.0.0"
    except ImportError as e:
        assert False, f"Openpyxl import edilemedi: {e}"


def test_numpy_import():
    """Numpy'ın import edildiğini test et"""
    try:
        import numpy as np
        version = np.__version__
        print(f"✅ Numpy {version} import edildi")
        assert version >= "1.20.0"
    except ImportError as e:
        assert False, f"Numpy import edilemedi: {e}"


if __name__ == "__main__":
    print("\n" + "="*60)
    print("BAĞIMLILIK TESTLERİ")
    print("="*60 + "\n")
    
    test_python_version()
    test_pyqt5_import()
    test_pandas_import()
    test_openpyxl_import()
    test_numpy_import()
    
    print("\n" + "="*60)
    print("TÜM TESTLER BAŞARILI! ✅")
    print("="*60 + "\n")