import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import webbrowser

LINKEDIN_URL = "https://www.linkedin.com/in/pablo-bernar"

# Paleta de cores moderna e vibrante
PRIMARY = "#FF6B35"  # Coral vibrante
PRIMARY_HOVER = "#FF8555"
PRIMARY_DARK = "#E54D1F"
SECONDARY = "#4ECDC4"  # Turquesa
ACCENT = "#FFE66D"  # Amarelo suave
BACKGROUND = "#1A1A2E"  # Azul escuro elegante
SURFACE = "#16213E"  # Azul médio escuro
CARD = "#0F3460"  # Azul profundo
WHITE = "#F7F7F7"
TEXT = "#E8E8E8"
TEXT_SECONDARY = "#A8A8A8"
SUCCESS = "#06D6A0"
ERROR = "#EF476F"
BORDER = "#2D4263"

class ModernButton(tk.Canvas):
    """Botão customizado com efeitos hover e animações"""
    def __init__(self, parent, text, command=None, bg=PRIMARY, fg=WHITE, 
                 hover_bg=PRIMARY_HOVER, width=300, height=50, state='normal', **kwargs):
        super().__init__(parent, width=width, height=height, 
                        bg=CARD, highlightthickness=0, **kwargs)
        
        self.command = command
        self.bg = bg
        self.fg = fg
        self.hover_bg = hover_bg
        self.text = text
        self.state = state
        self.is_hover = False
        
        # Criar o retângulo do botão com bordas arredondadas
        self.rect = self.create_rounded_rect(5, 5, width-5, height-5, 
                                             radius=12, fill=bg, outline="")
        
        # Texto do botão
        self.text_id = self.create_text(width//2, height//2, 
                                       text=text, fill=fg, 
                                       font=("Poppins", 12, "bold"))
        
        # Binds para hover e click
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        
    def create_rounded_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1]
        return self.create_polygon(points, smooth=True, **kwargs)
        
    def on_enter(self, e):
        if self.state == 'normal':
            self.is_hover = True
            self.itemconfig(self.rect, fill=self.hover_bg)
            self.config(cursor="hand2")
            
    def on_leave(self, e):
        self.is_hover = False
        color = self.bg if self.state == 'normal' else TEXT_SECONDARY
        self.itemconfig(self.rect, fill=color)
        self.config(cursor="")
        
    def on_click(self, e):
        if self.state == 'normal' and self.command:
            # Animação de click
            self.itemconfig(self.rect, fill=PRIMARY_DARK)
            self.after(100, lambda: self.itemconfig(self.rect, 
                      fill=self.hover_bg if self.is_hover else self.bg))
            self.command()
            
    def set_state(self, state):
        self.state = state
        if state == 'disabled':
            self.itemconfig(self.rect, fill=TEXT_SECONDARY)
            self.itemconfig(self.text_id, fill="#666666")
            self.config(cursor="")
        else:
            self.itemconfig(self.rect, fill=self.bg)
            self.itemconfig(self.text_id, fill=self.fg)


