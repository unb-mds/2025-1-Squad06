import socket
from collections import defaultdict
import json
from datetime import datetime
import os

ARQUIVO_VOTOS = 'votos.json'

class ServidorVotacao:
    def __init__(self):
        self.votos = self.carregar_votos()
        self.host = '0.0.0.0'
        self.port = 5000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def carregar_votos(self):
        """Carrega os votos existentes ou cria um novo arquivo"""
        if os.path.exists(ARQUIVO_VOTOS):
            with open(ARQUIVO_VOTOS, 'r') as f:
                return json.load(f)
        return {
            'total': {'a_favor': 0, 'contra': 0, 'abstencao': 0},
            'historico': []
        }
    
    def salvar_votos(self):
        """Salva os votos no arquivo JSON"""
        with open(ARQUIVO_VOTOS, 'w') as f:
            json.dump(self.votos, f, indent=2, ensure_ascii=False)
    
    def processar_voto(self, voto, endereco):
        """Registra um novo voto e atualiza o JSON"""
        voto = voto.lower()
        timestamp = datetime.now().isoformat()
        
        # Mapeia as variações de votos
        if voto in ['sim', 's', 'a favor', 'afavor']:
            tipo = 'a_favor'
        elif voto in ['nao', 'n', 'não', 'contra']:
            tipo = 'contra'
        elif voto in ['abster', 'abs', 'abstencao', 'abstenção']:
            tipo = 'abstencao'
        else:
            return False  # Voto inválido
        
        # Atualiza totais
        self.votos['total'][tipo] += 1
        
        # Adiciona ao histórico
        self.votos['historico'].append({
            'tipo': tipo,
            'endereco': f"{endereco[0]}:{endereco[1]}",
            'timestamp': timestamp,
            'voto_original': voto
        })
        
        self.salvar_votos()
        return True
    
    def iniciar(self):
        """Inicia o servidor de votação"""
        self.socket.bind((self.host, self.port))
        print(f"✅ Servidor ativo em {self.host}:{self.port}")
        print("📊 Aguardando votos... (Ctrl+C para encerrar)")
        
        try:
            while True:
                data, addr = self.socket.recvfrom(1024)
                voto = data.decode().strip()
                
                if self.processar_voto(voto, addr):
                    print(f"🗳️ Voto recebido de {addr}: {voto.upper()}")
                    print(f"📊 Totais: {self.votos['total']}")
                else:
                    print(f"⚠️ Voto inválido de {addr}: {voto}")
                
        except KeyboardInterrupt:
            print("\n🛑 Encerrando servidor...")
        finally:
            self.socket.close()
            print("💾 Dados salvos em votos.json")

if __name__ == "__main__":
    servidor = ServidorVotacao()
    servidor.iniciar()