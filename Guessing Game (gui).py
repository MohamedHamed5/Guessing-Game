

# Project Name: Guessing Game with (GUI)
# Date: 4/29/26
# Team Members:
# 1- Amira Saber Saadin Amer
# 2- Malak Tarek Saleh El-Belasy
# 3- Mariam El-Mofty Abdelshafy El-Hamady
# 4- Menna Mohamed Diab
# 5- Mohamed Ahmed AlSayed Hamed (TL)
# 6- Mohamed Mostafa
# 7- Mohamed Rami Zakaria
# 8- Mostafa Kamel Abo El-Ezz
# 9- Somaya Hesham El-Sayed Ahmed Ali Gomaa
# 10- Yasmin Mostafa Yassin El-Sayed

import customtkinter as ctk
import random
import math

# General appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Calcs the num of attempts needed for Binary Search Algorthim (BSA) to reach the target number
def get_optimal_attempts(target, low, high):

    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if mid == target:
            return count
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return count

class GuessGameGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Guessing Game")
        self.geometry("600x550")
        
        # Game variables
        self.target_number = 0
        self.attempts = 0
        self.low = 1
        self.high = 100
        self.optimal_needed = 0
        
        # Rankings
        self.best_rank = "None"

        # ال main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.show_main_menu()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_frame()
        
        label = ctk.CTkLabel(self.main_frame, text="WECOME TO THE GUESS GAME", font=("Roboto", 26, "bold"), text_color="#3498DB")
        label.pack(pady=30)

        rank_color = "#FFD700" if self.best_rank != "None" else "gray"
        self.rank_label = ctk.CTkLabel(self.main_frame, text=f"Your Best Rank: {self.best_rank}", font=("Roboto", 18), text_color=rank_color)
        self.rank_label.pack(pady=10)

        btn2 = ctk.CTkButton(self.main_frame, text="Computer Guesses Your Number", command=self.start_computer_mode, height=45, fg_color="transparent", border_width=2)
        btn2.pack(pady=10, padx=40, fill="x")
        
        btn1 = ctk.CTkButton(self.main_frame, text="Start A Hard Challenge (You Guess)", command=self.start_user_mode, height=45, fg_color="transparent", border_width=2)
        btn1.pack(pady=15, padx=40, fill="x")


        btn_exit = ctk.CTkButton(self.main_frame, text="Exit Game", fg_color="#C0392B", hover_color="#A93226", command=self.quit)
        btn_exit.pack(pady=20)

    def start_user_mode(self):
        self.clear_frame()
        self.target_number = random.randint(1, 100)
        self.optimal_needed = get_optimal_attempts(self.target_number, 1, 100)
        self.attempts = 0

        self.info_label = ctk.CTkLabel(self.main_frame, text=f"I've picked a number (1-100)\nTry to find it in {self.optimal_needed} attempts or less!", font=("Roboto", 18))
        self.info_label.pack(pady=20)

        self.user_input = ctk.CTkEntry(self.main_frame, placeholder_text="Enter your guess", width=200, font=("Roboto", 16))
        self.user_input.pack(pady=10)
        self.user_input.bind("<Return>", lambda e: self.check_user_guess())

        self.result_label = ctk.CTkLabel(self.main_frame, text="", font=("Roboto", 15))
        self.result_label.pack(pady=15)

        self.btn_guess = ctk.CTkButton(self.main_frame, text="Submit Guess", command=self.check_user_guess, height=40)
        self.btn_guess.pack(pady=10)

        self.btn_play_again = ctk.CTkButton(self.main_frame, text="New Round", command=self.start_user_mode, fg_color="#2ECC71")
        
        btn_back = ctk.CTkButton(self.main_frame, text="Back to Menu", fg_color="gray", command=self.show_main_menu)
        btn_back.pack(side="bottom", pady=20)

    def check_user_guess(self):
        try:
            val = self.user_input.get()
            if not val: return
            guess = int(val)
            self.attempts += 1
            self.user_input.delete(0, 'end')

            if guess < self.target_number:
                self.result_label.configure(text=f"Higher! Try a greater number. (Attempt: {self.attempts})", text_color="#E67E22")
            elif guess > self.target_number:
                self.result_label.configure(text=f"Lower! Try a samller number. (Attempt: {self.attempts})", text_color="#E67E22")
            else:
                self.show_victory_screen()
        except ValueError:
            self.result_label.configure(text="Please enter a valid number!", text_color="#E74C3C")

    def show_victory_screen(self):
        self.user_input.configure(state="disabled")
        self.btn_guess.pack_forget()
        
        diff = self.attempts - self.optimal_needed
        
        if diff <= 0:
            rank, color = "LEGENDARY (Perfect!)", "#F1C40F"
        elif diff == 1:
            rank, color = "MASTER (Close!)", "#9B59B6"
        elif diff <= 3:
            rank, color = "PRO (Good Job)", "#3498DB"
        else:
            rank, color = "APPRENTICE", "#95A5A6"

        # Best Rank to be Updated
        rank_order = {"LEGENDARY (Perfect!)": 4, "MASTER (Close!)": 3, "PRO (Good Job)": 2, "APPRENTICE": 1, "None": 0}
        if rank_order[rank] > rank_order[self.best_rank]:
            self.best_rank = rank

        victory_text = f"CORRECT! The number was {self.target_number}\n\n"
        victory_text += f"Your Attempts: {self.attempts}\n"
        victory_text += f"Optimal Possible: {self.optimal_needed}\n\n"
        victory_text += f"RANK: {rank}"
        
        self.result_label.configure(text=victory_text, text_color=color, font=("Roboto", 18, "bold"))
        self.btn_play_again.pack(pady=10)

    # Machine Guessing Mode
    def start_computer_mode(self):
        self.clear_frame()
        self.low, self.high, self.attempts = 1, 100, 0
        
        ctk.CTkLabel(self.main_frame, text="Computer Guessing Mode", font=("Roboto", 20, "bold")).pack(pady=20)
        self.guess_display = ctk.CTkLabel(self.main_frame, text="Think of a number...", font=("Roboto", 22), text_color="#3498DB")
        self.guess_display.pack(pady=20)

        self.feedback_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        ctk.CTkButton(self.feedback_frame, text="Smaller", fg_color="#E74C3C", command=lambda: self.comp_feedback("smaller")).grid(row=0, column=0, padx=5)
        ctk.CTkButton(self.feedback_frame, text="Correct!", fg_color="#2ECC71", command=lambda: self.comp_feedback("true")).grid(row=0, column=1, padx=5)
        ctk.CTkButton(self.feedback_frame, text="Greater", fg_color="#3498DB", command=lambda: self.comp_feedback("greater")).grid(row=0, column=2, padx=5)

        self.btn_start = ctk.CTkButton(self.main_frame, text="Start", command=self.next_comp_guess)
        self.btn_start.pack(pady=10)

        ctk.CTkButton(self.main_frame, text="Back", fg_color="gray", command=self.show_main_menu).pack(side="bottom", pady=20)

    def next_comp_guess(self):
        if self.low <= self.high:
            self.attempts += 1
            self.curr = (self.low + self.high) // 2
            self.guess_display.configure(text=f"Is it {self.curr}?")
            self.btn_start.pack_forget()
            self.feedback_frame.pack(pady=20)
        else:
            self.guess_display.configure(text="Contradictory hints!", text_color="red")

    def comp_feedback(self, f):
        if f == "true":
            self.guess_display.configure(text=f"Found it in {self.attempts} attempts!", text_color="#2ECC71")
            self.feedback_frame.pack_forget()
        elif f == "greater": self.low = self.curr + 1; self.next_comp_guess()
        else: self.high = self.curr - 1; self.next_comp_guess()


app = GuessGameGUI()
app.mainloop()
