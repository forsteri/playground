import socket
import threading
import random

BACKENDS = [
    ('localhost', 8081),
    ('localhost', 8082),
    ('localhost', 8083)
]

def parse_headers(data):
    headers = {}
    lines = data.split(b'\r\n')
    for line in lines[1:]:  # 最初の行はリクエストラインなのでスキップ
        if b':' in line:
            key, value = line.split(b':', 1)
            headers[key.strip().lower()] = value.strip()
    return headers

def modify_headers(headers, client_addr):
    # X-Forwarded-Forヘッダーを追加
    headers[b'x-forwarded-for'] = client_addr[0].encode()
    # Hostヘッダーを修正（必要に応じて）
    if b'host' in headers:
        original_host = headers[b'host']
        headers[b'x-original-host'] = original_host
        headers[b'host'] = b'backend-server'
    return headers

def handle_client(client_socket, client_addr):
    backend = random.choice(BACKENDS)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
        backend_socket.connect(backend)
        
        request = client_socket.recv(4096)
        headers = parse_headers(request)
        modified_headers = modify_headers(headers, client_addr)
        
        # ヘッダーを再構築
        request_lines = request.split(b'\r\n')
        new_request = request_lines[0] + b'\r\n'  # リクエストライン
        for key, value in modified_headers.items():
            new_request += key + b': ' + value + b'\r\n'
        new_request += b'\r\n'  # ヘッダーの終わり
        
        # ボディがあれば追加
        if b'\r\n\r\n' in request:
            new_request += request.split(b'\r\n\r\n', 1)[1]
        
        backend_socket.sendall(new_request)
        
        while True:
            response = backend_socket.recv(4096)
            if not response:
                break
            client_socket.sendall(response)
    
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    
    print("リバースプロキシが待機中...")
    
    while True:
        client_sock, address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_sock, address))
        client_handler.start()

if __name__ == "__main__":
    main()