import json
import re
import tkinter as tk
from tkinter import messagebox, ttk
from bs4 import BeautifulSoup, Comment

class ExamAnswerExtractor:
    def __init__(self):
        self.answers_window = None
        self.root = tk.Tk()
        self.root.title("SHOW MY ANSWERS - CISCO Exam Answer Extractor")
        self.root.configure(bg="black")  # Set background color
        self.root.resizable(False, False)
        self.root.geometry("550x550")
        self.root.configure(bg="black")

        # Label for the big heading
        tk.Label(self.root, text="SHOW MY ANSWERS", bg="black", fg="red", font=("Arial", 20, "bold")).pack(pady=(20, 0))

        # Label and Text widget for entering JSON code
        tk.Label(self.root, text="Paste your JSON code below...", bg="black", fg="white", font=("Fira Code", 12)).pack()
        self.json_text_entry = tk.Text(self.root, height=16, width=100, bg="black", fg="white", insertbackground="white", font=("Arial", 16))
        self.json_text_entry.pack(padx=10, pady=(10, 0))  # Adjust padding as needed

        # Create a frame to hold the buttons and center it horizontally
        button_frame = tk.Frame(self.root, bg="black")
        button_frame.pack(fill="x", pady=(20, 0))

        # Button to save JSON data
        save_button = tk.Button(button_frame, text="Save JSON Data", command=self.save_json_button_click, bg="white", fg="black", padx=10, pady=5, font=("Arial", 12), width=12)
        save_button.pack(side="left", padx=(10, 5))

        # Button to get answers
        get_answers_button = tk.Button(button_frame, text="Get Answers", command=self.display_answers, bg="white", fg="black", padx=10, pady=5, font=("Arial", 12), width=10)
        get_answers_button.pack(side="left", padx=(5, 5))

        # Button to display developer details
        dev_button = tk.Button(button_frame, text="Developer Details", command=self.show_developer_details, bg="white", fg="black", padx=10, pady=5, font=("Arial", 12), width=12)
        dev_button.pack(side="left", padx=(5, 5))

        # Exit button
        exit_button = tk.Button(button_frame, text="Exit", command=self.exit_program, bg="white", fg="black", padx=10, pady=5, font=("Arial", 12), width=10)
        exit_button.pack(side="left", padx=(5, 10))

    def show_developer_details(self):
        developer_window = tk.Toplevel(self.root)
        developer_window.title("Developer Details")
        developer_window.geometry("450x100")  # Set the size of the window
        message = "Developer : B. PAVAN KUMAR\nGitHub      : www.github.com/pth55\nEmail        : 238w5a1201@vrsec.ac.in"
        tk.Label(developer_window, text=message, font=("Arial", 16), justify='left').pack(padx=10, pady=10, anchor='w')

    def save_json_data(self, json_data):
        try:
            with open('data.json', 'w', encoding='utf-8') as file:
                file.truncate(0)  # Clear existing content if writing
                json.dump(json_data, file)
            messagebox.showinfo("Success", "JSON data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving JSON data: {str(e)}")


    def save_json_button_click(self):
        try:
            json_data = json.loads(self.json_text_entry.get("1.0", "end-1c"))
            # Save JSON data to file
            self.save_json_data(json_data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def exit_program(self):
        self.root.destroy()

    def remove_tags(self, element):
        if element is None:
            return ''

        if element.name in ['script', 'style', Comment]:
            return ''

        result = []
        for content in element.contents:
            if not isinstance(content, str):
                content = self.remove_tags(content)
            result.append(content)

        return ''.join(result)

    def close_answers_window(self):
        if self.answers_window:
            self.answers_window.destroy()
            self.root.deiconify()  # Re-enable the main window when the answers window is closed

    def display_answers(self):
        self.root.withdraw()
        self.answers_window = tk.Toplevel(self.root)
        self.answers_window.title("Answers")
        self.answers_window.configure(bg="black")  # Set background color
        self.answers_window.geometry("600x650")
        self.answers_window.resizable(True, False) # width, height
        self.answers_window.grab_set()  # Make the window modal

        # Frame to hold the contents with scrollbar
        frame = tk.Frame(self.answers_window, bg="black")
        frame.pack(fill="both", expand=True)

        # Canvas widget
        canvas = tk.Canvas(frame, bg="black")
        canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        def on_mouse_wheel(event):
            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        # Bind mouse wheel events to canvas for scrolling
        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        # Frame inside the canvas
        inner_frame = tk.Frame(canvas, bg="black")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # Load JSON data from data.json
        try:
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No JSON data found. Please save JSON data first.")
            return
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading JSON data: {str(e)}")
            return

        # Extract information for all questions
        if "questions" in data and len(data["questions"]) > 0:
            for quest_no, question_data in enumerate(data["questions"], start=1):
                # Display the question
                question_html = question_data["question"]
                question_soup = BeautifulSoup(question_html, 'html.parser')
                question_text = self.remove_tags(question_soup)

                # Frame for each question and its answer
                question_frame = tk.Frame(inner_frame, bg="black")
                question_frame.pack(fill="x", padx=10, pady=5)

                # Bold label for question number
                tk.Label(question_frame, text=f"Question {quest_no} Answer: ", font=("Arial", 12, "bold"), bg="black", fg="white").pack(side="left")

                # Check if the question type is "Single Choice" or "Multiple Choice"
                if question_data.get("type") == "Single Choice":
                    # Extract the first option
                    first_option_data = question_data["options"][0]["option"]

                    # Check if the first option contains a <code> tag
                    if '<code>' in first_option_data:
                        # Extract the content inside <code> tag
                        first_option_code = re.search(r'<code[^>]*>(.*?)<\/code>', first_option_data, re.DOTALL)
                        first_option = first_option_code.group(1).strip() if first_option_code else None
                    else:
                        # The first option is plain text
                        first_option = first_option_data.strip()

                    # Remove HTML tags from the answer
                    first_option_text = self.remove_tags(BeautifulSoup(first_option, 'html.parser'))

                    # Label for answer
                    tk.Label(question_frame, text=f"{first_option_text}", font=("Arial", 11), wraplength=500, anchor="w", justify="left", bg="black", fg="white").pack(fill="x")

                elif question_data.get("type") == "Multiple Choice":
                    if "(Select two answers.)" or "Choose all correct ansers." in question_text:
                        # Print two options
                        answer_text = f"Answer: [This is Multiple Choice] ==> "
                        count = 1
                        for option in question_data["options"][:2]:
                            option_text = self.remove_tags(BeautifulSoup(option["option"], 'html.parser'))
                            answer_text += f"Option-{count}: {option_text} "
                            count += 1
                        # Label for answer
                        tk.Label(question_frame, text=answer_text, wraplength=500, anchor="w", justify="left", bg="black", fg="white").pack(fill="x")
                    else:
                        # Label for answer
                        tk.Label(question_frame, text="Answer: (Multiple Choice question)", wraplength=500, anchor="w", justify="left", bg="black", fg="white").pack(fill="x")
                tk.Label(inner_frame, text="", bg="black").pack()  # Empty label for spacing

        else:
            tk.Label(inner_frame, text="No questions found in the data.", anchor="w", justify="left", bg="black", fg="white").pack(fill="x")

        # Update scrollregion after adding all widgets to inner_frame
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Frame to hold the "Developed by" text
        developed_by_frame = tk.Frame(inner_frame, bg="black")
        developed_by_frame.pack(fill="both", expand=True, padx=10, pady=(10, 0))

        # Developed by label
        developer_label = tk.Label(developed_by_frame, text="Developed by PAVAN KUMAR BANDARU", font=("Arial", 16), bg="black", fg="orange")
        developer_label.pack(side="bottom")

        # Close button
        tk.Button(self.answers_window, text="Done", command=self.close_answers_window, bg="white", fg="black", padx=10, pady=5, font=("Arial", 12)).pack(pady=(10, 10))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    extractor = ExamAnswerExtractor()
    extractor.run()
