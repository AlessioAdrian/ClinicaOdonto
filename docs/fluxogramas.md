```mermaid
graph TD
    classDef sistema fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decisao fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef acao fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;

    subgraph Canais Digitais
        A[Instagram/Facebook/Google] --> B(Interação do Usuário)
        B --> C{Ação Legítima?}:::decisao
    end

    subgraph CRM Central
        C -->|Formulário/Mensagem| D[Captura Lead no CRM]:::sistema
        C -->|Visualização/Curtida| E[Público de Remarketing]:::acao
    end

    subgraph Qualificação da IA
        D --> F[IA inicia contato via WhatsApp]:::sistema
        F --> G{Tem interesse?}:::decisao
    end

    subgraph Desfecho do Atendimento
        G -->|SIM| H[Integração: Confirma Agenda]:::acao
        G -->|NÃO| I[Registra Motivo e Nutrição]:::sistema
        G -->|SEM RESPOSTA| J[Follow-up Automático]:::sistema
        J -->|Continua sem resposta| K[Encerra Fluxo]:::acao
    end
```mermaid

```mermaid
graph TD
    classDef sistema fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decisao fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef acao fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;

    subgraph Sistema Odontológico
        A[Consulta Automática Diária]:::sistema --> B{Último atendimento > 3 anos?}:::decisao
    end

    subgraph CRM e IA
        B -->|SIM| C[Cria Lista de Reativação]:::sistema
        B -->|NÃO| D[Fim do Fluxo]
        C --> E[WhatsApp + IA Inicia Contato]:::acao
        E --> F{Qual a resposta?}:::decisao
    end

    subgraph Desfecho
        F -->|SIM| G[Agendar na Agenda]:::acao
        F -->|NÃO| H[Registrar Recusa]:::sistema
        F -->|SEM RESPOSTA| I[Régua de Follow-up]:::sistema
        G --> J[Atualiza Dashboard e Relatório]:::sistema
        H --> J
        I --> J
    end
```mermaid

```mermaid
graph TD
    classDef sistema fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef decisao fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef acao fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;

    subgraph Captura Física
        A[Paciente Escaneia QR Code] --> B[Responde Pesquisa]:::sistema
    end

    subgraph CRM Central
        B --> C[Consulta ao Banco de Dados]:::sistema
        C --> D{Está em Tratamento?}:::decisao
    end

    subgraph Motor de IA e Agenda
        D -->|SIM| E[Acompanhamento do Tratamento Atual]:::acao
        D -->|NÃO| F[IA aborda via WhatsApp]:::acao
        F --> G{Demonstra Interesse?}:::decisao
        G -->|SIM| H[Agenda Consulta e Envia Confirmação]:::acao
        G -->|NÃO ou Falha| I[Gera Tarefa para Recepção]:::sistema
    end
```mermaid

