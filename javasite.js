document.addEventListener("DOMContentLoaded", () => {
    carregarDestinos();
    
    // Adiciona os event listeners para filtros
    document.getElementById("search-destination").addEventListener("input", filtrarDestinos);
    document.getElementById("distance").addEventListener("change", filtrarDestinos);
    document.getElementById("price").addEventListener("change", filtrarDestinos);
});

function carregarDestinos() {
    console.log("Carregando destinos...");
    
    // Mostrar loading
    const lista = document.getElementById("destinos-list");
    if (lista) {
        lista.innerHTML = '<div style="text-align: center; padding: 20px;">Carregando destinos...</div>';
    }
    
    fetch("http://127.0.0.1:5000/api/destinos")
        .then(res => {
            console.log("Resposta recebida:", res.status);
            if (!res.ok) {
                throw new Error(`HTTP ${res.status}: ${res.statusText}`);
            }
            return res.json();
        })
        .then(destinos => {
            console.log("Destinos carregados:", destinos);
            const lista = document.getElementById("destinos-list");
            if (!lista) {
                console.error("Elemento 'destinos-list' nao encontrado!");
                return;
            }
            lista.innerHTML = "";

            if (destinos.length === 0) {
                console.warn("Nenhum destino encontrado!");
                lista.innerHTML = "<p>Nenhum destino encontrado.</p>";
                return;
            }

            destinos.forEach(destino => {
                const div = document.createElement("div");
                div.classList.add("destino");
                div.setAttribute("data-distancia", destino.distancia);
                div.setAttribute("data-preco", destino.preco);
                div.setAttribute("data-id", destino.id);

                div.innerHTML = `
                    <img src="${destino.imagem}" alt="${destino.nome}">
                    <h3><a href="#" onclick="mostrarDetalhesDestino(${destino.id})">${destino.nome}</a></h3>
                    <p>${destino.descricao}</p>
                    <div class="preco-info">
                        <span class="preco">R$ ${parseFloat(destino.preco_numerico).toFixed(2)}</span>
                        <button class="btn-reservar" onclick="abrirModalReserva(${destino.id}, '${destino.nome}', ${parseFloat(destino.preco_numerico)})">Reservar</button>
                    </div>
                `;
                lista.appendChild(div);
            });
        })
        .catch(err => {
            console.error("Erro ao carregar destinos:", err);
            const lista = document.getElementById("destinos-list");
            if (lista) {
                lista.innerHTML = `
                    <div style="text-align: center; padding: 20px; color: #e74c3c;">
                        <h3>Erro ao carregar destinos</h3>
                        <p>Erro: ${err.message}</p>
                        <p>Verifique se o backend está rodando em http://127.0.0.1:5000</p>
                        <button onclick="carregarDestinos()" style="padding: 10px 20px; background: #3498db; color: white; border: none; border-radius: 5px; cursor: pointer;">
                            Tentar Novamente
                        </button>
                    </div>
                `;
            }
        });
}

function filtrarDestinos() {
    const searchQuery = document.getElementById("search-destination").value.toLowerCase();
    const distanceFilter = document.getElementById("distance").value;
    const priceFilter = document.getElementById("price").value;

    const destinos = document.querySelectorAll(".destino");

    destinos.forEach(destino => {
        const nome = destino.querySelector("h3").textContent.toLowerCase();
        const distancia = destino.getAttribute("data-distancia");
        const preco = destino.getAttribute("data-preco");

        const matchesSearch = nome.includes(searchQuery);
        const matchesDistance = distanceFilter ? distancia === distanceFilter : true;
        const matchesPrice = priceFilter ? preco === priceFilter : true;

        if (matchesSearch && matchesDistance && matchesPrice) {
            destino.style.display = "block";
        } else {
            destino.style.display = "none";
        }
    });
}

// Função para mostrar detalhes do destino
function mostrarDetalhesDestino(destinoId) {
    fetch(`http://127.0.0.1:5000/api/destinos/${destinoId}`)
        .then(res => res.json())
        .then(destino => {
            alert(`Destino: ${destino.nome}\nDescrição: ${destino.descricao}\nPreço: R$ ${parseFloat(destino.preco_numerico).toFixed(2)}\nDistância: ${destino.distancia} km`);
        })
        .catch(err => console.error("Erro ao carregar detalhes:", err));
}

