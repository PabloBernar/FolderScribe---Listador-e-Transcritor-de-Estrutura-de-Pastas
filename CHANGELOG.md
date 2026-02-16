# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2025-02-15

### ✨ Adicionado
- Interface gráfica moderna com design dark mode
- Seleção de pasta via dialog
- Visualização em tempo real de quantidade de arquivos e pastas
- Botão de transcrever com feedback visual
- Exportação da estrutura completa para arquivo .txt
- Processamento em thread separada para não travar a interface
- Componentes customizados (ModernButton, FileViewer)
- Footer com link para perfil do criador
- Suporte a emojis na interface
- Estados visuais para botões (hover, disabled, active)

### 🎨 Design
- Paleta de cores vibrante (coral, turquesa, amarelo)
- Logo "Tq" personalizado
- Cards de estatísticas com cores diferenciadas
- Animações e transições suaves
- Bordas arredondadas em todos os componentes
- Feedback visual para todas as ações

### 🔧 Técnico
- Baseado em Python 3.7+
- Interface Tkinter com componentes customizados
- Zero dependências externas
- Threading para operações assíncronas
- Codificação UTF-8 para suporte completo a caracteres especiais
- Tratamento robusto de erros

---

## [Unreleased]

### 🚀 Planejado para versão 1.1.0
- [ ] Filtros por extensão de arquivo
- [ ] Exportação para JSON e CSV
- [ ] Opção de tema claro
- [ ] Incluir tamanhos de arquivos na listagem
- [ ] Opção de incluir datas de modificação
- [ ] Barra de progresso durante processamento

### 💡 Ideias Futuras (2.0.0)
- [ ] Comparação de duas estruturas de pastas
- [ ] Busca dentro dos resultados
- [ ] Ignorar pastas específicas (.git, node_modules, etc)
- [ ] Preview do conteúdo antes de exportar
- [ ] Estatísticas avançadas (tamanho total, tipos de arquivo)
- [ ] Gráficos de distribuição de arquivos
- [ ] Modo de linha de comando (CLI)
- [ ] Interface web opcional

---

## Tipos de Mudanças

- `✨ Adicionado` - para novas funcionalidades
- `🔄 Modificado` - para mudanças em funcionalidades existentes
- `🗑️ Removido` - para funcionalidades removidas
- `🐛 Corrigido` - para correção de bugs
- `🔒 Segurança` - para correções de vulnerabilidades
- `🎨 Design` - para mudanças visuais
- `⚡ Performance` - para melhorias de desempenho
- `📝 Documentação` - para mudanças na documentação

---

## Como Contribuir

Veja as mudanças planejadas acima e sinta-se livre para:
1. Abrir uma Issue discutindo a feature
2. Fazer um Fork do projeto
3. Implementar a mudança
4. Abrir um Pull Request

Para mais detalhes, veja [CONTRIBUTING.md](CONTRIBUTING.md)