class FileViewer(tk.Frame):
    """Componente para visualizar informações dos arquivos"""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg=SURFACE, **kwargs)
        self.setup_ui()
        
    def setup_ui(self):
        # Container interno com padding
        inner = tk.Frame(self, bg=SURFACE)
        inner.pack(padx=18, pady=18, fill='both', expand=True)
        
        # Ícone e título
        header = tk.Frame(inner, bg=SURFACE)
        header.pack(fill='x', pady=(0, 12))
        
        # Ícone de pasta (usando caracteres Unicode)
        icon_label = tk.Label(header, text="📁", font=("Segoe UI Emoji", 24), 
                             bg=SURFACE, fg=ACCENT)
        icon_label.pack(side='left', padx=(0, 12))
        
        # Título
        title_frame = tk.Frame(header, bg=SURFACE)
        title_frame.pack(side='left', fill='x', expand=True)
        
        self.title_label = tk.Label(title_frame, text="Nenhuma pasta selecionada",
                                    font=("Poppins", 11, "bold"), bg=SURFACE, 
                                    fg=WHITE, anchor='w')
        self.title_label.pack(fill='x')
        
        self.subtitle_label = tk.Label(title_frame, 
                                      text="Selecione uma pasta para começar",
                                      font=("Poppins", 9), bg=SURFACE, 
                                      fg=TEXT_SECONDARY, anchor='w')
        self.subtitle_label.pack(fill='x')
        
        # Linha separadora
        separator = tk.Frame(inner, height=1, bg=BORDER)
        separator.pack(fill='x', pady=(0, 12))
        
        # Stats container
        self.stats_frame = tk.Frame(inner, bg=SURFACE)
        self.stats_frame.pack(fill='x')
        
        # Criar cards de estatísticas
        self.files_stat = self.create_stat_card(self.stats_frame, "Arquivos", "0", PRIMARY)
        self.files_stat.pack(side='left', fill='x', expand=True, padx=(0, 8))
        
        self.folders_stat = self.create_stat_card(self.stats_frame, "Pastas", "0", SECONDARY)
        self.folders_stat.pack(side='left', fill='x', expand=True)
        
    def create_stat_card(self, parent, label, value, color):
        card = tk.Frame(parent, bg=CARD, relief=tk.FLAT)
        card_inner = tk.Frame(card, bg=CARD)
        card_inner.pack(padx=12, pady=12, fill='both', expand=True)
        
        # Valor grande
        value_label = tk.Label(card_inner, text=value, font=("Poppins", 20, "bold"),
                              bg=CARD, fg=color)
        value_label.pack()
        card.value_label = value_label  # Guardar referência
        
        # Label menor
        text_label = tk.Label(card_inner, text=label, font=("Poppins", 9),
                             bg=CARD, fg=TEXT_SECONDARY)
        text_label.pack()
        
        return card
        
    def update_info(self, pasta_nome, arquivos, pastas):
        self.title_label.config(text=pasta_nome, fg=ACCENT)
        self.subtitle_label.config(text="Pronto para exportar")
        self.files_stat.value_label.config(text=str(arquivos))
        self.folders_stat.value_label.config(text=str(pastas))


class FolderScribeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FolderScribe")
        self.geometry("480x580")
        self.configure(bg=BACKGROUND)
        self.resizable(False, False)
        
        # Tentar definir o ícone (se disponível)
        try:
            self.iconbitmap('icon.ico')
        except:
            pass
        
        self.pasta = None
        self.arquivos = 0
        self.pastas = 0
        self.conteudo = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Container principal
        main_container = tk.Frame(self, bg=BACKGROUND)
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header com logo e título
        header = tk.Frame(main_container, bg=BACKGROUND)
        header.pack(fill='x', pady=(0, 15))
        
        # Logo/Ícone
        logo_frame = tk.Frame(header, bg=PRIMARY, width=45, height=45)
        logo_frame.pack(side='left', padx=(0, 12))
        logo_frame.pack_propagate(False)
        
        logo_label = tk.Label(logo_frame, text="FS", font=("Poppins", 16, "bold"),
                             bg=PRIMARY, fg=WHITE)
        logo_label.place(relx=0.5, rely=0.5, anchor='center')
        
        # Título e subtítulo
        title_frame = tk.Frame(header, bg=BACKGROUND)
        title_frame.pack(side='left', fill='x', expand=True)
        
        title = tk.Label(title_frame, text="FolderScribe", 
                        font=("Poppins", 22, "bold"), bg=BACKGROUND, fg=WHITE)
        title.pack(anchor='w')
        
        subtitle = tk.Label(title_frame, text="Mapeie sua estrutura de arquivos",
                           font=("Poppins", 9), bg=BACKGROUND, fg=TEXT_SECONDARY)
        subtitle.pack(anchor='w')
        
        # Card principal
        card = tk.Frame(main_container, bg=SURFACE, relief=tk.FLAT)
        card.pack(fill='both', expand=True, pady=(0, 15))
        
        # Botão de seleção
        btn_frame = tk.Frame(card, bg=SURFACE)
        btn_frame.pack(pady=18, padx=18, fill='x')
        
        self.btn_selecionar = ModernButton(btn_frame, "📂  Selecionar Pasta", 
                                          command=self.selecionar_pasta,
                                          bg=PRIMARY, hover_bg=PRIMARY_HOVER,
                                          width=380, height=48)
        self.btn_selecionar.pack()
        
        # File Viewer
        self.file_viewer = FileViewer(card)
        self.file_viewer.pack(fill='x', padx=18, pady=(0, 15))
        
        # Status label
        self.status_label = tk.Label(card, text="", font=("Poppins", 9),
                                    bg=SURFACE, fg=TEXT_SECONDARY)
        self.status_label.pack(pady=(0, 12))
        
        # Botão de exportar
        btn_transcribe_frame = tk.Frame(card, bg=SURFACE)
        btn_transcribe_frame.pack(pady=(0, 18), padx=18, fill='x')
        
        self.btn_gerar = ModernButton(btn_transcribe_frame, "✨  Exportar", 
                                     command=self.gerar_arquivo,
                                     bg=SECONDARY, hover_bg="#5FE0D7",
                                     width=380, height=48, state='disabled')
        self.btn_gerar.pack()
        
        # Footer com GitHub
        footer = tk.Frame(main_container, bg=BACKGROUND)
        footer.pack(fill='x', pady=(8, 0))
        
        # Linha decorativa
        line = tk.Frame(footer, height=1, bg=BORDER)
        line.pack(fill='x', pady=(0, 10))
        
        footer_content = tk.Frame(footer, bg=BACKGROUND)
        footer_content.pack()
        
        made_label = tk.Label(footer_content, text="Criado por", 
                             font=("Poppins", 9), bg=BACKGROUND, fg=TEXT_SECONDARY)
        made_label.pack(side='left', padx=(0, 5))
        
        self.github_link = tk.Label(footer_content, text="PabloBernar", 
                                   font=("Poppins", 9, "bold underline"),
                                   bg=BACKGROUND, fg=ACCENT, cursor="hand2")
        self.github_link.pack(side='left')
        self.github_link.bind("<Button-1>", lambda e: webbrowser.open_new(LINKEDIN_URL))
        self.github_link.bind("<Enter>", lambda e: self.github_link.config(fg=PRIMARY))
        self.github_link.bind("<Leave>", lambda e: self.github_link.config(fg=ACCENT))
        
    def selecionar_pasta(self):
        pasta = filedialog.askdirectory(title="Selecione a pasta para listar")
        if pasta:
            self.pasta = pasta
            self.contar_conteudo()
            
            pasta_nome = os.path.basename(pasta) or pasta
            self.file_viewer.update_info(pasta_nome, self.arquivos, self.pastas)
            
            self.btn_gerar.set_state('normal')
            self.status_label.config(text="✓ Pronto para exportar", fg=SUCCESS)
        else:
            self.status_label.config(text="✗ Operação cancelada", fg=ERROR)
            
    def contar_conteudo(self):
        self.arquivos = 0
        self.pastas = 0
        self.conteudo = []
        
        for raiz, dirs, arquivos in os.walk(self.pasta):
            for nome in dirs:
                self.pastas += 1
                self.conteudo.append(f"PASTA: {nome}")
            for nome in arquivos:
                self.arquivos += 1
                self.conteudo.append(nome)
                
    def gerar_arquivo(self):
        caminho_salvar = filedialog.asksaveasfilename(
            title="Salvar estrutura de arquivos",
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        
        if not caminho_salvar:
            self.status_label.config(text="✗ Operação cancelada", fg=ERROR)
            return
            
        self.status_label.config(text="⏳ Exportando estrutura...", fg=ACCENT)
        self.btn_gerar.set_state('disabled')
        self.update_idletasks()
        
        threading.Thread(target=self._salvar_arquivo, args=(caminho_salvar,), 
                        daemon=True).start()
        
    def _salvar_arquivo(self, caminho_salvar):
        total = len(self.conteudo)
        
        try:
            with open(caminho_salvar, 'w', encoding='utf-8') as f:
                for i, item in enumerate(self.conteudo, 1):
                    f.write(item + '\n')
                    self.update_idletasks()
                        
            self.status_label.config(text=f"✓ Arquivo salvo com sucesso!", fg=SUCCESS)
            
            # Reativar botão após 2 segundos
            self.after(2000, lambda: self.btn_gerar.set_state('normal'))
            
        except Exception as e:
            self.status_label.config(text=f"✗ Erro: {str(e)}", fg=ERROR)
            self.btn_gerar.set_state('normal')


if __name__ == "__main__":
    app = FolderScribeApp()
    app.mainloop()