"""
Cyber Blue Theme - Mavi Siber Tema
Modern mavi tonları ile teknolojik görünüm
"""

from .base_theme import BaseTheme


class CyberBlueTheme(BaseTheme):
    """Cyber Blue tema - Mavi ve cyan tonları"""
    
    def __init__(self):
        super().__init__()
        self.name = "Cyber Blue"
    
    def _define_colors(self):
        """Cyber Blue renk paleti"""
        return {
            # Ana renkler - Mavi gradient
            'primary_start': '#00d4ff',
            'primary_end': '#0099ff',
            'accent': '#00ffff',
            
            # Background - Koyu mavi tonları
            'bg_dark': '#001a2e',
            'bg_medium': '#002540',
            'bg_light': '#003152',
            
            # Text
            'text_primary': '#e0f7ff',
            'text_secondary': '#b0d9e8',
            'text_disabled': '#6090a8',
            
            # States
            'success': '#00ff88',
            'warning': '#ffaa00',
            'error': '#ff4466',
            'info': '#00d4ff',
            
            # Border & Shadow
            'border': '#0099ff',
            'shadow': 'rgba(0, 212, 255, 0.3)',
        }