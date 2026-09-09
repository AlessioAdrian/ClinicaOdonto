// URL do Webhook do Make que fornecerá os dados do Dashboard (Método GET)
const MAKE_WEBHOOK_URL = 'COLE_AQUI_A_URL_DO_SEU_WEBHOOK_DO_MAKE';

async function carregarMétricas() {
    try {
        // Na prática, habilitaremos essa chamada quando o webhook estiver no ar
        /*
        const resposta = await fetch(MAKE_WEBHOOK_URL);
        const dados = await resposta.json();
        */
        
        // Dados simulados para visualização do MVP enquanto o Make é configurado
        const dadosSimulados = {
            contatados: 145,
            agendados: 32,
            pendencias: 5
        };

        document.getElementById('metric-contatados').innerText = dadosSimulados.contatados;
        document.getElementById('metric-agendados').innerText = dadosSimulados.agendados;
        document.getElementById('metric-pendencias').innerText = dadosSimulados.pendencias;

    } catch (erro) {
        console.error("Erro ao buscar dados do Make:", erro);
        document.getElementById('metric-contatados').innerText = "Erro";
    }
}

// Inicializa a PWA registrando o Service Worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js')
            .then(reg => console.log('Service Worker Registrado!', reg))
            .catch(err => console.error('Erro no Service Worker', err));
    });
}

// Carrega os dados ao abrir a tela
carregarMétricas();
