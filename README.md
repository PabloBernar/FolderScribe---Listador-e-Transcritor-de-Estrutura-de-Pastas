# 📁 FolderScribe - Listador e Transcritor de Estrutura de Pastas

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Uma ferramenta moderna e intuitiva para listar e transcrever toda a estrutura de arquivos e pastas em um único arquivo de texto.**

[Características](#-características) • [Instalação](#-instalação) • [Como Usar](#-como-usar) • [Screenshots](#-screenshots) • [Contribuir](#-contribuir)

</div>

---

## 🎯 Sobre o Projeto

**FolderScribe** é uma aplicação desktop leve e elegante que permite visualizar e exportar toda a estrutura de arquivos e pastas de um diretório. Ideal para:

- 📊 **Documentação de projetos** - Gere uma lista completa da estrutura do seu projeto
- 🗂️ **Organização pessoal** - Visualize rapidamente o conteúdo de suas pastas
- 💼 **Backup de estruturas** - Mantenha um registro textual da organização de seus arquivos
- 🔍 **Análise de diretórios** - Identifique rapidamente quantidade de arquivos e subpastas
- 📝 **Relatórios** - Crie documentação da estrutura de diretórios para relatórios

---

## ✨ Características

- 🎨 **Interface Moderna** - Design dark mode elegante e minimalista
- ⚡ **Rápido e Eficiente** - Processamento em threads para não travar a interface
- 📊 **Visualização em Tempo Real** - Veja a quantidade de arquivos e pastas instantaneamente
- 💾 **Exportação Simples** - Salve toda a estrutura em arquivo .txt
- 🖱️ **UX Intuitiva** - Interface amigável com feedback visual em todas as ações
- 🌐 **Multiplataforma** - Funciona em Windows, Linux e macOS
- 🎯 **Zero Dependências Externas** - Usa apenas bibliotecas padrão do Python

---

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Tkinter (geralmente já incluído no Python)

### Verificar instalação do Tkinter

```bash
python -m tkinter
```

Se uma janela aparecer, o Tkinter está instalado corretamente!

---

## 🚀 Instalação

### Método 1: Clone o repositório

```bash
git clone https://github.com/PabloBernar/folderscribe.git
cd folderscribe
python Listar_pastas.py
```

### Método 2: Download direto

1. Baixe o arquivo `Listar_pastas.py`
2. Execute:
   ```bash
   python Listar_pastas.py
   ```

### Criar executável (opcional)

Para criar um arquivo .exe (Windows) usando PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="FolderScribe" Listar_pastas.py
```

O executável estará na pasta `dist/`

---

## 💡 Como Usar

### Passo 1: Iniciar a aplicação

Execute o arquivo Python:

```bash
python Listar_pastas.py
```

### Passo 2: Selecionar pasta

1. Clique no botão **"📂 Selecionar Pasta"**
2. Navegue até o diretório que deseja listar
3. Confirme a seleção

### Passo 3: Visualizar informações

A aplicação mostrará:
- Nome da pasta selecionada
- Quantidade total de arquivos
- Quantidade total de subpastas

### Passo 4: Transcrever

1. Clique no botão **"✨ Transcrever"**
2. Escolha onde salvar o arquivo .txt
3. Aguarde a confirmação de sucesso!

---

## 📸 Screenshots

### Interface Principal
```
┌─────────────────────────────────────┐
│  Tq                      │
│      Organize e transcreva seus     │
│      arquivos                       │
├─────────────────────────────────────┤
│  📂  Selecionar Pasta               │
│                                     │
│  📁  Meus Documentos                │
│      Pronto para transcrever        │
│  ┌─────────────┬─────────────┐     │
│  │     142     │      18     │     │
│  │  Arquivos   │   Pastas    │     │
│  └─────────────┴─────────────┘     │
│                                     │
│  ✓ Pronto para transcrever          │
│                                     │
│  ✨  Transcrever                    │
│                                     │
│  ─────────────────────────────      │
│  Criado por PabloBernar             │
└─────────────────────────────────────┘
```

---

## 📄 Formato do Arquivo Gerado

O arquivo .txt gerado terá o seguinte formato:

```
PASTA: Documentos
arquivo1.txt
arquivo2.pdf
PASTA: Imagens
foto1.jpg
foto2.png
PASTA: Videos
video1.mp4
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem de programação
- **Tkinter** - Interface gráfica
- **Threading** - Processamento assíncrono
- **OS & Webbrowser** - Módulos built-in do Python

---

## 🎨 Personalização

### Alterar cores

Edite as variáveis de cor no início do arquivo:

```python
PRIMARY = "#FF6B35"      # Cor principal (coral)
SECONDARY = "#4ECDC4"    # Cor secundária (turquesa)
ACCENT = "#FFE66D"       # Cor de destaque (amarelo)
BACKGROUND = "#1A1A2E"   # Fundo (azul escuro)
```

### Alterar fontes

Modifique as declarações de fonte:

```python
font=("Poppins", 12, "bold")  # (Família, Tamanho, Estilo)
```

---

## 🔧 Solução de Problemas

### Tkinter não instalado

**Linux:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

### Erro de codificação

Se encontrar problemas com caracteres especiais, certifique-se de que o arquivo é salvo com UTF-8.

### Fontes não encontradas

A aplicação usa "Poppins", mas fallback para fontes do sistema se não disponível.

---

## 📦 Casos de Uso

### 1. Documentar estrutura de projeto
```
Ideal para incluir em README.md ou documentação técnica
```

### 2. Inventário de arquivos
```
Crie listas de arquivos para controle, backup ou auditoria
```

### 3. Análise de diretórios grandes
```
Visualize rapidamente o conteúdo sem abrir dezenas de pastas
```

### 4. Comparação de estruturas
```
Compare duas estruturas de pastas gerando dois arquivos
```

---

## 🤝 Contribuir

Contribuições são bem-vindas! Siga os passos:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

### Ideias para contribuir:

- [ ] Adicionar filtros por extensão de arquivo
- [ ] Exportar para formatos JSON, CSV ou XML
- [ ] Adicionar opção de incluir tamanhos de arquivo
- [ ] Criar modo de comparação de duas pastas
- [ ] Adicionar busca dentro dos resultados
- [ ] Suporte para ignorar pastas específicas (.git, node_modules, etc)

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Pablo Bernar**

- LinkedIn: [Pablo Bernar](https://www.linkedin.com/in/pablo-bernar)
- GitHub: [@PabloBernar](https://github.com/PabloBernar)

---

## ⭐ Mostre seu apoio

Se este projeto foi útil para você, considere dar uma ⭐️!

---

## 📊 Keywords para SEO

`file lister` `folder structure` `directory tree` `file organizer` `python tkinter` `folder scanner` `file system tool` `directory viewer` `file inventory` `estrutura de pastas` `listar arquivos` `organizador de arquivos`

---

<div align="center">

**Desenvolvido com ❤️ por [Pablo Bernar](https://github.com/PabloBernar)**

</div>
