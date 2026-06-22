import tkinter as tk
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha Flashcard Quiz App")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e2e")

        self.flashcards = [
            {"question": "What does API stand for?", "answer": "Application Programming Interface"},
            {"question": "What is a primary key in SQL?", "answer": "A unique identifier for a database record"},
            {"question": "What is Python's execution model?", "answer": "It is an interpreted, high-level language"}
        ]
        
        self.current_index = 0
        self.showing_answer = False

        self.tracker_label = tk.Label(root, text="", font=("Arial", 11), bg="#1e1e2e", fg="#a6adc8")
        self.tracker_label.pack(pady=15)

        self.card_box = tk.Button(
            root, text="", font=("Arial", 16, "bold"), bg="#313244", fg="#cdd6f4",
            wraplength=350, width=30, height=8, bd=0, cursor="hand2",
            activebackground="#45475a", activeforeground="#cdd6f4",
            command=self.toggle_flip
        )
        self.card_box.pack(pady=10)

        self.hint_label = tk.Label(root, text="(Click the card box above to flip)", font=("Arial", 9, "italic"), bg="#1e1e2e", fg="#585b70")
        self.hint_label.pack(pady=5)

        nav_frame = tk.Frame(root, bg="#1e1e2e")
        nav_frame.pack(pady=15)

        self.prev_btn = tk.Button(nav_frame, text="Prev", font=("Arial", 11), bg="#11111b", fg="#a6e3a1", width=8, bd=0, command=self.prev_card)
        self.prev_btn.grid(row=0, column=0, padx=15)

        self.delete_btn = tk.Button(nav_frame, text="Delete", font=("Arial", 11), bg="#11111b", fg="#f38ba8", width=8, bd=0, command=self.delete_card)
        self.delete_btn.grid(row=0, column=1, padx=15)

        self.next_btn = tk.Button(nav_frame, text="Next", font=("Arial", 11), bg="#11111b", fg="#a6e3a1", width=8, bd=0, command=self.next_card)
        self.next_btn.grid(row=0, column=2, padx=15)

        divider = tk.Frame(root, height=2, bg="#313244", width=380)
        divider.pack(pady=10)

        form_label = tk.Label(root, text="Add New Flashcard", font=("Arial", 12, "bold"), bg="#1e1e2e", fg="#cdd6f4")
        form_label.pack(pady=5)

        self.q_entry = tk.Entry(root, font=("Arial", 11), bg="#313244", fg="#cdd6f4", insertbackground="white", width=35, bd=0)
        self.q_entry.pack(pady=5, ipady=4)

        self.a_entry = tk.Entry(root, font=("Arial", 11), bg="#313244", fg="#cdd6f4", insertbackground="white", width=35, bd=0)
        self.a_entry.pack(pady=5, ipady=4)

        self.save_btn = tk.Button(root, text="Save Flashcard", font=("Arial", 11, "bold"), bg="#89b4fa", fg="#11111b", width=20, bd=0, command=self.add_card)
        self.save_btn.pack(pady=10, ipady=2)

        self.update_ui()

    def update_ui(self):
        if self.flashcards:
            total = len(self.flashcards)
            self.tracker_label.config(text=f"Card {self.current_index + 1} of {total}")
        
            
            if self.showing_answer:
                self.card_box.config(text=self.flashcards[self.current_index]["answer"], fg="#a6e3a1", bg="#45475a")
            else:
                self.card_box.config(text=self.flashcards[self.current_index]["question"], fg="#cdd6f4", bg="#313244")
        else:
            self.tracker_label.config(text="0 Cards Available")
            self.card_box.config(text="No flashcards left!\nCreate a new one below.", fg="#fab387", bg="#313244")

    def toggle_flip(self):
        if self.flashcards:
            self.showing_answer = not self.showing_answer
            self.update_ui()

    def next_card(self):
        if self.flashcards:
            self.current_index = (self.current_index + 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_ui()

    def prev_card(self):
        if self.flashcards:
            self.current_index = (self.current_index - 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_ui()

    def add_card(self):
        q = self.q_entry.get().strip()
        a = self.a_entry.get().strip()
        
        if q and a:
            self.flashcards.append({"question": q, "answer": a})
            self.q_entry.delete(0, tk.END)
            self.a_entry.delete(0, tk.END)
            self.current_index = len(self.flashcards) - 1
            self.showing_answer = False
            self.update_ui()
        else:
            messagebox.showwarning("Empty Fields", "Please type both a question and answer!")

    def delete_card(self):
        if self.flashcards:
            self.flashcards.pop(self.current_index)
            if self.current_index >= len(self.flashcards) and self.flashcards:
                self.current_index = len(self.flashcards) - 1
            elif not self.flashcards:
                self.current_index = 0
            self.showing_answer = False
            self.update_ui()

if __name__ == "__main__":
    window = tk.Tk()
    app = FlashcardApp(window)
    window.mainloop()
