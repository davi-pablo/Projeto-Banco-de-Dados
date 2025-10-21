#!/usr/bin/env python3
"""
Script simples para criar as tabelas no MySQL
"""

import pymysql

def criar_tabelas():
    try:
        # Conectar ao MySQL
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            database='universi_tour',
            charset='utf8mb4'
        )
        
        print("Conectado ao MySQL com sucesso!")
        
        cursor = connection.cursor()
        
        # Script SQL para criar as tabelas
        sql_script = """
        -- Tabela de Destinos
        CREATE TABLE IF NOT EXISTS destino (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT NOT NULL,
            imagem VARCHAR(200) NOT NULL,
            distancia VARCHAR(50) NOT NULL,
            preco VARCHAR(20) NOT NULL,
            preco_numerico DECIMAL(10,2) NOT NULL,
            ativo BOOLEAN DEFAULT TRUE,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        -- Tabela de Usuários
        CREATE TABLE IF NOT EXISTS usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(120) UNIQUE NOT NULL,
            telefone VARCHAR(20),
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        -- Tabela de Reservas
        CREATE TABLE IF NOT EXISTS reserva (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario_id INT NOT NULL,
            destino_id INT NOT NULL,
            data_viagem DATE NOT NULL,
            data_retorno DATE NOT NULL,
            num_pessoas INT NOT NULL,
            valor_total DECIMAL(10,2) NOT NULL,
            status VARCHAR(20) DEFAULT 'pendente',
            observacoes TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE,
            FOREIGN KEY (destino_id) REFERENCES destino(id) ON DELETE CASCADE
        );

        -- Tabela de Contatos
        CREATE TABLE IF NOT EXISTS contato (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(120) NOT NULL,
            mensagem TEXT NOT NULL,
            data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            respondido BOOLEAN DEFAULT FALSE
        );

        -- Inserir dados iniciais dos destinos
        INSERT IGNORE INTO destino (nome, descricao, imagem, distancia, preco, preco_numerico) VALUES
        ('Rio de Janeiro', 'A cidade carioca, famosa por suas praias e seus pontos turisticos.', 'Imagens/rio.jpg', '100-500', 'medio', 800.00),
        ('Salvador', 'A cidade calorosa, um lugar de tradicao e cultura.', 'Imagens/salvador.jpg', '500-1000', 'alto', 1200.00),
        ('Recife', 'A cidade maravilhosa, com praias paradisiacas e cultura vibrante.', 'Imagens/recife.jpg', '0-100', 'baixo', 500.00);

        -- Inserir usuários de exemplo
        INSERT IGNORE INTO usuario (nome, email, telefone) VALUES
        ('Joao Silva', 'joao.silva@email.com', '(11) 99999-1111'),
        ('Maria Santos', 'maria.santos@email.com', '(11) 99999-2222'),
        ('Pedro Oliveira', 'pedro.oliveira@email.com', '(11) 99999-3333'),
        ('Ana Costa', 'ana.costa@email.com', '(11) 99999-4444');

        -- Inserir reservas de exemplo
        INSERT IGNORE INTO reserva (usuario_id, destino_id, data_viagem, data_retorno, num_pessoas, valor_total, status, observacoes) VALUES
        (1, 1, '2025-02-15', '2025-02-20', 2, 1600.00, 'confirmada', 'Primeira viagem de casal'),
        (2, 2, '2025-03-10', '2025-03-15', 1, 1200.00, 'pendente', 'Viagem de aniversario'),
        (3, 3, '2025-04-05', '2025-04-08', 3, 1500.00, 'confirmada', 'Viagem em familia'),
        (4, 1, '2025-05-20', '2025-05-25', 2, 1600.00, 'pendente', 'Ferias de verao');

        -- Inserir contatos de exemplo
        INSERT IGNORE INTO contato (nome, email, mensagem) VALUES
        ('Carlos Ferreira', 'carlos.ferreira@email.com', 'Gostaria de informacoes sobre pacotes para o Rio de Janeiro.'),
        ('Lucia Mendes', 'lucia.mendes@email.com', 'Preciso de ajuda para planejar uma viagem de 15 dias pelo Brasil.'),
        ('Roberto Alves', 'roberto.alves@email.com', 'Qual o melhor periodo para viajar para Salvador?');
        """
        
        # Executar cada comando separadamente
        for statement in sql_script.split(';'):
            statement = statement.strip()
            if statement and not statement.startswith('--'):
                try:
                    cursor.execute(statement)
                except Exception as e:
                    print(f"Aviso: {e}")
        
        connection.commit()
        print("Tabelas criadas e dados inseridos com sucesso!")
        
        # Verificar tabelas criadas
        cursor.execute("SHOW TABLES")
        tabelas = cursor.fetchall()
        print("\nTabelas criadas:")
        for tabela in tabelas:
            print(f"  - {tabela[0]}")
        
        cursor.close()
        connection.close()
        
        return True
        
    except Exception as e:
        print(f"Erro: {e}")
        return False

if __name__ == '__main__':
    criar_tabelas()