// Função para abrir modal de reserva
function abrirModalReserva(destinoId, nomeDestino, preco) {
    const modal = document.createElement('div');
    modal.className = 'modal-reserva';
    modal.innerHTML = `
        <div class="modal-content">
            <div class="modal-header">
                <h2>✈️ Reservar ${nomeDestino}</h2>
                <span class="close" onclick="fecharModal()">&times;</span>
            </div>
            
            <div class="modal-body">
                <div class="destino-info">
                    <h3>🏖️ ${nomeDestino}</h3>
                    <p>Valor por pessoa: <strong>R$ ${parseFloat(preco).toFixed(2)}</strong></p>
                </div>
                
                <form id="formReserva">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="nomeUsuario">👤 Nome Completo:</label>
                            <input type="text" id="nomeUsuario" name="nome" placeholder="Digite seu nome completo" required>
                        </div>
                        <div class="form-group">
                            <label for="emailUsuario">📧 Email:</label>
                            <input type="email" id="emailUsuario" name="email" placeholder="seu@email.com" required>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="telefoneUsuario">📱 Telefone:</label>
                            <input type="tel" id="telefoneUsuario" name="telefone" placeholder="(11) 99999-9999">
                        </div>
                        <div class="form-group">
                            <label for="numPessoas">👥 Número de Pessoas:</label>
                            <select id="numPessoas" name="num_pessoas" required>
                                <option value="">Selecione...</option>
                                <option value="1">1 pessoa</option>
                                <option value="2">2 pessoas</option>
                                <option value="3">3 pessoas</option>
                                <option value="4">4 pessoas</option>
                                <option value="5">5 pessoas</option>
                                <option value="6">6 pessoas</option>
                                <option value="7">7 pessoas</option>
                                <option value="8">8 pessoas</option>
                                <option value="9">9 pessoas</option>
                                <option value="10">10 pessoas</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label for="dataViagem">📅 Data da Viagem:</label>
                            <input type="date" id="dataViagem" name="data_viagem" required>
                        </div>
                        <div class="form-group">
                            <label for="dataRetorno">📅 Data de Retorno:</label>
                            <input type="date" id="dataRetorno" name="data_retorno" required>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="observacoes">📝 Observações Especiais:</label>
                        <textarea id="observacoes" name="observacoes" rows="3" placeholder="Ex: Crianças, necessidades especiais, preferências de quarto..."></textarea>
                    </div>
                    
                    <div class="preco-total">
                        <div class="preco-item">
                            <span>Valor por pessoa:</span>
                            <span>R$ ${parseFloat(preco).toFixed(2)}</span>
                        </div>
                        <div class="preco-item total">
                            <span>Total:</span>
                            <span id="valorTotal">R$ ${parseFloat(preco).toFixed(2)}</span>
                        </div>
                    </div>
                    
                    <div class="form-actions">
                        <button type="button" class="btn-cancelar" onclick="fecharModal()">❌ Cancelar</button>
                        <button type="submit" class="btn-confirmar">✅ Confirmar Reserva</button>
                    </div>
                </form>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    modal.classList.add('show');
    
    // Atualizar valor total quando número de pessoas mudar
    document.getElementById('numPessoas').addEventListener('change', function() {
        const numPessoas = parseInt(this.value) || 1;
        const valorTotal = parseFloat(preco) * numPessoas;
        document.getElementById('valorTotal').textContent = `R$ ${valorTotal.toFixed(2)}`;
    });
    
    // Submeter formulário
    document.getElementById('formReserva').addEventListener('submit', function(e) {
        e.preventDefault();
        fazerReserva(destinoId);
    });
    
    // Definir data mínima como hoje e validações
    const hoje = new Date().toISOString().split('T')[0];
    const dataViagemInput = document.getElementById('dataViagem');
    const dataRetornoInput = document.getElementById('dataRetorno');
    
    dataViagemInput.min = hoje;
    dataRetornoInput.min = hoje;
    
    // Validar que data de retorno seja após data de viagem
    dataViagemInput.addEventListener('change', function() {
        dataRetornoInput.min = this.value;
        if (dataRetornoInput.value && dataRetornoInput.value <= this.value) {
            dataRetornoInput.value = '';
        }
    });
}

function fecharModal() {
    const modal = document.querySelector('.modal-reserva');
    if (modal) {
        modal.remove();
    }
}

function fazerReserva(destinoId) {
    // Desabilitar botão para evitar duplo clique
    const btnConfirmar = document.querySelector('.btn-confirmar');
    btnConfirmar.disabled = true;
    btnConfirmar.textContent = '⏳ Processando...';
    
    const formData = {
        nome: document.getElementById('nomeUsuario').value,
        email: document.getElementById('emailUsuario').value,
        telefone: document.getElementById('telefoneUsuario').value,
        data_viagem: document.getElementById('dataViagem').value,
        data_retorno: document.getElementById('dataRetorno').value,
        num_pessoas: parseInt(document.getElementById('numPessoas').value),
        observacoes: document.getElementById('observacoes').value
    };
    
    console.log('Fazendo reserva...', formData);
    
    // Primeiro, criar ou buscar usuário
    fetch('http://127.0.0.1:5000/api/usuarios', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nome: formData.nome,
            email: formData.email,
            telefone: formData.telefone
        })
    })
    .then(res => {
        if (!res.ok) {
            throw new Error(`Erro ao criar usuário: ${res.status}`);
        }
        return res.json();
    })
    .then(usuario => {
        console.log('Usuário criado/encontrado:', usuario);
        
        // Agora criar a reserva
        return fetch('http://127.0.0.1:5000/api/reservas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                usuario_id: usuario.id,
                destino_id: destinoId,
                data_viagem: formData.data_viagem,
                data_retorno: formData.data_retorno,
                num_pessoas: formData.num_pessoas,
                observacoes: formData.observacoes
            })
        });
    })
    .then(res => {
        if (!res.ok) {
            throw new Error(`Erro ao criar reserva: ${res.status}`);
        }
        return res.json();
    })
    .then(reserva => {
        console.log('Reserva criada:', reserva);
        
        // Mostrar sucesso
        alert(`🎉 Reserva realizada com sucesso!\n\n📋 Detalhes:\n• ID da Reserva: ${reserva.id}\n• Destino: ${formData.nome}\n• Data: ${formData.data_viagem} a ${formData.data_retorno}\n• Pessoas: ${formData.num_pessoas}\n• Total: R$ ${(parseFloat(document.querySelector('.preco-item span:last-child').textContent.replace('R$ ', '')) * formData.num_pessoas).toFixed(2)}\n\n📧 Enviaremos os detalhes para: ${formData.email}`);
        
        fecharModal();
    })
    .catch(err => {
        console.error('Erro ao fazer reserva:', err);
        
        // Reabilitar botão
        btnConfirmar.disabled = false;
        btnConfirmar.textContent = '✅ Confirmar Reserva';
        
        alert(`❌ Erro ao realizar reserva:\n\n${err.message}\n\nTente novamente ou entre em contato conosco.`);
    });
}

// Função para enviar formulário de contato
function enviarContato(event) {
    event.preventDefault();
    
    const formData = {
        nome: document.getElementById('nome').value,
        email: document.getElementById('email').value,
        mensagem: document.getElementById('mensagem').value
    };
    
    fetch('http://127.0.0.1:5000/api/contatos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(res => res.json())
    .then(contato => {
        // Redirecionar para página de confirmação
        window.location.href = 'confirmacao.html';
    })
    .catch(err => {
        console.error('Erro ao enviar contato:', err);
        alert('Erro ao enviar mensagem. Tente novamente.');
    });
}

// Adicionar event listener ao formulário de contato
document.addEventListener("DOMContentLoaded", () => {
    const formContato = document.querySelector('form[action="confirmacao.html"]');
    if (formContato) {
        formContato.addEventListener('submit', enviarContato);
    }
});
